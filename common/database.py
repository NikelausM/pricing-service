import pymongo
import logging

from typing import Dict

logger = logging.getLogger("pricing-service.common.database")


class Database:
    URI = 'mongodb://127.0.0.1/pricing'
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        logger.debug("db.insert...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"data: {data}")
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        logger.debug("db.find...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = Database.DATABASE[collection].find(query)
        logger.debug(f"result: {result}")
        return result

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        logger.debug("db.find_one...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = Database.DATABASE[collection].find_one(query)
        logger.debug(f"result: {result}")
        return result

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        logger.debug("db.update...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        logger.debug(f"data: {data}")
        logger.debug(f"data: {data}")
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        logger.debug("db.remove...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = Database.DATABASE[collection].remove(query)
        logger.debug(f"result: {result}")
        return result
