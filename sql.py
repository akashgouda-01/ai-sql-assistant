import sqlite3

connection=sqlite3.connect("STUDENT.db")

cursor = connection.cursor()

table_info="""CREATE TABLE STUDENT(NAME VARCHAR(30), CLASS VARCHAR(30), SECTION VARCHAR(5), MARKS INT) """

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES('AKASH', 'AGENTIC AI', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('HEMA', 'AI-ML', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('HARJEET', 'GEN AI', 'B', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('AADHISH', 'WEBDEV', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('ALVIN', 'FULL STACK', 'C', 90)''')

connection.commit()
connection.close()

