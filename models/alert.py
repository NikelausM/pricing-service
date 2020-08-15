import logging
import pdb

from typing import Dict, List, Union, Any
from bson.objectid import ObjectId

from models.item import Item
from models.model import Model
from dataclasses import dataclass, field, InitVar

logger = logging.getLogger("pricing-service.models.alert")


@dataclass(eq=False)
class Alert(Model):
    collection: str = field(init=False, default='alerts')
    name: str
    price_limit: float
    item_id: InitVar[Union[str, ObjectId]]
    _id: InitVar[Union[str, ObjectId]] = field(default=None)

    def __post_init__(self, item_id: Union[str, ObjectId], _id: Union[str, ObjectId] = None):
        super().__init__(_id)
        logger.debug(f"item_id: {item_id}")
        logger.debug(f"_id: {_id}")
        self.item_id = ObjectId(item_id)
        self.item = Item.get_by_id(item_id)

    def json(self) -> Dict[str, Any]:
        return {
            '_id': self._id,
            'name': self.name,
            'price_limit': self.price_limit,
            'item_id': self.item_id
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under {self.price_limit:.2f}." +
                  f" Latest price: {self.item.price:.2f}.")

