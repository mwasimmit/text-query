import sqlite3

conn = sqlite3.connect('student.db')
#create cursor to insert record and create table
cursor = conn.cursor()
#create table

data = cursor.execute('''select * from student''')
for i in data:
    print(i)
conn.commit()
conn.close()