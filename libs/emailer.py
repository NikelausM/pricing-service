"""
This module contains the logic for sending emails with the python email module.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.
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


class Encryption(Enum):
    """
    Enumerate email encryption types.

    Specifies the types of email encryption available.

    Attributes
    ----------
    SSL : str
        SSl encryption string.
    TLS : str
        TLS encryption string.

    """
    SSL: str = 'ssl'
    TLS: str = 'tls'


class Port(IntEnum):
    """
    Enumerate port integer numbers for email encryption types.

    Attributes
    ----------
    SSL : int
        Port number corresponding to SSL encryption.
    TLS : int
        Port number corresponding to TLS encryption.

    """

    SSL: int = 465
    TLS: int = 587


class Email():
    """
    Class used for sending multipart emails (text and html).

    This class can send emails by combining a text version and an HTML version of an 
    email separately, then merge them with the MIMEMultipart('alternative') instance. 
    This is such that the email has two rendering options, such that in case HTML 
    can't be rendered successfully, the text version can still be rendered.

    Attributes
    ----------
    _ENCRYPTION : str
        The encryption type string.
    _PORT : int
        The port number corresponding to the encryption type.
    _SMTP_SERVER : str
        The SMTP server of the sender email.
    _FROM_EMAIL : str
        The sender email.
    _FROM_PASSWORD : str
        The sender' email password.
    FROM_TITLE : str
        The display name portion of the address.

    """
    _ENCRYPTION: str = str(Encryption('tls'))
    _PORT: int = int(Port.TLS)
    _SMTP_SERVER: str = os.environ['SMTP_SERVER']
    _FROM_EMAIL: str = os.environ['ADMIN']
    _FROM_PASSWORD: str = os.environ['ADMIN_EMAIL_PASS']
    FROM_TITLE: str = 'Pricing Service'

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str):
        """
        Sends the email.

        Parameters
        ----------
        email : List[str]
            The list of email addresses to send the email to.
        subject : str
            The subject of the email message.
        text : str
            The text version of the email message body.
        html : str
            The HTML version of the email message body.

        Raises
        ------
        EmailException
            If there was an error sending the email.

        """
        try:
            message = MIMEMultipart('alternative')
            message["Subject"] = subject
            message["From"] = f"{cls.FROM_TITLE} <{cls._FROM_EMAIL}>"
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
