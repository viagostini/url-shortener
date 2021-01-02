import pprint
import secrets
import string
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:8080", "http://127.0.0.1:8080", "http://0.0.0.0:8089/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database: Dict[str, str] = {}


class Url(BaseModel):
    url: str


class Shortlink(Url):
    shortlink: str


BASE_SHORTLINK_URL = "localhost:8000/"


def random_shortlink(length: int = 7) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


@app.get("/{shortlink}")
def get_full_url(shortlink: str) -> Url:
    global database
    return Url(url=database[shortlink])


@app.post("/")
def create_shortlink(url: Url) -> Shortlink:
    global database
    shortlink = random_shortlink()
    while shortlink in database:
        shortlink = random_shortlink()
    database[shortlink] = url.url
    pprint.pprint(database)
    return Shortlink(url=url.url, shortlink=BASE_SHORTLINK_URL + shortlink)
