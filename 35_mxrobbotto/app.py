from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        cur = get_db().cursor()
        cur.execute("SELECT id, title, latest_text FROM stories")
        stories = cur.fetchall()
        cur.execute("SELECT title, latest_text FROM stories WHERE id IN (SELECT story_id FROM contributions WHERE user_id=?)", (user_id,))
        user_stories = cur.fetchall()
        return render_template('home.html', stories=stories, user_stories=user_stories)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = get_db().cursor()
        cur.execute("SELECT id, password FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/new_story', methods=['GET', 'POST'])
def new_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        user_id = session['user_id']
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO stories (title, latest_text) VALUES (?, ?)", (title, text))
        story_id = cur.lastrowid
        cur.execute("INSERT INTO contributions (user_id, story_id) VALUES (?, ?)", (user_id, story_id))
        db.commit()
        return redirect(url_for('index'))
    return render_template('new_story.html')


@app.route('/add_to_story/<int:story_id>', methods=['GET', 'POST'])
def add_to_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT latest_text FROM stories WHERE id=?", (story_id,))
    story = cur.fetchone()
    cur.execute("SELECT 1 FROM contributions WHERE user_id=? AND story_id=?", (user_id, story_id))
    has_contributed = cur.fetchone()
    if has_contributed:
        return "You have already contributed to this story."
    if request.method == 'POST':
        text = request.form['text']
        cur.execute("UPDATE stories SET latest_text=? WHERE id=?", (text, story_id))
        cur.execute("INSERT INTO contributions (user_id, story_id) VALUES (?, ?)", (user_id, story_id))
        db.commit()
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
                        latest_text TEXT NOT NULL)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS contributions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        story_id INTEGER NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(story_id) REFERENCES stories(id))''')
        db.commit()
    app.run(debug=True)
