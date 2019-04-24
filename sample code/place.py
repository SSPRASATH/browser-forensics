import sqlite3
import json, ast
from urlparse import urlparse

connp = sqlite3.connect('places.sqlite')

places_url=[]

cursor_place = connp.execute("select * from moz_places;")
for row in cursor_place:

	if row[3]!='\0':
		places_url.append(row[1])
	
	

print '[+] HISTORY'
placesk=ast.literal_eval(json.dumps(places_url))
host_place=[]
for x  in places_url:
	y= urlparse(x).hostname
	host_place.append(y)
	

temp_palces=set(host_place)
result_places={}
for i in temp_palces:
	result_places[i]=host_place.count(i)
k_places=ast.literal_eval(json.dumps(result_places))
for x in k_places:
	print '[-]',x


print 'FAVICON'

cursor_fav = connp.execute("select * from moz_favicons;")
fav_place=[]
for x in cursor_fav:
	yfav=urlparse(x[1]).hostname
	fav_place.append(yfav)

temp_favicon=set(fav_place)
result_fav={}
for i in temp_favicon:
	result_fav[i]=host_place.count(i)
k_fav=ast.literal_eval(json.dumps(result_fav))
for x in k_fav:
	print '[-]',x



print 'HOST'

cursor_host = connp.execute("select * from moz_hosts;")
host_place=[]
for x in cursor_host:
	host_place.append(x[1])

temp_host=set(host_place)
result_host={}
for i in temp_host:
	result_host[i]=host_place.count(i)
k_host=ast.literal_eval(json.dumps(result_host))
for x in k_host:
	print '[-]',x


