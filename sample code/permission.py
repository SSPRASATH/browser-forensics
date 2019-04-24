import sqlite3

connpp = sqlite3.connect('permissions.sqlite')

cursor_per = connpp.execute("select * from moz_perms;")
for row in cursor_per:
	   print '\t[-]', row[1]