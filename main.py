import sqlite3
from pathlib import Path

Path('data/').mkdir(parents=True, exist_ok=True)

try:
    con = sqlite3.connect('data/test.db')
except Error as e:
    print(e)

cur = con.cursor()

print(cur.connection == con)

cur.execute('''CREATE TABLE person (
               # Constrain for "Id" has to be "INTEGER PRIMARY KEY"
               # to result in auto-increment column
               Id INTEGER PRIMARY KEY,
               LastName TEXT NOT NULL,
               FirstName TEXT,
               DateOfBirt TEXT)''')

cur.execute('''INSERT INTO person VALUES (
               NULL,
               "Baumann",
               "Jan",
               "1900-01-01")''')

con.commit()

for row in cur.execute('''SELECT * FROM person'''):
    print(row)

con.close()
