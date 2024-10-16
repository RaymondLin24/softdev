# Kevin Lin, Raymond Lin, Christopher Louie
# Death Row Coders
# SoftDev
# October 16, 2024
# 1 hour

import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    return render_template( 'index.html' )

if __name__ == "__main__":
    app.debug = True 
    app.run()