import re
import random
import string

from passlib.hash import pbkdf2_sha512


class Utils:
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_address_matcher = re.compile(r"^[\w-]+@([\w-]+\.)+[\w]+$")
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def random_string_generator(str_size=30,
                                allowed_chars=string.ascii_letters + string.punctuation):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))

    @staticmethod
    def hash_password(password: str) -> str:
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password: str, hashed_password: str) -> bool:
        return pbkdf2_sha512.verify(password, hashed_password)
