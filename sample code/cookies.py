#contain cookies url

import sqlite3
import ast, json
connc = sqlite3.connect('cookies.sqlite')

col=[]
cursor_cookie = connc.execute("select * from moz_cookies;")
for row in cursor_cookie:
	   col.append(row[1])

temp=set(col)
result={}
for i in temp:
	result[i]=col.count(i)
k=ast.literal_eval(json.dumps(result))
for x in k:
	print '[+]',x
#print sorted(k.items(), key=lambda x:x[1])
#my_dict = {i:col.count(i) for i in col}
#print my_dic