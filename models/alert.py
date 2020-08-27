"""
This module contains the Alert :class:`.Model` class.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""

import logging
import pdb

from typing import Dict, List, Union, Any
from bson.objectid import ObjectId

from models.item import Item
from models.model import Model
from models.user import User
from dataclasses import dataclass, field, InitVar
# from libs.mailgun import Mailgun
from libs.emailer import Email


logger = logging.getLogger("pricing-service.models.alert")


@dataclass(eq=False)
class Alert(Model):
    """
    Class that models an Alert.

    Attributes
    ----------
    collection : str
        The database collection name of the Alert class.
    name : str
        The name of the alert.
    price_limit : float
        The price limit.
    user_email : str
        The email of the user the alert corresponds to.
    item_id : InitVar[Union[str, ObjectId]]
        The id of the alert's corresponding item.
    item : Item
        The alert's corresponding item.
    _id : InitVar[Union[str, ObjectId]]
        The id of the alert.

    """
    collection: str = field(init=False, default='alerts')
    name: str
    price_limit: float
    user_email: str
    item_id: InitVar[Union[str, ObjectId]]
    _id: InitVar[Union[str, ObjectId]] = field(default=None)

    def __post_init__(self, item_id: Union[str, ObjectId], _id: Union[str, ObjectId] = None):
        """
        The post-init processing function.

        Parameters
        ----------
        item_id : InitVar[Union[str, ObjectId]]
            The id of the alert's corresponding item.
        _id : InitVar[Union[str, ObjectId]]
            The id of the alert.

        """
        super().__init__(_id)
        logger.debug(f"item_id: {item_id}")
        logger.debug(f"_id: {_id}")
        self.item_id = ObjectId(item_id)
        self.item = Item.get_by_id(item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self) -> dict:
        """
        Returns the json representation of the alert.

        Returns
        -------
        dict
            The json representation of the alert.

        """
        return {
            '_id': self._id,
            'name': self.name,
            'price_limit': self.price_limit,
            'user_email': self.user_email,
            'item_id': self.item_id
        }

    def load_item_price(self) -> float:
        """
        Returns the current price of the alert's corresponding item.

        Returns
        -------
        float
            The current price of the alert's item.

        """

        return self.item.price  # type: ignore

    def notify_if_price_reached(self):
        """
        Notifies a user via email if a price has reached their desired price.

        """
        if self.item.price < self.price_limit:
            # print(f"Item {self.item} has reached a price under {self.price_limit:.2f}." +
            #       f" Latest price: {self.item.price:.2f}.")
            Email.send_mail(
                email=[self.user_email],
                subject=f"Notification for {self.name}",
                text=f'Your alert for {self.name} has reached a price under {self.price_limit:.2f}.' +
                     f" The latest price is {self.item.price:.2f}." +
                     f" Go to this address to check your item: {self.item.url}",
                html=f'<h>Your alert for {self.name} has reached a price under {self.price_limit:.2f}.</h>' +
                     f"<p>The latest price is {self.item.price:.2f}.</p>" +
                     f"<p>Click <a href=\"{self.item.url}\">here</a> to purchase your item.</p>"
            )
