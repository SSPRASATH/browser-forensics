import os

os.system('cp ~/.mozilla/firefox ./ -rf')
os.system('cd firefox;find -name *.sqlite > read.txt')
with open('firefox/read.txt') as f:
    lines = f.readlines()
k=lines[0]
l=k.split('/')
os.system('cd firefox/'+l[1]+';cp *.sqlite ./')
