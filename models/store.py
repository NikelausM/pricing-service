"""
This module contains the Store :class:`.Model` class.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""
from __future__ import annotations

import re
import logging

from typing import Dict, Any, Union
from dataclasses import dataclass, field, InitVar
from bson.objectid import ObjectId

from models.model import Model

logger = logging.getLogger("pricing-service.models.store")


@dataclass(eq=False)
class Store(Model):
    """"
    Class that models a store.

    Attributes
    ----------
    collection : str
        The database collection name of the store class.
    URL_PREFIX_REGEX : str
        The regex expression used to validate a URL prefix.
    name : str
        The store name.
    url_prefix : str
        The store URL prefix.
    tag_name : str
        The store's tag name.
    query : str
        The `CSS selector <https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Selector>`_
        used to find the item.
    _id : InitVar[Union[str, ObjectId]]
        The id of the store.

    """
    collection: str = field(init=False, default='stores')
    URL_PREFIX_REGEX: str = field(init=False, default=r"(^https?:\/\/.+?\/$)")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict[str, Any]
    _id: InitVar[Union[str, ObjectId]] = None

    def __post_init__(self, _id: Union[str, ObjectId] = None):
        """
        The post-init processing function.

        Parameters
        ----------
        _id : InitVar[Union[str, ObjectId]]
            The id of the item.

        """
        super().__init__(_id)
        logger.debug("Creating store...")
        self.url_prefix = self.fix_url_prefix(self.url_prefix)

    def json(self) -> dict:
        """
        Returns the json representation of the store.

        Returns
        -------
        dict
            The json representation of the store.

        """
        return {
            '_id': self._id,
            'name': self.name,
            'url_prefix': self.url_prefix,
            'tag_name': self.tag_name,
            'query': self.query
        }

    @classmethod
    def validate_url_prefix(cls, url: str) -> bool:
        """
        Validates a URL prefix.

        Parameters
        ----------
        url : str
            The url to be validated.

        Returns
        -------
        bool
            True if URL valid, False otherwise.

        """
        logger.debug("validate_url_prefix...")
        logger.debug(f"URL_PREFIX_REGEX: {cls.URL_PREFIX_REGEX}")
        logger.debug(f"url prefix: {url}")
        pattern = re.compile(cls.URL_PREFIX_REGEX)
        match = pattern.search(url)

        if match is None:
            logger.debug("invalid url")
            return False
        else:
            logger.debug("valid url")
            return True

    @classmethod
    def fix_pre_url_prefix(cls, url: str) -> str:
        """
        Tries to fix the pre url prefix.

        Parameters
        ----------
        url : str
            The URL to be fixed.

        Returns
        -------
        str
            The fixed URL if it was fixed,
            otherwise the original URL is returned.

        """
        logger.debug("fix_pre_url_prefix...")
        str_added = "http://"
        url = str_added + url
        if not cls.validate_url_prefix(url):
            url = url[len(str_added):]
        return url

    @classmethod
    def fix_post_url_prefix(cls, url: str) -> str:
        """
        Tries to fix post url prefix.

        Parameters
        ----------
        url : str
            The URL to be fixed.

        Returns
        -------
        str
            The fixed URL if it was fixed,
            otherwise the original URL is returned.

        """
        logger.debug("fix_post_url_prefix...")
        str_added = "/"
        url += str_added
        if not cls.validate_url_prefix(url):
            url = url[:-len(str_added)]
        return url

    @classmethod
    def fix_pre_and_post_url_prefix(cls, url: str) -> str:
        """
        Tries to fix pre and post url prefix.

        Parameters
        ----------
        url : str
            The URL to be fixed.

        Returns
        -------
        str
            The fixed URL if it was fixed,
            otherwise the original URL is returned.

        """
        logger.debug("fix_pre_and_post_url_prefix...")
        pre_str_added = "http://"
        url = pre_str_added + url
        post_str_added = "/"
        url += post_str_added
        if not cls.validate_url_prefix(url):
            url = url[len(pre_str_added):]
            url = url[:-len(post_str_added)]
        return url

    @classmethod
    def fix_url_prefix(cls, url: str) -> str:
        """
        Tries to fix the URL prefix.

        Parameters
        ----------
        url : str
            The URL to be fixed.

        Returns
        -------
        str
            The fixed URL if it was fixed,
            otherwise the original URL is returned.

        Raises
        ------
        ValueError
            If the URL is invalid or unfixable.
        """
        if cls.validate_url_prefix(url):
            return url

        url_fixes = [cls.fix_pre_url_prefix,
                     cls.fix_post_url_prefix,
                     cls.fix_pre_and_post_url_prefix]

        for url_fix in url_fixes:
            new_url = url_fix(url)
            if new_url != url:
                logger.debug(f"new_url: {new_url}")
                return new_url
        raise ValueError(f"URL prefix is invalid/unfixable: {url}")

    @classmethod
    def get_by_name(cls, store_name: str) -> Store:
        """
        Gets a store by name.

        Parameters
        ----------
        store_name : str
            The store name.

        Returns
        -------
        Store
            The store corresponding to the store name provided.

        """
        store = cls.find_one_by('name', store_name)
        return store

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> Store:
        """
        Gets a store by URL prefix.

        Parameters
        ----------
        url_prefix : str
            The store name.

        Returns
        -------
        Store
            The store corresponding to the URL prefix provided.

        """
        url_regex = {"$regex": r"^{}".format(url_prefix)}
        logger.debug(f"url_regex: {url_regex}")
        store = cls.find_one_by('url_prefix', url_regex)
        return store

    @classmethod
    def find_by_url(cls, url: str) -> Store:
        """
        Gets a store by URL.

        Parameters
        ----------
        url_prefix : str
            The store name.

        Returns
        -------
        Store
            The store corresponding to the URL provided.

        """
        pattern = re.compile(r"(https?://.*?/)")
        match = pattern.search(url)
        url_prefix = match.group(1)  # type: ignore
        logger.debug(f"url_prefix: {url_prefix}")
        store = cls.get_by_url_prefix(url_prefix)
        return store
