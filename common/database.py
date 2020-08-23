import pymongo
import logging
import json
import os

from typing import Dict
from urllib.parse import quote
from dotenv import load_dotenv  # type: ignore

logger = logging.getLogger("pricing-service.common.database")

load_dotenv()


class Database:
    # URI = 'mongodb://127.0.0.1/pricing'
    DB_USERNAME: str = os.environ['DB_USERNAME']
    DB_PASSWORD: str = os.environ['DB_PASSWORD']
    USER_INFO: str = f'{DB_USERNAME}:{quote(DB_PASSWORD)}'
    BASE_HOST_NAME: str = os.environ['DB_BASE_HOST_NAME']
    DB_NAME: str = os.environ['DB_NAME']
    HOST: str = f'{BASE_HOST_NAME}/{DB_NAME}'
    PORT: str = os.environ['PORT']
    AUTHORITY: str = f'{USER_INFO}@{HOST}:{PORT}' if PORT else f'{USER_INFO}@{HOST}'
    SCHEME: str = os.environ['SCHEME']
    SCHEME_POST_FIX: str = os.environ['SCHEME_POST_FIX']
    CONNECTION_OPTIONS: str = os.environ['CONNECTION_OPTIONS']
    URI: str = f'{SCHEME}{SCHEME_POST_FIX}://{AUTHORITY}?{CONNECTION_OPTIONS}'
    DATABASE: pymongo.database.Database

    @classmethod
    def initialize(cls):
        try:
            print(f"PORT: {cls.PORT}")
            client = pymongo.MongoClient(
                Database.URI)
            cls.DATABASE = client.get_database()
            client.server_info()
        except pymongo.errors.PyMongoError as err:
            raise err
        except Exception as err:
            raise err
        else:
            print("Successfully connected to database.")

    @classmethod
    def insert(cls, collection: str, data: Dict) -> None:
        logger.debug("db.insert...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"data: {data}")
        cls.DATABASE[collection].insert(data)

    @classmethod
    def find(cls, collection: str, query: Dict) -> pymongo.cursor:
        logger.debug("db.find...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = cls.DATABASE[collection].find(query)
        logger.debug(f"result: {result}")
        return result

    @classmethod
    def find_one(cls, collection: str, query: Dict) -> Dict:
        logger.debug("db.find_one...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = cls.DATABASE[collection].find_one(query)
        logger.debug(f"result: {result}")
        return result

    @classmethod
    def update(cls, collection: str, query: Dict, data: Dict) -> None:
        logger.debug("db.update...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        logger.debug(f"data: {data}")
        logger.debug(f"data: {data}")
        cls.DATABASE[collection].update(query, data, upsert=True)

    @classmethod
    def remove(cls, collection: str, query: Dict) -> Dict:
        logger.debug("db.remove...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = cls.DATABASE[collection].remove(query)
        logger.debug(f"result: {result}")
        return result
