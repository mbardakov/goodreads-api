from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def get_shelf(id, shelf='to-read'):
    url = "https://www.goodreads.com/review/list/{0}?shelf={1}".format(id, shelf)
    r = urlopen(url)
    full_page = BeautifulSoup(r, 'html.parser')
    raw_links = full_page.find_all(href=re.compile("/book/show"))
    links = list(set(map(lambda x: x['href'].replace("/book/show/", ""), raw_links)))
    next_link = full_page.find(rel='next')['href']
    print(next_link)
    for link in links:
        print(link)
    return {'books': links, 'next_link': next_link}
