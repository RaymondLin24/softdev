# Raymond Lin
# Death Row Coders
# SoftDev
# K09 <CSV file parsing, flask, displaying to HTML>
# 2024-9-24
# Time Spent : 0.5 Hours

import random
import csv
from flask import Flask

app = Flask(__name__)

def readfile(f):
    d = {}
    with open (f, 'r') as listfile:
        reader = csv.reader(listfile)
        next(reader)
        for row in reader:
            job = row[0]
            if job == "Total":
                continue
            percent = float(row[1])
            d[job] = percent
    return d
        
        
def sel(d):
    return random.choices(list(d.keys()), weights=d.values(), k=1)[0]

@app.route("/")

def page():
    occ = sel(readfile("occupations.csv"))
    code = """
    <!DOCTYPE html>
    <html>
      <body>
            <p>Death Row Coders with Raymond, Christopher, and Kevin. Traveling team with Yinwei, Endrit, Raymond.</p>
            <h1>This time: """ + occ + """
            <h2>Occupations</h2>
    """
    for a, b in readfile("occupations.csv").items():
        code += "<li>" + a + ": " + str(b) + "</li>"

    code += "</body></html>"
    return code

if __name__ == "__main__":
    app.debug = True
    app.run()