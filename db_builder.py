import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...


q = "CREATE TABLE peeps (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

for k in d:
	c.execute("INSERT INTO peeps VALUES('" + k['name'] + "', " + k['id']+ ')')
	

'''

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
'''

#==========================================================
db.commit() #save changes
db.close()  #close database


