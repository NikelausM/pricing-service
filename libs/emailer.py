"""
This module contains the logic for sending emails with the python email module.

"""

import os
import smtplib
import logging

from requests import Response, post
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enum import Enum, IntEnum
from typing import List

logger = logging.getLogger("pricing-service.libs.email")


class EmailException(Exception):
    """
    Class that is thrown when there is a Email error.

    Parameters
    ----------
    message : str
        Human readable string describing the exception.

    Attributes
    ----------
    message : str
        Human readable string describing the exception.
    """

    def __init__(self, message: str):
        self.message = message

# Encryption types


class Encryption(Enum):
    """Enumerate email encryption types.
    Specifies the types of email encryption available.
    """
    SSL: str = 'ssl'
    TLS: str = 'tls'

# Email ports
# port 465 for SSL encryption
# port 587 for TLS encryption


class Port(IntEnum):
    """Enumerate port integer numbers for email encryption types."""

    SSL: int = 465
    TLS: int = 587


class Email():
    _ENCRYPTION: str = str(Encryption('tls'))
    _PORT: int = int(Port.TLS)
    _SMTP_SERVER = os.environ['SMTP_SERVER']
    _FROM_EMAIL = os.environ['ADMIN']
    _FROM_PASSWORD = os.environ['ADMIN_EMAIL_PASS']

    FROM_TITLE = 'Pricing service'

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str):
        try:
            message = MIMEMultipart("alternative")
            message["Subject"] = "multipart test"
            message["From"] = f"Pricing Service <{cls._FROM_EMAIL}>"
            message["To"] = ', '.join(email)

            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            message.attach(part1)
            message.attach(part2)

            logger.debug(f"cls._SMTP_SERVER: {cls._SMTP_SERVER}")
            logger.debug(f"cls._PORT: {cls._PORT}")

            with smtplib.SMTP(cls._SMTP_SERVER, cls._PORT) as server:
                server.starttls()  # enable security
                server.login(cls._FROM_EMAIL, cls._FROM_PASSWORD)
                server.sendmail(message["From"], message["To"],
                                message.as_string())

            logger.info("Email sent.")
        except Exception as err:
            raise EmailException("An error occurred while sending e-mail.")
