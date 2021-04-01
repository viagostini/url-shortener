from pymongo import MongoClient


class Database:
    database = MongoClient("mongodb://database:27017/").url_shortener

    @classmethod
    def get_url(cls, shortlink: str) -> str:
        shortlinks = cls.database.shortlinks
        document = shortlinks.find_one({"shortlink": shortlink})
        return document["url"]

    @classmethod
    def save_shortlink(cls, url: str, shortlink: str) -> None:
        document = {"shortlink": shortlink, "url": url}
        shortlinks = cls.database.shortlinks
        shortlinks.insert_one(document).inserted_id

    @classmethod
    def contains(cls, shortlink: str) -> bool:
        shortlinks = cls.database.shortlinks
        return shortlinks.find_one({"shortlink": shortlink}) is not None
