# Clyde 'Thluffy' Sinclair
# SoftDev
# October 2024

import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

@app.route("/")
def disp_loginpage():
    print(session.get('username'))
    if 'username' in session:
        return "you're session exists"
    return render_template( 'login.html' )

@app.route("/response.html" , methods=['GET','POST'])
def authenticate():
    session['username'] = request.args.get('username')
    return render_template( 'response.html', username = request.args['username'])

@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template('logout.html')
    
if __name__ == "__main__":
    app.debug = True 
    app.run()