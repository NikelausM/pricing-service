"""
This module contains the Item :class:`.Model` class.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""

from __future__ import annotations

import re
import requests
import logging

from bs4 import BeautifulSoup
from typing import Dict, List, Union, Any
from bson.objectid import ObjectId
from dataclasses import dataclass, field, InitVar

from models.model import Model

logger = logging.getLogger("pricing-service.models.item")


@dataclass(eq=False)
class Item(Model):
    """
    Class that models an item.

    Attributes
    ----------
    collection : str
        The database collection name of the Item class.
    url : str
        The `URL <https://en.wikipedia.org/wiki/URL>`_ of the webpage on which the item is found.
    tag_name : str
        The tag for the item.
    query : str
        The `CSS selector <https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Selector>`_
        used to find the item.
    price : float
        The maximum desired price for the item.
    _id : InitVar[Union[str, ObjectId]]
        The id of the item.

    """
    collection: str = field(init=False, default='items')
    url: str
    tag_name: str
    query: Dict[str, Any]
    price: float = field(default=None)

    _id: InitVar[Union[str, ObjectId]] = field(default=None)

    def __post_init__(self, _id: Union[str, ObjectId] = None):
        """
        The post-init processing function.

        Parameters
        ----------
        _id : InitVar[Union[str, ObjectId]]
            The id of the item.

        """
        super().__init__(_id)

    def load_price(self) -> float:
        """
        Requests the items webpage, then parses it for the item price, and returns the price.

        Returns
        -------
        float
            The item price.

        """
        logger.debug("load_price...")
        logger.debug(f"self.url: {self.url}")
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        logger.debug("soup.find(self.tag_name, self.query)....")
        logger.debug(f"self.tag_name: {self.tag_name}")
        logger.debug(f"self.query: {self.query}")
        element = soup.find(self.tag_name, self.query)
        logger.debug(f"element: {element}")

        string_price = element.text.strip()
        logger.debug(f"string_price: {string_price}")

        # pattern = re.compile(r"(\d+,?\d+\.\d+)")
        pattern = re.compile(r"(\d+,?\d*\.*\d+)")
        match = pattern.search(string_price)
        logger.debug(f"match: {match}")
        found_price = match.group(1)  # type: ignore
        logger.debug(f"found_price: {found_price}")
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)

        return self.price

    def json(self) -> dict:
        """
        Returns the json representation of the item.

        Returns
        -------
        str
            The json representation of the item.

        """
        return {
            '_id': self._id,
            'url': self.url,
            'tag_name': self.tag_name,
            'price': self.price,
            'query': self.query
        }
