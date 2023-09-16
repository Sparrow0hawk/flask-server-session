import pytest

def test_index(client):
    response = client.get("/")
    assert b"<h1>Hello world!</h1>" in response.data

def test_session(client):
    with client.session_transaction() as session:
        session["user"] = "user1"
    response = client.get("/")
    assert b"<h1>Hello user1!</h1>" in response.data