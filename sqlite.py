import sqlite3
# Connect to sqlite
conn = sqlite3.connect('student.db')
#create cursor to insert record and create table
cursor = conn.cursor()
#create table
table_info = '''
CREATE TABLE student (Name VARCHAR(20),Class VARCHAR(20),Marks VARCHAR(20),
Section VARCHAR(20));   '''

cursor.execute(table_info)

#insert record

cursor.execute("INSERT INTO student VALUES('Raj','DataScience','100','A')")
cursor.execute("INSERT INTO student VALUES('Asim','Math','10','A')")
cursor.execute("INSERT INTO student VALUES('Wasim','Science','90','B')")
cursor.execute("INSERT INTO student VALUES('Ali','Physics','70','C')")


#Display all record
data=cursor.execute('''select * from student''')
for i in data:
    print(i)

conn.commit()
conn.close()