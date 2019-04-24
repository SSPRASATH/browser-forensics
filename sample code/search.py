import sqlite3

conn = sqlite3.connect('content-prefs.sqlite')
print "Opened database successfully";

cursor = conn.execute("select * from groups;")
for row in cursor:
	   print "domain = %s %s", row[0]