from flask import Flask, render_template
import random, csv
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
            d[job] = [float(row[1]),row[2]]
    return d        

def sel(d):
    newlist = []
    for num in list(d.values()):
        newlist.append(num[0])
    return random.choices(list(d.keys()), weights=newlist, k=1)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/wdywtbwygp")
def test_tmplt():
    occupations = readfile("data/occupations.csv")
    return render_template('tablified.html', collection1=occupations, occupation=sel(occupations))

if __name__ == "__main__":
    app.debug = True
    app.run()