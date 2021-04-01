from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from url_shortener.backend.database import Database
from url_shortener.backend.models import Shortlink, Url

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://0.0.0.0:8089/",
    "http://localhost:27017",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{shortlink}")
def get_full_url(shortlink: str) -> Url:
    return Url(url=Database.get_url(shortlink))


@app.post("/")
def create_shortlink(url: Url) -> Shortlink:
    shortlink = Shortlink.create_new(url.url)
    return shortlink
