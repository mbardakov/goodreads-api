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
    print(client)
    response = client.get("/tbr/150603697/")
    assert response.status_code == 200