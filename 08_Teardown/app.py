#Raymond Lin
#Louie-Lin 4 Da Win
#SoftDev
#K08_Teardown/Printing to HTML/Using flask to print to HTML
#2024/9/20
#30 Minutes

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. Java, NetLogo, and many other languages as this is usually the simplest way for variable assignment
1. File System Root
2. To the console of the site
3. Prints the name of the app 
4. It appears as HTML, we can see it on the site
5. Java
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():                  
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



