import os

os.system('cd ~/.mozilla/firefox/;find -name *.sqlite > read.txt')
os.system('cp ~/.mozilla/firefox/read.txt ./')

with open('read.txt') as f:
    lines = f.readlines()
k=lines[0]
l=k.split('/')
os.system('cp ~/.mozilla/firefox/'+l[1]+'/*.sqlite ./ -rf')
