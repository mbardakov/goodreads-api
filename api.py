from flask import Flask, jsonify
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_date():
    return jsonify({'greeting': 'hello'})

if __name__ == '__main__':
    app.run()

# move into another file
tbr = 'https://www.goodreads.com/review/list/150603697?shelf=to-read'
my_id = '150603697'
def get_books(id=my_id, shelf='to-read'):
    url = "https://www.goodreads.com/review/list/{0}?shelf={1}".format(id, shelf)
    r = urlopen(url)
    full_page = BeautifulSoup(r, 'html.parser')
    raw_links = full_page.find_all(href=re.compile("/book/show"))
    links = map(lambda x: x['href'].replace("/book/show/", "") ,raw_links)
    next_link = full_page.find(rel='next')['href'] # return this
    print(next_link)
    for link in links:
        print(link) # return these

get_books()