import sqlite3
import json, ast

conn = sqlite3.connect('formhistory.sqlite')
q=[]
url=[]
uname=[]
dom=[]
email=[]
log=[]
sea=[]
web=[]
cursor_fh = conn.execute("select * from moz_formhistory;")
for row in cursor_fh:

	if row[1]=='q':
		q.append(row[2])
	elif row[1]=='sf_url':
		url.append(row[2])
	elif row[1]=='username':
		uname.append(row[2])
	elif row[1]=='logData':
		log.append(row[2])
	elif row[1]=='domainToCheck':
		dom.append(row[2])
	elif row[1]=='searchbar-history':
		sea.append(row[2])
	elif row[1]=='email':
		email.append(row[2])
	elif row[1]=='Email':
		email.append(row[2])
	elif row[1]=='web_user[rhlogin]':
		web.append(row[2])
	

print '[+] KEYWORD'
qk=ast.literal_eval(json.dumps(q))
for x in qk:
	print '\t[-]',x
print '[+] URL'
urlk=ast.literal_eval(json.dumps(url))
for x in urlk:
	print '\t[-]',x
print '[+] USERNAME'
unamek=ast.literal_eval(json.dumps(uname))
for x in unamek:
	print '\t[-]',x
print '[+] SEARCH-HISTORY'
seak=ast.literal_eval(json.dumps(sea))
for x in seak:
	print '\t[-]',x
print '[+] EMAIL'
emailk=ast.literal_eval(json.dumps(email))
for x in emailk:
	print '\t[-]',x
print'[+] WEB USER LOGIN'
webk=ast.literal_eval(json.dumps(web))
for x in webk:
	print '\t[-]',x
print '[+] DOMAINTOCHECK'
domk=ast.literal_eval(json.dumps(dom))
for x in domk:
	print '\t[-]',x
print '[+] LOG DATA'
logk=ast.literal_eval(json.dumps(dom))
for x in logk:
	print '\t[-]',x

		
