"""
This module contains :class:`.User` Errors
"""


class UserError(Exception):
    """
    Class that represents a generic :class:`.User` Error.
    """

    def __init__(self, message):
        self.message = message


class UserNotFoundError(UserError):
    """
    Class raised when a :class:`.User` is not found.
    """
    pass


class UserAlreadyRegisteredError(UserError):
    """
    Class raised when a :class:`.User` is already registered.
    """
    pass


class InvalidEmailError(UserError):
    """
    Class raised when an email is invalid.
    """
    pass


class IncorrectPasswordError(UserError):
    """
    Class raised when an incorrect :class:`.User` password is provided.
    """
    pass
