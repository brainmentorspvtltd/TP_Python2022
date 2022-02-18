import random
from datetime import datetime as dt
import os, glob
import bs4
import urllib.request as url

def greet(greetIntent):
    cpu = random.choice(greetIntent)
    print(cpu.title())

def showDate():
    date = dt.now().date()
    print("Date is", date.strftime("%d %b, %Y, %a"))

def showTime():
    time = dt.now().time()
    print("Time is", time.strftime("%I:%M:%S, %p"))

def playMusic():
    songs_dir = r"D:\Trainings\Songs"
    os.chdir(songs_dir)
    songs = glob.glob("*.mp3")
    random_song = random.choice(songs)
    print("Playing :", random_song)
    os.startfile(random_song)

def showNews():
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
    path = path + category

    response = url.urlopen(path)
    html = bs4.BeautifulSoup(response, 'lxml')
    newsList = html.find('ul', class_='itg-listing')
    newsData = newsList.findAll('li')
    for item in newsData:
        print(item.text)
        print("*" * 40)