from typing import Dict


class Database:
    database: Dict[str, str] = {}

    @classmethod
    def get_url(cls, shortlink: str) -> str:
        return cls.database[shortlink]

    @classmethod
    def save_shortlink(cls, url: str, shortlink: str) -> None:
        cls.database[shortlink] = url
        print(cls.database)

    @classmethod
    def contains(cls, shortlink: str) -> bool:
        return shortlink in cls.database
