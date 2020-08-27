"""
Module that contains database interaction logic.

This module allows for interaction with a database, and can be run by itself.
All database URL generic syntax components are assumed to be stored as environment
variables at runtime. For more information about URL generic syntax
see `WIKI Docs <https://en.wikipedia.org/wiki/URI>`_

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""
import typing
import pymongo
import logging
import json
import os

from urllib.parse import quote
from dotenv import load_dotenv  # type: ignore

logger = logging.getLogger("pricing-service.common.database")

load_dotenv()


class Database:
    """
    Class that interacts with database.

    This class provides further abstraction to a database object that performs database
    level operations.

    Attributes
    ----------
    SCHEME : str
        Component of the **URI** that specifies the protocol.
    SCHEME_POST_FIX : str
        Optional postfix of the **SCHEME**.
    DB_USERNAME : str
        Part of the **USER_INFO**, specifying the database user username.
    DB_PASSWORD : str
        Part of the **USER_INFO**, specifying the database user password.
    USER_INFO : str
        Subcomponent of **AUTHORITY** that consists of username and password
        preceded by a colon :code:`:`.
    BASE_HOST_NAME : str
        Part of **HOST** that is proceded by a
        forward slash :code:`/' and the database name, **DB_NAME**.
    DB_NAME : str
        Part of **HOST** that specifies the name of the database to connect to.
    HOST : str
        Subcomponent of **AUTHORITY** that consists of the **BASE_HOST_NAME***
        and the **DB_NAME**.
    PORT : str
        Optional subcomponent of **AUTHORITY** preceded by a colon :code:`:`.
    AUTHORITY : str
        Component of **URI** preceded by two forward slashes :code:`//`.
    CONNECTION_OPTIONS : str
        Component of **URI** that specifies the behavior of the client.
    URI : str
        Uniform Resource Identifier for connecting to the database.
    DATABASE : pymongo.database.Database
        The database object that performs database level operations.

    """
    # URI = 'mongodb://127.0.0.1/pricing'
    SCHEME: str = os.environ['DB_SCHEME']
    SCHEME_POST_FIX: str = os.environ['DB_SCHEME_POST_FIX']
    DB_USERNAME: str = os.environ['DB_USERNAME']
    DB_PASSWORD: str = os.environ['DB_PASSWORD']
    USER_INFO: str = f'{DB_USERNAME}:{quote(DB_PASSWORD)}'
    BASE_HOST_NAME: str = os.environ['DB_BASE_HOST_NAME']
    DB_NAME: str = os.environ['DB_NAME']
    HOST: str = f'{BASE_HOST_NAME}/{DB_NAME}'
    PORT: str = os.environ['DB_PORT']
    AUTHORITY: str = f'{USER_INFO}@{HOST}:{PORT}' if PORT else f'{USER_INFO}@{HOST}'
    CONNECTION_OPTIONS: str = os.environ['DB_CONNECTION_OPTIONS']
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
    def insert(cls, collection: str, data: dict) -> None:
        """
        Insert document into a database collection.

        Parameters
        ----------
        collection : str
            The collection for document to be inserted into.
        data : dict
            The document to be inserted into the collection.

        """
        logger.debug("db.insert...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"data: {data}")
        cls.DATABASE[collection].insert(data)

    @classmethod
    def find(cls, collection: str, query: dict) -> pymongo.cursor.Cursor:
        """
        Filters a collection with a query to find all matching documents.

        Parameters
        ----------
        collection : str
            The collection to be queried.
        query : dict
            The query to filter the collection with.

        Returns
        -------
        pymongo.cursor.Cursor
            The cursor corresponding to the query.

        """
        logger.debug("db.find...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = cls.DATABASE[collection].find(query)
        logger.debug(f"result: {result}")
        return result

    @classmethod
    def find_one(cls, collection: str, query: dict) -> pymongo.cursor.Cursor:
        """
        Filters a collection with a query to find matching a document.

        Parameters
        ----------
        collection : str
            The collection to be queried.
        query : dict
            The query to filter the collection with.

        Returns
        -------
        pymongo.cursor.Cursor
            Cursor corresponding to the query.

        """
        logger.debug("db.find_one...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = cls.DATABASE[collection].find_one(query)
        logger.debug(f"result: {result}")
        return result

    @classmethod
    def update(cls, collection: str, query: dict, data: dict) -> None:
        """
        Filters a collection with a query to update a matching document.

        Parameters
        ----------
        collection : str
            The collection to be queried.
        query : dict
            The query to filter the collection with.
        data : dict
            The document to be updated.

        """

        logger.debug("db.update...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        logger.debug(f"data: {data}")
        logger.debug(f"data: {data}")
        cls.DATABASE[collection].update(query, data, upsert=True)

    @classmethod
    def remove(cls, collection: str, query: dict) -> dict:
        """
        Filters a collection with a query to remove a matching document.

        Parameters
        ----------
        collection : str
            The collection to be queried.
        query : dict
            The query to filter the collection with.

        Returns
        -------
        pymongo.cursor.Cursor
            Cursor corresponding to the query.

        """
        logger.debug("db.remove...")
        logger.debug(f"collection: {collection}")
        logger.debug(f"query: {query}")
        result = cls.DATABASE[collection].remove(query)
        logger.debug(f"result: {result}")
        return result
