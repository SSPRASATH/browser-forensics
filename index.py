import platform 
import os
import sys
import sqlite3
import json, ast
from urlparse import urlparse


def findPlatform():
	return platform.system()

def menu():
	print '\nMENU:'
	print '\n\t1. Analysis'
	print '\t2. System Info'
	print '\t3. About'
	print '\t4. Exit'	
	cond()

def getinput():
	sol=raw_input('\nResponse: What you want to do >_ ')
	return sol

def cond():
	inpt=getinput()
	if inpt=='1':
		Analysis()
	elif inpt=='2':
		sysinfo()
	elif inpt=='3':
		About()
	elif inpt=='4':
		os.system('clear')
		os.system(exit())
	else:
		print '\x1b[6;37;41m' + 'choose correct option' + '\x1b[0m'
		cond()
		
def index(dist):
	a = dist
	Archi=platform.machine()	
	print '\t\t ------- BOWSPY -------'
	print '\n\t\t\tBASIC INFO\n' 
	print '======================================================='
	print '\t\tOperating System:',a
	print '\t\tArchitecture    :',Archi
	print '======================================================='
	menu()


def Analysis():
	print '\n======================================================='
	print '\t\t\tANALYSIS'
	print '=======================================================\n'
	print '\nMENU:'
	print '\n\t1. Scan'
	print '\t2. Collect Evidence'
	print '\t3. Previous'
	choice_cond()
def getchoice():
		choice_input=raw_input('\nEnter the choice >_  ')
		return choice_input
def choice_cond():
	choice=getchoice()
	if choice=='1':
		scan()
	elif choice=='2':
		print 'Collect Evidence'
	elif choice=='3':
		getinput()
	else:
		print 'other evidence'
		choice_cond()
def scan():
	browser = ['firefox','google-chrome','opera']
	os_browser=[]
	i=0
	print '\n======================================================='
	print '\n\x1b[6;30;46m' + '>_INSTALLED BROWSERS' + '\x1b[0m \n'
	for sof in browser:
		resulr_browser = os.path.exists("/usr/bin/" +sof)
		if resulr_browser is True:
			os_browser.append(sof)
	total_no_of_bow = len(os_browser)
	print 'NO OF BOWSER    :', total_no_of_bow
	print 'LIST OF BROWSER :'
	for x in os_browser:
		print '\t\t [~]',x.upper()
		i=i+1
	print '\nADVANCE OPTIONS :\n'
	print '\t\t  [N] NORMAL SCAN {HISTORY}'
	print '\t\t  [D] DEEP   SCAN {HISTORY,COOKIES,SO ON}'
	print '\t\t  [C] CUSTOM SCAN {SEARCH}'
	evid=raw_input('Enter ur choice (N/D/C)(CAPS)>_ ')
	if evid=='N':
		normal()
	elif evid=='D':
		deep()
	elif evid=='C':
		custom()
	else:
		print 'Worng input'
		cond()




def normal():
	print '\n======================================================='
	print '\t\t     NORMALSCAN'
	print '=======================================================\n'
	print 'This scan only HISTORY..\n'
	print 'EVIDENCE STATUS : \x1b[6;37;41m' + 'INITIATED' + '\x1b[0m\n'
	file_import()
	print 'EVIDENCE STATUS : \x1b[6;37;42m' + 'COLLECTED' + '\x1b[0m\n' 
	place()
	print '\n=======================================================\n'
	cond()






def deep():
	print '\n======================================================='
	print '\t\t     DEEP'
	print '=======================================================\n'
	print 'This ADVANCED SACNING..\n'
	print 'EVIDENCE STATUS : \x1b[6;37;41m' + 'INITIATED' + '\x1b[0m\n'
	file_import()
	print 'EVIDENCE STATUS : \x1b[6;37;42m' + 'COLLECTED' + '\x1b[0m\n' 
	print '\nADVANCES OPTION'
	print '\t 	1. HISTORY'
	print '\t	2. SEARCH'
	print '\t 	3. WEBAPP'
	print '\t 	4. FROMHISTORY'
	print '\t 	5. COOKIES'
	print '\t 	6. PERMISSIONS'
	dcon()

