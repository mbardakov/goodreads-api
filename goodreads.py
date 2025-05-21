from bs4 import BeautifulSoup
from urllib.request import urlopen
from util import parse_num
import re

def get_shelf(id, shelf='to-read', page=1):
    url = "https://www.goodreads.com/review/list/{0}?shelf={1}&page={2}".format(id, shelf, page)
    res = urlopen(url)
    full_page = BeautifulSoup(res, 'html.parser')
    raw_links = full_page.find_all(href=re.compile("/book/show"))
    links = list(set(map(lambda x: x['href'].replace("/book/show/", ""), raw_links)))
    next_link = full_page.find(rel='next')['href']
    return {'books': links, 'next_link': next_link}

def get_book(id):
    url = "https://www.goodreads.com/book/show/{0}".format(id)
    res = urlopen(url)
    full_page = BeautifulSoup(res, 'html.parser')
    book_main_content = full_page.find('div', {'class': 'BookPage__mainContent'})
    book_rating = book_main_content.find('div', {'class': 'RatingStatistics__rating'}).decode_contents()
    rating_count = parse_num(book_main_content.find('span', {'data-testid': 'ratingsCount'}).decode_contents())
    review_count = parse_num(book_main_content.find('span', {'data-testid': 'reviewsCount'}).decode_contents())
    author_name = book_main_content.find('span', {'class': 'ContributorLink__name'}).decode_contents()
    author_link = book_main_content.find('a', {'class': 'ContributorLink'})['href']
    title = book_main_content.find('h1', {'data-testid': 'bookTitle'}).decode_contents()
    series = book_main_content.find('div', {'class': 'BookPageTitleSection__title'}).find('a')
    [series_name, series_entry] = map(lambda x: x.strip(), series.decode_contents().split('<!-- -->'))
    series_link = series['href']
    print(series_name, series_entry, series_link)
    return {
        'book_rating': book_rating,
        'rating_count': rating_count,
        'review_count': review_count,
        'author_name': author_name,
        'author_link': author_link,
        'title': title,
        'series_name': series_name,
        'series_entry': series_entry,
        'series_link': series_link
    }