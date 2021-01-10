from fastapi.testclient import TestClient

from url_shortener.backend.database import Database
from url_shortener.backend.main import app

client = TestClient(app)


def test_create_shortlink():
    response = client.post("/", json={"url": "testurl.com"})
    response_json = response.json()

    assert response.status_code == 200
    assert "url" in response_json
    assert "shortlink" in response_json
    assert response_json["url"] == "testurl.com"

    # not the most safe test
    shortlink = response_json["shortlink"].split("/")[-1]
    assert len(shortlink) == 7
    assert shortlink.isalnum()
    print(response_json["shortlink"])
    # hacky check for insertion for now
    assert Database.get_url(shortlink) == "testurl.com"


def test_get_full_url():
    # hacky insert to database for now
    Database.save_shortlink("testurl.com", "1234567")

    response = client.get("/1234567")
    assert response.status_code == 200
    assert response.json() == {"url": "testurl.com"}
