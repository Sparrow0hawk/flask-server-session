import pytest

def test_index(client):
    response = client.get("/")
    assert b"<h1>Hello world!</h1>" in response.data