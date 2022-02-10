import random
from datetime import datetime as dt
import os, glob
import bs4
import urllib.request as url

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["date", "tell me date", "please tell me date", "what's the date"]
timeIntent = ["time", "tell me time", "please tell me time", "what's the time"]
musicIntent = ["play song", "start song", "play music"]
newsIntent = ["show news", "news", "what's the news"]

chat = True

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        cpu = random.choice(greetIntent)
        print(cpu.title())
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is",date.strftime("%d %b, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is",time.strftime("%I:%M:%S, %p"))

    elif msg in musicIntent:
        songs_dir = r"D:\Trainings\Songs"
        os.chdir(songs_dir)
        songs = glob.glob("*.mp3")
        random_song = random.choice(songs)
        print("Playing :",random_song)
        os.startfile(random_song)

    elif msg in newsIntent:
        path = "https://www.indiatoday.in/"

        response = url.urlopen(path)
        page = bs4.BeautifulSoup(response, 'lxml')
        newsList = page.find('ul', class_='itg-listing')
        newsData = newsList.findAll('li')
        for item in newsData:
            print(item.text)
            print("*" * 40)
            

        print("""
        Which Category you want ?
        Sports
        Elections
        Technology
        """)

        category = input("Enter Category : ")
        category = category.lower()
        path = path+category

        response = url.urlopen(path)
        html = bs4.BeautifulSoup(response, 'lxml')
        newsList = html.find('ul', class_='itg-listing')
        newsData = newsList.findAll('li')
        for item in newsData:
            print(item.text)
            print("*" * 40)


    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
