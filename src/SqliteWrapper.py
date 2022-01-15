import sqlite3
import re
from pathlib import Path
full_database_path = 'data/test.db'


def create_database(file_path):
    # file_path = ''
    file_name = re.search('([^\/\\]+\.db)$)')

    if type(file_path) != str:
        raise ValueError

    # for i in range(len(full_file_path)-1, 0):
    #     if full_file_path[i] == '/' or full_file_path[i] == '\\':
    #         file_path = full_file_path[0:i]
    #         file_name = full_file_path[i+1:len(full_file_path)]
    #     elif i == 0:
    #         if file_path == '' and file_name == '':
    #             file_path = full_file_path
    #             file_name = full_file_path

    try:
        Path(file_path).mkdir(parents=True, exist_ok=True)
    except Exception:
        print(e)

    # return file_path, file_name


create_database(full_database_path)

try:
    con = sqlite3.connect('data/test.db')
    conEstablished = True
except Exception as e:
    print(e)

if conEstablished:
    cur = con.cursor()
    print(cur.connection == con)
    con.close()

# cur.execute('''CREATE TABLE person (
#               # Constrain for "Id" has to be "INTEGER PRIMARY KEY"
#               # to result in auto-increment column
#               Id INTEGER PRIMARY KEY,
#               LastName TEXT NOT NULL,
#               FirstName TEXT,
#               DateOfBirt TEXT)''')

# cur.execute('''INSERT INTO person VALUES (
#               NULL,
#               "Baumann",
#               "Jan",
#               "1900-01-01")''')

# con.commit()

#for row in cur.execute('''SELECT * FROM person'''):
#    print(row)

con.close()
