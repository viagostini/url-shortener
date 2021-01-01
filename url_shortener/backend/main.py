import pprint
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = {}


class Url(BaseModel):
    url: str


class Shortlink(Url):
    shortlink: int


@app.get("/shortlink/{shortlink}")
def get_full_url(shortlink: int) -> Url:
    global database
    return {"url": database[shortlink]}


@app.post("/shortlink")
def create_shortlink(url: Url) -> Shortlink:
    global database
    shortlink = random.randint(1, 2 ** 32)
    database[shortlink] = url.url
    pprint.pprint(database)
    return {"url": url.url, "shortlink": shortlink}
