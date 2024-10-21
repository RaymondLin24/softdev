## K19: All Your Database Are Belong To Us
### Due: 2024-10-21m before class

_Step 0: Establish team comms. Fetch KtS._

#### Your trio MISSION: 
Write a __simple Python script__ to import CSV data into a relational database.
* Read data from CSV files,
* create a database whose table structure mimics that of CSV files.
* (In the care package you will find a CSV file of students and their IDs, and another linking said IDs to the students' current grades in some courses. Desire more lulz? Add extra, more expansive CSVs.)

##### TASK the Foist: 
Familiarize yourself with Python's CSV module, specifically its DictReader() method, as it will greatly expedite your work going forward. (If you are already familiar, do your crew a solid and *share protips/insights*.)

---

##### TASK the Second: 
Read through the python skeleton db-building script, and talk it over with your ducky and teammates BEFORE you begin making it your own...

---

##### TASK the Toid:

Flesh out skeleton python script, which will...
* create a new SQLite database,
* utilize `csv.DictReader()` to read each provided CSV file,
* create a table for each,
* populate each table.

---

<br>

Specifications/Guidelines:
* Use Q&A forum liberally.
* Comment liberally in-line. Speak to your future self and/or teammates.
* Note anything notable in readme in app's root directory. (_KtS on hand always..._). Convert to markdown file if necessary.
* _Behold! A care package awaits you. (You will need it for this...)_
* __Use the sqlite shell__ to test SQL commands _before_ baking them into your Python script. (`$ sqlite3` to launch, `Ctrl-D` to exit)
* _Reminder:_ include heading as comment in all source files.
<br>

PROTIPS:
* _Simplicity is divine_.
* **Diagnostic print statements are your friend.**
  - Use them liberally.
  - When not in use, comment out rather than delete.
* `Ctrl-Z` will send a process (like a running sqlite shell) to the background; `fg` or `%` will bring it back to the foreground.
* It may be helpful during development to delete your db file between runs.


DELIVERABLES:
* In your heading, replace your name with your TNPG and roster.
* Save to workshop as indicated.

```
path/to/myworkshop$ tree 19_csv2db
.
├── courses.csv
├── build_db.py
├── readme
└── students.csv
```


<br>

related:
<br>
[sqlite3 shell 411](https://www.sqlite.org/cli.html)
<br>
[...](https://www.youtube.com/watch?v=8fvTxv46ano)
<br>
[...]()
