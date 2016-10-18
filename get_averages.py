import sqlite3

db = open("discobandit.db")
c = db.cursor()

s = "SELECT name, courses.id, mark FROM students,courses WHERE student.id == courses.id"

dict = {}
for record in c.execute(s):
	if record[0] not in dict:
		dict[record[0]] = []
	
		




