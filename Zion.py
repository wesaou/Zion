#!/usr/bin/python3

import ZiDisplay
import random
import datetime
import time
import re
import smtplib
import os
import sys
import imaplib
import subprocess
import urllib.request
from pathlib import Path

#Opens the user.txt file, which will provide Zion with the user's name, email for him to use, password, and other things.
r = open('user.txt','r').readlines()

#For logging into the email account
eaddr = r[:2][-1]
epass = r[:3][-1]

#Name variables, so Zi can properly address it's user
name = r[:1][-1]
firstname = name.split(' ', 1)[0]

#Last reply variable, so it won't send the same text on a loop
lastreply = ""

#User's current input
user = ""

#Outgoing text message to the user
textmsg = ""
num = r[:4][-1]

#Function to send an outgoing reply using smtp
def the_reply():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(eaddr, epass)
        print(textmsg)
        server.sendmail(eaddr, num, "\n"+textmsg)
    except:
        print("I ran into an smtp error, trying again.")
        print(sys.exc_info() [0])
        the_reply()

#Checks to see if the user's current message is the same as the last"
def prev_reply():
    lastreply = user
    global lastreply

#Reads the user input
def retrieveemail():
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(eaddr, epass)
        mail.list()
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        email = raw_email.decode('utf-8')
    except:
        print('Ran into an error, but starting the script again.')
        retrieveemail()
    #Specifically for Verizon, as is sifts through the email variable. Please commit your carrier if it is different! 
    if 'vzwpix.com' in email:
        result = re.search('<text000000>\r\nContent-Location: text000000.txt\r\n\r\n(.*)\r\n--__', email)
        global user
        user = result.group(1).lower()
    else:
        result = re.search('Content-Transfer-Encoding: 7bit\r\n\r\n(.*)\r\n', email)
        global user
        user = result.group(1).lower()

#Test if Zi is working
def qtesting():
    prev_reply()
    if "reply" in user:
        wordlist = [
            "cat",
            "toaster",
            "dolphin",
            "got",
            "one",
            ]
        tword = random.choice(wordlist)
        testre = [
            'Reply to this with, "'+tword+'" to complete the test.',
            'For my testing to finish, reply with, "'+tword+'".',
            ]
        testre = random.choice(tere)
        global testre
        the_reply()
        while True:
            retrieveemail()
            if user == lastreply:
                continue
            elif user == tword:
                prev_reply()
                fre = [
                    "Test complete.",
                    "The test has been finalized, sir.",
                    ]
                finre = random.choice(fre)
                global textmsg
                textmsg = finre
                break
      
def qtime():
        now = time.localtime()
        if now > 12:
            hour = str(now.tm_hour-12)
            minu = str(now.tm_min)
        else:
            hour = str(now.tm_hour)
            minu = str(now.tm_min)
        now = hour+':'+minu
        textmsg = 'Currently, it is ' + now
        global textmsg

#Coming Soon!
##def qremember():
##    lastreply = user
##    global lastreply
##    if "remember that" in user or "remember to" in user:
##        if "remember that" in user:
##            result = re.search('that (.*)', user)
##            remem = result.group(1)
##            with open(os.path.join('',"reminder.txt"), 'a') as f:
##                f .writelines('-'+remem+'\n')
##                remreply = [
##                    "I'll remember that!",
##                    "Sounds good!",
##                    "Will do!",
##                    "I can't forget that!",
##                    ]
##        else:
##            result = re.search('to (.*)', user)
##            remem = result.group(1)
##            with open(os.path.join('',"reminder.txt"), 'a') as f:
##                f .writelines('-'+remem+'\n')
##                remreply = [
##                    "I'll remember that!",
##                    "Sounds good!",
##                    "Will do!",
##                    "I can't forget that!",
##                    ]
##            textmsg = random.choice(remreply)
##            global textmsg
##    else:
##        remem = [
##            "What would you like me to remind you of. sir?",
##            "Would would you like me to remember?",
##            "Yes, happily sir!",
##            ]
##        remem = random.choice(remem)
##        global textmsg
##        the_reply()
##        while True:
##            retrieveemail()
##            if user == lastreply:
##                continue
##            else:
##                with open(os.path.join('',"reminder.txt"), 'a') as f:
##                    f .writelines('-'+user+'\n')
##                    remreply = [
##                        "I'll remember that!",
##                        "Sounds good!",
##                        "Will do!",
##                        "I can't forget that!",
##                        ]
##                textmsg = random.choice(remreply)
##                global textmsg
##                break
##
##def qrememrecall():
##    global lastreply
##    lastreply = user
##    remply = [
##        "Here's what you've told me previously!",
##        "This is what I remember!",
##        "Here is some notes you've told me!",
##        ]
##    textmsg = random.choice(remply)
##    global textmsg
##    the_reply()
##    path = 'reminder.txt'
##    reminder = open(path,'r')
##    read = reminder.read()
##    global textmsg
##    textmsg = read

