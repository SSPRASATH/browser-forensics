import sqlite3
import ast, json
connwb = sqlite3.connect('webappsstore.sqlite')
# contain key
col=[]
cursor_webapp = connwb.execute("select * from webappsstore2;")
for row in cursor_webapp:
	   col.append(row[1][::-1])

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