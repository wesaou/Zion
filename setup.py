#!/usr/bin/python3

import ZiDisplay
import subprocess
import getpass
import re


GR = '\033[92m'
FA = '\033[91m'
BD = '\033[1m'
EC = '\033[0m'
nl = '\n'

#Installs Beautiful Soup for webscraping 
print(GR+BD+'[Installing Beautiful Soup...]'+EC) 
ibs = subprocess.getoutput('sudo apt-get install -y python-bs4')
wr = open('user.txt','w')

#Stores the user's name to a text file, for later use by Zion when addressing the user
while True:
    name = input(GR+BD+'First and last name (ex. John Doe): '+EC+BD)
    if not ' ' in name:
        print(FA+BD+'Please enter both first, and last name!')
        continue
    else:
        break

#Stores the email that was created by the user for Zion, and writes it to a text file for later use.
while True:
    eaddr = input(GR+BD+'Email address you created: '+EC+BD)
    if not '@' in eaddr:
        print(FA+BD+'Please enter the address of the email you created!')
        continue
    else:
        break
epass = getpass.getpass(GR+BD+'Email password: '+EC)

#Stores the phone number of the user, along with it's cell provider so Zion can reply to it's texts.
while True:
    phnum = input(GR+BD+'Cell phone Number for Zion to text: '+EC+BD)
    phnum = re.sub(r'[()]','',phnum)
    phnum = re.sub('-','',phnum)
    if len(phnum) != 10:
        print(FA+BD+'Please enter a valid 10 digit phone number!'+EC)
    else:
        break

print('Cell service provider:'+nl+EC+BD+'a)Verizon'+nl+'b)AT&T'+nl+'c)T-Mobile'+nl+'d)Sprint'+nl+'e)US Cellular')
aprov = input(GR+BD+'Select one: '+EC+BD)
if aprov == 'a':
    prov = '@vtext.com'
elif aprov == 'b':
    prov = '@txt.att.net'
elif aprov == 'c':
    prov = '@tmomail.net'
elif aprov == 'd':
    prov = '@messaging.sprintpcs.com'
elif aprov == 'e':
    prov = '@email.uscc.net'
else:
    print(FA+BD+"Please select one of the listed providers!")

#Writes data to user.txt
wr.write(name+nl+eaddr+nl+epass+nl+phnum+prov+nl)
wr.close()
print(GR+BD+'[Done!]')
