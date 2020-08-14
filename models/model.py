from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import List, Dict, Union, Any
from bson.objectid import ObjectId

from common.database import Database


class Model(metaclass=ABCMeta):
    collection: str
    _id: ObjectId

    def __init__(self, *args, _id: Union[str, ObjectId] = None):
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
        element = cls.find_one_by('_id', _id)
        return element

    @classmethod
    def all(cls) -> List[Model]:
        elements_from_db = Database.find(cls.collection, {})
        elements = [cls(**elem) for elem in elements_from_db]
        return elements

    @classmethod
    def find_one_by(cls, attribute: str, value: Any) -> Model:
        element = cls(**Database.find_one(cls.collection, {attribute: value}))
        return element

    @classmethod
    def find_many_by(cls, attribute: str, value: Any) -> List[Model]:
        elements = [cls(**elem) for elem
                    in Database.find_one(cls.collection, {attribute: value})]
        return elements
