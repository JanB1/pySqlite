import sqlite3

con = sqlite3.connect('data/test.db')

cur = con.cursor()

print(cur.connection == con)

#cur.execute('''CREATE TABLE test (Id INT, Data TEXT)''')

cur.execute('''CREATE TABLE person (
               Id INT NOT NULL PRIMARY KEY,
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