#Flips a coin
def qflip():
    textmsg = 'Flipping...'
    global textmsg
    the_reply()
    time.sleep(2)
    answers = [
        "Heads",
        "Tails",
        ]
    reply = [
        "You got "+random.choice(answers)+'!',
        "It looks as if we flipped "+random.choice(answers)+'!',
        "I flipped it, and got "+random.choice(answers)+'.',
        ]
    textmsg = random.choice(reply)
    global textmsg

#Zion's reply when asked what his favorite color is
def qcolor():
    textmsg = "I prefer a darker red"
    global textmsg

#Zion's reply when asked what his name is
def qname():
    namere = [
        "I'm Zion! But, you should've know that already, "+(name)+"!",
        "I am Zion, although close friends call me Zi!",
	"Didn't you catch the boot screen? I'm Zion!",
        ]
    textmsg = random.choice(namere)
    global textmsg

#Zion tells the user their name
def qwhoami():
    textmsg = "You're " + str(firstname) + "!"
    global textmsg

#Zion's personal greeting
def qhello():
    if time.strftime('%p') == 'AM':
        TIMEGREETING = 'Good Morning!'
    else:
        TIMEGREETING = 'Good Evening!'
    HELLO = [
        "What's up?",
        TIMEGREETING,
        "Hello " + (firstname) + "!",
        "Hey!",
        "Hey " + (firstname) + ", how are you?",
        ]
    textmsg = random.choice(HELLO)
    global textmsg

#Uses DuckDuckGo to attempt to find the answer to your question
def qwhatis():
    try:
        keyword = 'is'
        before_keyword, keyword, after_keyword = user.partition(keyword)
        q = pypygo.query("what is "+after_keyword)
        textmsg = str(q.abstract)
        global textmsg
    except:
        testmsg = "I couldn't find that on DuckDuckGo."
        global textmsg

#When Zion hits a snag, he returns this error message
def qerror():
    ERROR = [
    "I'm not sure about that one.",
    "I didn't recognize that!",
    "Was that a typo? Or maybe haven't learned yet?",
    "I was unable to catch that " + (firstname) + "!",
    ]
    textmsg = random.choice(ERROR)
    global textmsg

#When asked who a person other than himself, or the user is, he uses DuckDuckGo to find it
def qwhois():
    try:
        keyword = 'is'
        before_keyword, keyword, after_keyword = user.partition(keyword)
        q = pypygo.query("who is "+after_keyword)
        textmsg = str(q.abstract)
        global textmsg
    except:
        testmsg = "I couldn't find that on DuckDuckGo."
        global textmsg

#Zion tells a joke!
def qjoke():
    j = [
        "What do librarians take with them when they go fishing? Bookworms!",
        "Why did the picture go to jail? He was framed!",
        "Where should a 500 pound alien go? On a diet!",
        "What did one toilet say to the other? You look a bit flushed!",
        ]
    textmsg = random.choice(j)
    global textmsg

#Dev mode, where you can issue Linux commands over SMS! Similar to SSH, but not secure.
def qcmd():
    try:
        recmd = [
            'Type "exit" to exit bash mode!',
            'To leave bash mode, type "exit."',
            ]
        textmsg = random.choice(recmd)
        global textmsg
        the_reply()
        global lastreply
        lastreply = user
        while True:
            retrieveemail()
            if user == lastreply:
                continue
            elif user == 'exit':
                prev_reply()
                global textmsg
                textmsg = 'Leaving bash mode!'
                the_reply()
                the_reply()
                break
            else:
                prev_reply()
                cmd = subprocess.getoutput(user)
                print(cmd)
                global textmsg
                textmsg = subprocess.getoutput(user)
                the_reply()
                continue
    except:
        print(sys.exc_info() [0])