def deepchoice():
	dch=raw_input('Enter the Deep choice>_ ')
	return dch
def histo():
	place()
	favicon()
	host()
	dcon()


def dcon():
	dchi = deepchoice()
	if dchi=='1':
		histo()	
		
	elif dchi=='2':
		searchs()
		dcon()
	elif dchi=='3':
		weapp()
		dcon()
	elif dchi=='4':
		fromhis()
		dcon()
	elif dchi=='5':
		cookiess()
		dcon()
	elif dchi=='6':
		perm()
		dcon()
	else:
		cond()




def custom():
	print 'YET TO CODE'

def file_import():
	os.system('cd ~/.mozilla/firefox/;find -name *.sqlite > read.txt')
	os.system('cp ~/.mozilla/firefox/read.txt ./')

	with open('read.txt') as f:
	    lines = f.readlines()
	k=lines[0]
	l=k.split('/')
	os.system('cp ~/.mozilla/firefox/'+l[1]+'/*.sqlite ./ -rf')
	return


# DATA PROCESSING
#place 
def place():
 	print '\n=======================================================\n'

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
		print '\t[-]',x
	print '\n=======================================================\n'	

	return


def favicon():
 	print '\n=======================================================\n'
	connp = sqlite3.connect('places.sqlite')
	print 'FAVICON'
	cursor_fav = connp.execute("select * from moz_favicons;")
	fav_place=[]
	for x in cursor_fav:
		yfav=urlparse(x[1]).hostname
		fav_place.append(yfav)

	temp_favicon=set(fav_place)
	result_fav={}
	for i in temp_favicon:
		result_fav[i]=fav_place.count(i)
	k_fav=ast.literal_eval(json.dumps(result_fav))
	for x in k_fav:
		print '\t[-]',x
	print '\n=======================================================\n'	
	return

def host():
 	print '\n=======================================================\n'
	connp = sqlite3.connect('places.sqlite')
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
		print '\t[-]',x
	print '\n=======================================================\n'	

	return

def  searchs():
	conns = sqlite3.connect('content-prefs.sqlite')
	
	cursor_sear = conns.execute("select * from groups;")
	for row in cursor_sear:
		print '\t[+]', row[1]
	return



def perm():
	connpp = sqlite3.connect('permissions.sqlite')
	cursor_per = connpp.execute("select * from moz_perms;")
	for row in cursor_per:
	   print '\t[-]', row[1]
	return


def cookiess():
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
	return

def weapp():
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
	return


def searchs():
	conns = sqlite3.connect('content-prefs.sqlite')
	cursor_sear = conns.execute("select * from groups;")
	for row in cursor_sear:
		print '\t[+]', row[1]
	return



def fromhis():
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

	return		







def sysinfo():
	print '\n======================================================='
	print '\t\t   SYSTEM INFORMATION'
	print '=======================================================\n'

	print'\tSYSTEM     :',platform.system()
	print'\tPLATFORM   :',platform.architecture()[0]
	print'\tkERNAL     :',platform.release()
	print'\tPROCESSOR  :',platform.processor()
	print'\tMODEL	   :',platform.node()
	cond()
def About():
	print '\n======================================================='
	print '\t\t\t  ABOUT'
	print '=======================================================\n' 
	print' SUPPORTED BROWSERS : google-chrome,firefox,opera'
	print' FEATURES: The browser list can be updated manually,\n It allows to perform the basic filter operation based on keywords\n YET TO UPDATED'
	print' CREDITS : SP:),PANDA,ASHOK KUMAR'
	print'\n'
	cond()
def linuxOs():
	Dist = platform.dist()[0]
	index(Dist)

def windowsOs():
	print 'Windows  Function'

def macOs():
	print 'Mac Function' 

def find_fal():
	fl = findPlatform()
	if fl=='Linux':
		linuxOs()
	elif fl == 'Windows':
		windowsOs()
	elif fl == 'Mac':
		macOs()
	else:
		print 'unknown Operating System'
			
	
def call():
	find_fal()

def main():
	os.system('clear')
	
	call()

if __name__ == '__main__':
	main()