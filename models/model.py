from __future__ import annotations

import logging
import pdb

from abc import ABCMeta, abstractmethod
from typing import List, Dict, Union, Any
from bson.objectid import ObjectId

from common.database import Database

logger = logging.getLogger("pricing-service.models.model")


class Model(metaclass=ABCMeta):
    collection: str
    _id: Union[str, ObjectId]

    def __init__(self, _id: Union[str, ObjectId] = None):
        logger.debug("Creating model...")
        logger.debug(f"_id: {_id}")
        self._id = ObjectId(_id) or ObjectId()

    def save_to_mongo(self):
        Database.update(self.collection, {'_id': self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {'_id': self._id})

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def get_by_id(cls, _id: Union[str, ObjectId]) -> Model:
        element = cls.find_one_by('_id', ObjectId(_id))
        return element

    @classmethod
    def all(cls) -> List[Model]:
        logger.debug("all...")
        elements_from_db = Database.find(cls.collection, {})
        logger.debug(f"elements_from_db: {elements_from_db}")

        elements = [cls(**elem) for elem in elements_from_db]
        logger.debug(f"elements: {elements}")
        return elements

    @classmethod
    def find_one_by(cls, attribute: str, value: Union[str, Dict]) -> Model:
        logger.debug("find_one_by...")
        logger.debug(f"collection: {cls.collection}")
        logger.debug(f"attribute: {attribute}")
        logger.debug(f"value: {value}")
        element_from_db = Database.find_one(cls.collection, {attribute: value})
        element = cls(**element_from_db)
        logger.debug(f"element: {element}")
        return element

    @classmethod
    def find_many_by(cls, attribute: str, value: Union[str, Dict]) -> List[Model]:
        logger.debug("find_many_by...")
        logger.debug(f"collection: {cls.collection}")
        logger.debug(f"attribute: {attribute}")
        logger.debug(f"value: {value}")
        elements = [cls(**elem) for elem
                    in Database.find(cls.collection, {attribute: value})]
        logger.debug(f"elements: {elements}")
        return elements
