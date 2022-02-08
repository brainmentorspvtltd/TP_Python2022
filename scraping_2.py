import bs4
import urllib.request as url

path = "https://indianexpress.com/"

print("""
Which Category you want ?
Sports
Entertainment
World
Cities
""")

category = input("Enter Category : ")
path = path+"section/{}".format(category.lower())

response = url.urlopen(path)
html = bs4.BeautifulSoup(response, 'lxml')
newsList = html.findAll('li', {'class' : "swiper-slide"})
for news in newsList:
    print(news.text.strip('\n'))
