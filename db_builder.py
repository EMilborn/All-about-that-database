import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

q =  "DROP TABLE IF EXISTS students"

c.execute(q)

q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

for k in d:
	c.execute("INSERT INTO students VALUES('" + k['name'] + "', " + k['id']+ ')')


q =  "DROP TABLE IF EXISTS courses"

c.execute(q)
    
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)

fObj = open("courses.csv") 
d=csv.DictReader(fObj)

for k in d:
	c.execute("INSERT INTO courses VALUES('" + k['code'] + "', " + k['id']+ ',' + k['mark'] + ')')

#==========================================================
db.commit() #save changes
db.close()  #close database


