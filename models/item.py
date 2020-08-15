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
    collection: str = field(init=False, default='items')
    url: str
    tag_name: str
    query: Dict[str, Any]
    price: float = field(default=None)

    _id: InitVar[Union[str, ObjectId]] = field(default=None)

    def __post_init__(self, _id: Union[str, ObjectId] = None):
        super().__init__(_id)

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d+\.\d+)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)

        return self.price

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'url': self.url,
            'tag_name': self.tag_name,
            'price': self.price,
            'query': self.query
        }
