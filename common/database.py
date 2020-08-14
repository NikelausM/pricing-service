import pymongo

from typing import Dict


class Database:
    URI = 'mongodb://127.0.0.1/pricing'
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        result = Database.DATABASE[collection].find(query)
        return result

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        result = Database.DATABASE[collection].find_one(query)
        return result

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        result = Database.DATABASE[collection].remove(query)
        return result
