"""
This module contains the Model model class.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""

from __future__ import annotations

import logging
import pdb

from abc import ABCMeta, abstractmethod
from typing import List, Dict, Union, Any
from bson.objectid import ObjectId

from common.database import Database

logger = logging.getLogger("pricing-service.models.model")


class Model(metaclass=ABCMeta):
    """
    Class that models a generic model.

    Attributes
    ----------
    collection : str
        The database collection name of the class.
    _id : Union[str, ObjectId]
        The id of the model object.

    """
    collection: str
    _id: Union[str, ObjectId]

    def __init__(self, _id: Union[str, ObjectId] = None):
        """
        Constructs the model object.

        Parameters
        ----------
        _id: Union[str, ObjectId]
            The id of the model.

        """
        logger.debug("Creating model...")
        logger.debug(f"_id: {_id}")
        self._id = ObjectId(_id) or ObjectId()

    def save_to_mongo(self):
        """
        Saves the model to the MongoDB database.
        """
        Database.update(self.collection, {'_id': self._id}, self.json())

    def remove_from_mongo(self):
        """
        Removes the model from the MongoDB database.
        """
        Database.remove(self.collection, {'_id': self._id})

    @abstractmethod
    def json(self) -> dict:
        """
        Returns the json representation of the model.

        Returns
        -------
        dict
            The json representation of the model

        Raises
        ------
        NotImplementedError
            If the method is called without being implemented.
        """
        raise NotImplementedError

    @classmethod
    def get_by_id(cls, _id: Union[str, ObjectId]) -> Model:
        """
        Finds and returns a model by id from the database.

        Parameters
        ----------
        _id : Union[str, ObjectId]
            The id of the model object.

        Returns
        -------
        Model
            The model corresponding to the id.
        """
        element = cls.find_one_by('_id', ObjectId(_id))
        return element

    @classmethod
    def all(cls) -> List[Model]:
        """
        Finds and returns all the models corresponding to the model's collection.

        Returns
        -------
        List[Model]
            The list of all the models of the model's collection.

        """
        logger.debug("all...")
        elements_from_db = Database.find(cls.collection, {})
        logger.debug(f"elements_from_db: {elements_from_db}")

        elements = [cls(**elem) for elem in elements_from_db]
        logger.debug(f"elements: {elements}")
        return elements

    @classmethod
    def find_one_by(cls, attribute: str, value: Union[str, dict]) -> Model:
        """
        Finds and returns the model corresponding to an attribute value query.

        Parameters
        ----------
        attribute : str
            The attribute to query by.
        value : Union[str, dict]
            The value of the attribute to query by.

        Returns
        -------
        Model
            The model corresponding to the query.


        """
        logger.debug("find_one_by...")
        logger.debug(f"collection: {cls.collection}")
        logger.debug(f"attribute: {attribute}")
        logger.debug(f"value: {value}")
        element_from_db = Database.find_one(cls.collection, {attribute: value})
        element = cls(**element_from_db)
        logger.debug(f"element: {element}")
        return element

    @classmethod
    def find_many_by(cls, attribute: str, value: Union[str, dict]) -> List[Model]:
        """
        Finds and returns all the models corresponding to an attribute value query.

        Parameters
        attribute : str
            The attribute to query by.
        value : Union[str, dict]
            The value of the attribute to query by.

        Returns
        -------
        Model
            The list of models corresponding to the query.

        """
        logger.debug("find_many_by...")
        logger.debug(f"collection: {cls.collection}")
        logger.debug(f"attribute: {attribute}")
        logger.debug(f"value: {value}")
        elements = [cls(**elem) for elem
                    in Database.find(cls.collection, {attribute: value})]
        logger.debug(f"elements: {elements}")
        return elements
