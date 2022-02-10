import bs4
import urllib.request as url

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

