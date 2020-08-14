from __future__ import annotations

import re
import requests

from bs4 import BeautifulSoup
from typing import Dict, List, Union
from bson.objectid import ObjectId

from common.database import Database
from models.model import Model


class Item(Model):

    collection = 'items'

    def __init__(self, url: str, tag_name: str, query: Dict[str, str], _id: Union[str, ObjectId] = None):
        super().__init__(_id)
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None

    def __repr__(self):
        return f"<Item {self.url}>"

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
            'query': self.query
        }
