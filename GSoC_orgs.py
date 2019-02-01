import requests
from bs4 import BeautifulSoup

def get_links():
        url = 'https://summerofcode.withgoogle.com/archive/2018/organizations/'

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')

        rows = soup.select('section div ul li')
        link_list = []

        for row in rows:
                abc = 'https://summerofcode.withgoogle.com' + row.select_one('a')['href']
                link_list.append(abc)
                
        return link_list

def get_org(link_list):       
        for org_url in link_list:
                r = requests.get(org_url)
                soup = BeautifulSoup(r.content, 'html.parser')
                org = soup.find('div', class_="banner__text")
                print("\n",org.h3.text,"\n")
                technologies = soup.find_all('li', class_="organization__tag--technology")
                for technology in technologies:
                        print(technology.text)

links = get_links()
get_org(links)
