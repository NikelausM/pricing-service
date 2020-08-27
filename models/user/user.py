"""
This module contains the User :class:`.Model` class.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.
"""

from __future__ import annotations

import logging

from dataclasses import dataclass, field, InitVar
from typing import Dict, Union
from bson.objectid import ObjectId

from models.model import Model
from common.utils import Utils
import models.user.errors as UserErrors

logger = logging.getLogger("pricing-service.models.user.user")


@dataclass
class User(Model):
    """
    Class that models a :class:`.User`.

    Attributes
    ----------
    collection : str
        The database collection name for the class.
    email : str
        The user email.
    password : str
        The user email.
    _id : InitVar[Union[str, ObjectId]]
        The user id.

    """
    collection: str = field(init=False, default='users')
    email: str
    password: str = field(repr=False)
    _id: InitVar[Union[str, ObjectId]] = None

    def __post_init__(self, _id: Union[str, ObjectId] = None):
        """
        The post-init processing function.

        Parameters
        ----------
        _id : InitVar[Union[str, ObjectId]]
            The id of the alert.

        """
        super().__init__(_id)
        logger.debug("Creating store...")

    @classmethod
    def find_by_email(cls, email: str) -> User:
        """
        Finds a :class:`.User` by email.

        Parameters
        ----------
        email : str
            The email to query by.

        Returns
        -------
        User
            The :class:`.User` corresponding to the query.

        Raises
        ------
        UserErrors.UserNotFoundError
            If the :class:`.User` was not found.

        """
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError(
                "A user with this e-mail was not found.")

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        """
        Verifies the email and password provided for a :class:`.User`.

        Parameters
        ----------
        email : str
            The email to be verified.
        password : str
            The password to be verified.

        Returns
        -------
        bool
            True if the email and password is valid, False otherwise.

        Raises
        ------
        UserErrors.IncorrectPasswordError
            If an incorrect password was provided.

        """
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise UserErrors.IncorrectPasswordError(
                'Your password was incorrect')

        return True

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        """
        Registers a :class:`.User`.

        Parameters
        ----------
        email : str
            The email to register with.
        password : str
            The password to register with.

        Returns
        -------
        bool
            True if :class:`.User` was successfully registered, False otherwise.

        Raises
        ------
        UserErrors.InvalidEmailError
            If an invalid email was provided.
        UserErrors.UserAlreadyRegisteredError
            If the :class:`.User` has already been registered.
        UserErrors.UserNotFoundError
            If the :class:`.User` was not found.

        """
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError(
                "The e-mail does nothvae the right format.")
        try:
            user = cls.find_by_email(email)
            logger.debug(f"user already found: {user}")
            raise UserErrors.UserAlreadyRegisteredError(
                "The e-mail you used to register already exists.")
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    def json(self) -> dict:
        """
        Returns the json representation of the :class:`.User`.

        Returns
        -------
        str
            The json representation of the :class:`.User`.

        """
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
