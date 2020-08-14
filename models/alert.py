from typing import Dict, List, Union
from bson.objectid import ObjectId

from models.item import Item
from common.database import Database
from models.model import Model


class Alert(Model):

    collection = 'alerts'

    def __init__(self, item_id: Union[str, ObjectId], price_limit: float, _id: Union[str, ObjectId] = None):
        super().__init__(_id)
        self.item_id = ObjectId(item_id)
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'price_limit': self.price_limit,
            'item_id': self.item_id
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under {self.price_limit}." +
                  f" Latest price: {self.item.price}.")

