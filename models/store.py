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
    collection: str = field(init=False, default='stores')
    URL_PREFIX_REGEX: str = field(init=False, default=r"(^https?:\/\/.+?\/$)")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict[str, Any]
    _id: InitVar[Union[str, ObjectId]] = None

    def __post_init__(self, _id: Union[str, ObjectId] = None):
        super().__init__(_id)
        logger.debug("Creating store...")
        self.url_prefix = self.fix_url_prefix(self.url_prefix)

    def json(self) -> Dict[str: Any]:
        return {
            '_id': self._id,
            'name': self.name,
            'url_prefix': self.url_prefix,
            'tag_name': self.tag_name,
            'query': self.query
        }

    @classmethod
    def validate_url_prefix(cls, url) -> bool:
        logger.debug("validate_url_prefix...")
        logger.debug(f"URL_PREFIX_REGEX: {cls.URL_PREFIX_REGEX}")
        logger.debug(f"url: {url}")
        pattern = re.compile(cls.URL_PREFIX_REGEX)
        match = pattern.search(url)

        if match is None:
            logger.debug("invalid url")
            return False
        else:
            logger.debug("valid url")
            return True

    @classmethod
    def fix_pre_url_prefix(cls, url):
        """Try to fix pre url."""
        logger.debug("fix_pre_url_prefix...")
        str_added = "http://"
        url = str_added + url
        if not cls.validate_url_prefix(url):
            url = url[len(str_added):]
        return url

    @classmethod
    def fix_post_url_prefix(cls, url) -> bool:
        """Try to fix post url."""
        logger.debug("fix_post_url_prefix...")
        str_added = "/"
        url += str_added
        if not cls.validate_url_prefix(url):
            url = url[:-len(str_added)]
        return url

    @classmethod
    def fix_pre_and_post_url_prefix(cls, url) -> bool:
        """Try to fix pre and post url."""
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
    def fix_url_prefix(cls, url) -> str:
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
        store = cls.find_one_by('name', store_name)
        return store

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> Store:
        url_regex = {"$regex": r"^{}".format(url_prefix)}
        logger.debug(f"url_regex: {url_regex}")
        store = cls.find_one_by('url_prefix', url_regex)
        return store

    @classmethod
    def find_by_url(cls, url: str) -> Store:
        pattern = re.compile(r"(https?://.*?/)")
        match = pattern.search(url)
        url_prefix = match.group(1)
        logger.debug(f"url_prefix: {url_prefix}")
        store = cls.get_by_url_prefix(url_prefix)
        return store
