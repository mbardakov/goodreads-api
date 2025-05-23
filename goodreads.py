from bs4 import BeautifulSoup
from urllib.request import urlopen
from util import parse_num
from datetime import datetime
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
    release_date = book_main_content.find('p', {'data-testid': 'publicationInfo'}).decode_contents().replace('Expected publication ', '').replace('First published ', '')
    if (series is not None):
        [series_name, series_entry] = map(lambda x: x.strip(), series.decode_contents().split('<!-- -->'))
        series_link = series['href']
    else:
        [series_name, series_entry, series_link] = [None, None, None]
    return {
        'book_rating': book_rating,
        'rating_count': rating_count,
        'review_count': review_count,
        'author_name': author_name,
        'author_link': author_link,
        'title': title,
        'series_name': series_name,
        'series_entry': series_entry,
        'series_link': series_link,
        'release_date': datetime.strptime(release_date, '%B %d, %Y').strftime('%Y/%m/%d')
    }

def get_author(id):
    author_id = id.split('.')[0]
    url = "https://www.goodreads.com/author/show/{0}".format(id)
    res = urlopen(url)
    full_page = BeautifulSoup(res, 'html.parser')
    author_main_content = full_page.find('div', {'class': 'mainContent'})
    author_name = author_main_content.find('h1', {'class': 'authorName'}).find('span').decode_contents()
    average_rating = author_main_content.find('span', {'class': 'rating'}).find('span', {'class': 'average'}).decode_contents()
    author_bio_html = author_main_content.find('span', {'id': 'freeTextContainerauthor{0}'.format(author_id)}).decode_contents()
    author_bio = re.sub('</?[a-z][a-z0-9]*[^<>]*>|<!--.*?-->', '', author_bio_html)
    return {
        'author_id' : author_id,
        'author_name' : author_name,
        'average_rating' : average_rating,
        'author_bio' : author_bio,
    }

def get_author_books(id, page=1):
    url = "https://www.goodreads.com/author/list/{0}?page={1}&per_page=30".format(id, page)
    res = urlopen(url)
    full_page = BeautifulSoup(res, 'html.parser')
    print(full_page.prettify())
    return {
        'author' : None
    }

print(get_author('7367300'))