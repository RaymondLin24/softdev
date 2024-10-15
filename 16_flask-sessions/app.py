# Raymond Lin, Kevin Lin, Christopher Louie
# Death Row Coders
# SoftDev
# October 11, 2024
# 2 Hours

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
    if 'username' in session:
        return redirect("/response.html")
    return render_template( 'login.html' )

@app.route("/response.html" , methods=['GET','POST'])
def authenticate():
    #if(request.args.get('username') == None): #Lets you go back to response from logout and redirects to login, but breaks if you try to go back to login from response
    #    return redirect("/")
    if(request.args.get('username') != None): #Only change username if it's not none
        session['username'] = request.args.get('username')
    return render_template( 'response.html', username = session['username'])

@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template('logout.html')
    
if __name__ == "__main__":
    app.debug = True 
    app.run()