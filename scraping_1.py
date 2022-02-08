import bs4
import urllib.request as url

path = "https://indianexpress.com/"
response = url.urlopen(path)

html = bs4.BeautifulSoup(response, 'lxml')
headline = html.find('h1', class_='t-elecblock-heading')
print("Headline ::",headline.text)

topNews = html.find('div', {'class' : 'top-news'})
newsList = topNews.findAll('li')
print("Top News...")
for news in newsList:
    print(news.text)
    print("*" * 50)
