import urllib.request as url
import bs4

path = "https://www.marvel.com/"
response = url.urlopen(path)

page = bs4.BeautifulSoup(response, 'lxml') 
images = page.find_all('img')

for i in range(len(images)):
    img_url = images[i]['src']
    print(img_url)
    url.urlretrieve(img_url, 'images/img_{}.jpg'.format(i))

''' To Show Image
from PIL import Image
img = Image.open('images/img_14.jpg')
img.show()
'''
