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
    collection: str = field(init=False, default='users')
    email: str
    password: str = field(repr=False)
    _id: InitVar[Union[str, ObjectId]] = None

    def __post_init__(self, _id: Union[str, ObjectId] = None):
        super().__init__(_id)
        logger.debug("Creating store...")

    @classmethod
    def find_by_email(cls, email: str) -> User:
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError("A user with this e-ail was not found.")

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise UserErrors.IncorrectPasswordError('Your password was incorrect')

        return True

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does nothvae the right format.")
        try:
            user = cls.find_by_email(email)
            logger.debug(f"user already found: {user}")
            raise UserErrors.UserAlreadyRegisteredError("The e-mail you used to register already exists.")
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
