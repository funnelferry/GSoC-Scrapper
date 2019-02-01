import requests
from bs4 import BeautifulSoup

url = 'https://summerofcode.withgoogle.com/archive/2018/organizations/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.select('section div ul li')

for row in rows:

    

    abc = 'https://summerofcode.withgoogle.com' + row.select_one('a')['href']


    print(abc)
    

