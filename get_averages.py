import sqlite3

db = sqlite3.connect("discobandit.db")
c = db.cursor()

s = "SELECT name, courses.id, mark FROM students,courses WHERE students.id == courses.id"

dict = {}
for record in c.execute(s):
	if record[0] not in dict:
		dict[record[0]] = [record[1],record[2],1.0]
	else:
		dict[record[0]][1] += record[2]
		dict[record[0]][2] += 1

for name in dict:
	print "name = %s\nid = %d\naverage = %f \n\n"%(name, dict[name][0], dict[name][1]/dict[name][2])
		


	
	
		




