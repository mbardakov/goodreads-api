import pytest
from api import app as myapp

@pytest.fixture()
def app():
    myapp.config.update({
        "TESTING": True,
    })
    yield myapp

@pytest.fixture()
def client(app):
    return app.test_client()

my_id = '150603697'
jessie_id = '84639839'

def test_get_tbr(client):
    response = client.get('/tbr/150603697/')
    assert response.status_code == 200
    assert response.json and response.json['books'] and response.json['next_link']

def test_pages(client):
    response_1 = client.get('/tbr/150603697/')
    response_2 = client.get('/tbr/150603697/?page=2')
    assert response_1.json and response_2.json
    assert response_1.json['books'] != response_2.json['books']

def test_book_by_id(client):
    response = client.get('/book/50702014/')
    assert response.status_code == 200
    assert response.json['book_rating']
    assert response.json['rating_count']
    assert response.json['review_count']
    assert response.json['author_name']
    assert response.json['author_link']
    assert response.json['series_name']
    assert response.json['series_entry']
    assert response.json['series_link']

def test_book_with_title(client):
    response = client.get('/book/50702014-paladin-s-grace/')
    assert response.status_code == 200
    assert response.json['book_rating']
    assert response.json['rating_count']
    assert response.json['review_count']
    assert response.json['author_name']
    assert response.json['author_link']
    assert response.json['series_name']
    assert response.json['series_entry']
    assert response.json['series_link']

def test_book_future_release_date(client):
    response = client.get('/book/217388302-hemlock-silver/')
    assert response.status_code == 200
    assert response.json['book_rating']
    assert response.json['rating_count']
    assert response.json['review_count']
    assert response.json['author_name']
    assert response.json['author_link']

def test_book_not_in_series(client):
    response = client.get('/book/217223450/')
    assert response.status_code == 200
    assert response.json['book_rating']
    assert response.json['rating_count']
    assert response.json['review_count']
    assert response.json['author_name']
    assert response.json['author_link']
    assert not response.json['series_name']
    assert not response.json['series_entry']
    assert not response.json['series_link']

def get_author(client):
    response = client.get('/author/7367300')
    assert response.status_code == 200
    assert response.json['author_id']
    assert response.json['author_name']
    assert response.json['average_rating']
    assert response.json['author_bio']