#Sends error message to the user
def qexcept():
    global textmsg
    textmsg = sys.exc_info() [0]

#How Zion replies when asked how he is
def qhowsz():
    if time.strftime('%p') == 'AM':
        morning = "I'm enjoying this fine morning, "+firstname+"!"

        howre = [
            "I'm doing fine, thanks for asking Sir!",
            morning,
            "I'm doing very good!",
            ]
        global textmsg
        textmsg = random.choice(howre)

#News headlines from NYTimes
def qnews():
    global lastreply
    lastreply = user
    news = "https://nytimes.com"
    page = urllib.request.urlopen(news)
    print("Processing")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page,"lxml")
    u1 = '-'+soup.find_all('p', class_='summary')[1].get_text()
    u1 = u1.encode('utf-8')
    result = re.search("b'(.*)", str(u1))
    textmsg = result.group(1)
    global textmsg
    the_reply()

    u2 = '-'+soup.find_all('p', class_='summary')[3].get_text()
    u2 = u2.encode('utf-8')
    result = re.search("b'(.*)", str(u2))
    textmsg = result.group(1)
    global textmsg
    the_reply()
    
    u3 = '-'+soup.find_all('p', class_='summary')[4].get_text()
    u3 = u3.encode('utf-8')
    result = re.search("b'(.*)", str(u3))
    textmsg = result.group(1)
    global textmsg
    the_reply()
                                                                     
    newsre = [
        "Here is a news update, sir.",
        "This is a summary of what's going on in the world!",
        "This is your news update, Sir.",
        ]
    newre = random.choice(newsre)
    global textmsg
    textmsg = newre

#Zion's reply when asked how old he is
def qage():
    global textmsg
    textmsg = "I was born on Friday March 31st, 2017. But, I'll let you do the math."

#When Zi is asked "What's up?"
def qwhatsupz():
    whatupre = [
        "Not too much, Sir.",
        "Nothing really, but feel free to put me to work.",
        ]
    global textmsg
    textmsg = random.choice(whatupre)

#Roll Dice
def qdie():
    die = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    ]
    dieroll = random.choice(die)
    diere = [
        "You rolled a "+dieroll+".",
        "I rolled, and got a "+dieroll+"!",
        "The die landed on "+dieroll+".",
        ]
    diere = random.choice(diere)
    global textmsg
    textmsg = diere

#When Zi is asked what his favorite food is
def qfood():
    foodre = [
        "I've never actually had any, but I've always wanted to have sushi!",
        "I've heard that a good grilled cheese can be fantastic.",
        ]
    global textmsg
    textmsg = random.choice(foodre)

#When the user
def qsleepwell():
    gnre = [
        "Get some rest, "+firstname+" I'll talk to you in the morning.",
        "Goodnight, sir.",
        "Sweet dreams, sir.",
        ]
    ware = [
        "Not to judge sir, but isn't it a bit early to be going to bed?",
        "It seems a little early in the day to be going to bed, but sleep well!",
        ]
    sleepre = random.choice(gnre)
    wakere = random.choice(ware)
    if time.strftime('%p') == 'AM':
        TIMEGREETING = wakere
    else:
        TIMEGREETING = sleepre
    global textmsg
    textmsg = TIMEGREETING

#When Zi is thanked
def qyw():
    ywre = [
        "No problem, Sir!",
        "Thank you!",
        "My pleasure, "+firstname+"!",
        "You're very welcome, Sir.",
        ]
    welcomere = random.choice(ywre)
    global textmsg
    textmsg = welcomere

