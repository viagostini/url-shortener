from __future__ import annotations

import secrets
import string

from pydantic import BaseModel

from url_shortener.backend.database import Database

BASE_SHORTLINK_URL = "localhost:8000/"


class Url(BaseModel):
    url: str


class Shortlink(Url):
    shortlink: str

    @classmethod
    def create_new(self, url: str) -> Shortlink:
        shortlink = self._random_shortlink()
        while Database.contains(shortlink):
            shortlink = self._random_shortlink()
        Database.save_shortlink(url, shortlink)
        return Shortlink(url=url, shortlink=BASE_SHORTLINK_URL + shortlink)

    def _random_shortlink(length: int = 7) -> str:
        characters = string.ascii_letters + string.digits
        return "".join(secrets.choice(characters) for _ in range(length))
