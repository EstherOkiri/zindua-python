import sqlite3

db = sqlite3.connect('student_db.db')
cursor = db.cursor()

#cursor.execute('''
 #  CREATE TABLE student(
#       id INTEGER PRIMARY KEY,
 #      name TEXT,
 #      grade INTEGER
 #   )

#''')
name1 = 'Andres'
grade1 = 80
name2 = 'John'
grade2 = 90
name3 = 'Sheila'
grade3 = 50
name4= 'Elvis'
grade4 = 60

students_grades = [(name1, grade1), (name2,grade2),(name3,grade3),(name4,grade4)]
cursor.executemany('''INSERT INTO student(name,grade) VALUES(?,?)''',students_grades)

db.commit()