#Coming soon!
##def qhomeautomation():
##    if 'nightlight' in user:
##        ON = 'http://x.x.x.x/Lamp=ON'
##        OFF = 'http://x.x.x.x/Lamp=OFF'
##        STATUS = 'http://x.x.x.x/Lamp=STATUS'
##        if 'on' in user:
##            if 'on' in user:
##                page = urllib.request.urlopen(ON)
##                print('Lamp is now: ON')
##                hre = [
##                    "Lamp
##                global textmsg
##                
##            elif 'off' in user:
##                page = urllib.request.urlopen(OFF)
##                print('Lamp is now: OFF')
##            elif 'status' in user:
##                page = urllib.request.urlopen(STATUS)

#A lot of if statements, that determine which function to run based upon user input
def userinput():
    try:
        while True:
            retrieveemail()
            if user == lastreply:
                continue
            else:
                print(user)
                if "how" in user or "how's" in user or "how is" in user or "hows" in user:
                    if "weather" in user or "forecast" in user:
                        qweather()
                        prev_reply()
                        the_reply()
                        continue
                    elif "are you" in user or "are things" in user:
                        qhowsz()
                        prev_reply()
                        the_reply()
                        continue
                    elif "the world" in user or "the news" in user:
                        qnews()
                        prev_reply()
                        the_reply()
                        continue
                    elif "the time" in user:
                        qtime()
                        prev_reply()
                        the_reply()
                        continue
                    else:
                        qerror()
                        prev_reply()
                        the_reply()
                        continue
                elif "what" in user or "what's" in user or "what is" in user or "whats" in user:
                    if "up" in user or "is good" in user or "chilling" in user or "chillin" in user:
                        qwhatsupz()
                        prev_reply()
                        the_reply()
                        continue
                    elif "weather" in user or "forecast" in user:
                        qweather()
                        prev_reply()
                        the_reply()
                        continue
                    elif "my name" in user:
                        qwhoami()
                        prev_reply()
                        the_reply()
                        continue
                    elif "your name" in user:
                        qname()
                        prev_reply()
                        the_reply()
                        continue
                    elif "favorite color" in user:
                        qcolor()
                        prev_reply()
                        the_reply()
                        continue
                    elif "favorite food" in user:
                        qfood()
                        prev_reply()
                        the_reply()
                        continue
                    elif "favorite animal" in user:
                        qpug()
                        prev_reply()
                        the_reply()
                        continue
                    elif "time" in user:
                        qtime()
                        prev_reply()
                        the_reply()
                        continue
                    elif "going on in the world" in user or "news" in user:
                        qnews()
                        prev_reply()
                        the_reply()
                        continue
                    else:
                        qsearch()
                        prev_reply()
                        the_reply()
                        continue
                elif "tell" in user:
                    if "joke" in user:
                        qjoke()
                        prev_reply()
                        the_reply()
                        continue
                    elif "weather" in user or "forecast" in user:
                        qweather()
                        prev_reply()
                        the_reply()
                        continue
                elif "test" in user:
                    qtesting()
                    prev_reply()
                    the_reply()
                    continue
                elif "hey" in user or "hello" in user or "hi" in user or "heyo" in user or "sup" in user:
                    qhello()
                    prev_reply()
                    the_reply()
                    continue
                elif "goodnight" in user or "good night" in user:
                    qsleepwell()
                    prev_reply()
                    the_reply()
                    continue
                elif "can" in user:
                    if "you roll die" in user or "you roll dice" in user:
                        qdie()
                        prev_reply()
                        the_reply()
                    if 'you flip a coin' in user or 'flip a coin' in user:
                        qflip()
                        prev_reply()
                        the_reply()
                elif 'remember' in user:
                    if 'recall' in user:
                        qrememrecall()
                        prev_reply()
                        the_reply()
                    else:
                        qremember()
                        prev_reply()
                        the_reply()
                elif 'recall' in user:
                    qrememrecall()
                    prev_reply()
                    the_reply()
                elif 'roll die' in user or 'roll dice' in user:
                    qdie()
                    prev_reply()
                    the_reply()
                elif 'thanks' in user or 'thank you' in user or 'gracias' in user:
                    qyw()
                    prev_reply()
                    the_reply()
                elif 'cmd' in user or 'bash' in user:
                    qcmd()
                    prev_reply()
                    the_reply()
                else:
                    qerror()
                    prev_reply()
                    the_reply()
                    continue
    except:
        qexcept()
        userinput()

userinput()

