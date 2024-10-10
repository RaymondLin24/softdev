# Clyde 'Thluffy' Sinclair
# SoftDev
# October 2024

import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

@app.route("/")
def disp_loginpage():
    print(session.get('username'))
    if session.get('username'):
        print("TRUEEEEEEEEEEE")
    return render_template( 'login.html' )

@app.route("/response.html" , methods=['GET','POST'])
def authenticate():
    session['username'] = request.args.get('username')
    return render_template( 'response.html', username = request.args['username'])


    
if __name__ == "__main__":
    app.debug = True 
    app.run()