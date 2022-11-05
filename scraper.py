from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
# debug 
# url=("<insert-url>")

url = input("url: " )
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

repos = soup.find_all('a', class_ ='d-inline-block')
for links in repos:
	print("https://github.com" + links.get('href'))
