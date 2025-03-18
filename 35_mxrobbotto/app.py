from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'database.db'

# Create a new connection for each request.
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row  # To access columns by name.
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def validate_password(password):
    # Check for a strong password with at least 8 characters, one number, and one special character.
    if len(password) < 8 or not re.search(r"\d", password) or not re.search(r"[A-Za-z]", password):
        return False
    return True

@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT id, title, latest_text FROM stories WHERE status='active'")
        stories = cur.fetchall()
        cur.execute("SELECT title, latest_text FROM stories WHERE id IN (SELECT story_id FROM contributions WHERE user_id=?)", (user_id,))
        user_stories = cur.fetchall()
        return render_template('home.html', stories=stories, user_stories=user_stories)
    flash('You need to log in first!', 'warning')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not validate_password(password):
            flash('Password must be at least 8 characters long and contain both numbers and letters.', 'danger')
            return render_template('register.html')
        
        hashed_password = generate_password_hash(password)
        db = get_db()
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            db.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists.', 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT id, password FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('index'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/new_story', methods=['GET', 'POST'])
def new_story():
    if 'user_id' not in session:
        flash('You need to log in to create a story!', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        user_id = session['user_id']
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO stories (title, latest_text, status) VALUES (?, ?, ?)", (title, text, 'active'))
        story_id = cur.lastrowid
        cur.execute("INSERT INTO contributions (user_id, story_id) VALUES (?, ?)", (user_id, story_id))
        db.commit()
        flash('Story created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('new_story.html')

@app.route('/add_to_story/<int:story_id>', methods=['GET', 'POST'])
def add_to_story(story_id):
    if 'user_id' not in session:
        flash('You need to log in to contribute to a story!', 'warning')
        return redirect(url_for('login'))

    user_id = session['user_id']
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT latest_text FROM stories WHERE id=?", (story_id,))
    story = cur.fetchone()
    
    if not story:
        flash('Story not found.', 'danger')
        return redirect(url_for('index'))

    cur.execute("SELECT 1 FROM contributions WHERE user_id=? AND story_id=?", (user_id, story_id))
    has_contributed = cur.fetchone()
    if has_contributed:
        flash('You have already contributed to this story.', 'warning')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        text = request.form['text']
        cur.execute("UPDATE stories SET latest_text=? WHERE id=?", (text, story_id))
        cur.execute("INSERT INTO contributions (user_id, story_id) VALUES (?, ?)", (user_id, story_id))
        db.commit()
        flash('Contribution added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_to_story.html', story=story)

if __name__ == '__main__':
    with app.app_context():
        db = get_db()
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS stories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        latest_text TEXT NOT NULL,
                        status TEXT DEFAULT 'active')''')
        cur.execute('''CREATE TABLE IF NOT EXISTS contributions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        story_id INTEGER NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(story_id) REFERENCES stories(id))''')
        db.commit()

    app.run(debug=True)
