"""
Module that contains a class with utility functions.

"""

import re
import random
import string

from passlib.hash import pbkdf2_sha512


class Utils:
    """
    Class that provides utility functions.

    """

    @staticmethod
    def email_is_valid(email: str) -> bool:
        """
        Checks if the email has valid email format.

        Parameters
        ----------
        email : str
            The email to be validated.

        Returns
        -------
        bool
            True if email is valid, False otherwise.

        """
        email_address_matcher = re.compile(r"^[\w-]+@([\w-]+\.)+[\w]+$")
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def random_string_generator(str_size=30,
                                allowed_chars=string.ascii_letters
                                + string.punctuation) -> str:
        """
        Generates and returns a random string.

        Parameters
        ----------
        str_size : str
            The size of the string to be generated.
        allowed_chars : str
            The string containing the characters allowed.

        Returns
        -------
        str
            The random string generated.
        """
        return ''.join(random.choice(allowed_chars) for x in range(str_size))

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Encrypts the provided password.

        Parameters
        ----------
        password : str
            The password to be encrypted.

        Returns
        -------
        str
            The encrypted password.

        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password: str, hashed_password: str) -> bool:
        """
        Verifies if the provided password matches the hashed_password.

        Parameters
        ----------
        password : str
            The password provided.
        hashed_password : str
            The password stored.

        Returns
        -------
        bool
            True if passwords match, False otherwise.
        """
        return pbkdf2_sha512.verify(password, hashed_password)
