import sqlite3
import re
from pathlib import Path


def createDatabase(databasePath):
    try:
        Path('').mkdir(parents=True, exist_ok=True)

try:
    con = sqlite3.connect('data/test.db')
    conEstablished = True
except Exception as e:
    print(e)

if conEstablished:
    cur = con.cursor()
    print(cur.connection == con)
    con.close()

#cur.execute('''CREATE TABLE person (
#               # Constrain for "Id" has to be "INTEGER PRIMARY KEY"
#               # to result in auto-increment column
#               Id INTEGER PRIMARY KEY,
#               LastName TEXT NOT NULL,
#               FirstName TEXT,
#               DateOfBirt TEXT)''')

#cur.execute('''INSERT INTO person VALUES (
#               NULL,
#               "Baumann",
#               "Jan",
#               "1900-01-01")''')

#con.commit()

#for row in cur.execute('''SELECT * FROM person'''):
#    print(row)

#con.close()
