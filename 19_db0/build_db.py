#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
command = "CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);"
c.execute(command)

with open('courses.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses(code,mark,id) VALUES (?,?,?)", (row['code'],row['mark'],row['id']))

c.execute('SELECT * FROM courses') #Reads the table
table = c.fetchall() #Gets the data after reading it
for tab in table:
    print(tab)

with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO students(name,age,id) VALUES (?,?,?)", (row['name'],row['age'],row['id']))

c.execute('SELECT * FROM students') #Reads the table
table = c.fetchall() #Gets the data after reading it
for tab in table:
    print(tab)
#==========================================================

db.commit() #save changes
db.close()  #close database
