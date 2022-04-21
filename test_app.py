import pytest

from dist.app import app

@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    response = client.get('/home')
    assert response.status_code == 302
    print('test_redirect')


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h2>Winc Academy!</h2>' in response.data
    print('test_index')


def test_about(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'<h2>Contact me:</h2>' in response.data
    print('test_contact')
