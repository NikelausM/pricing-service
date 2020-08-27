"""
This module contains the logic for sending emails with Mailgun.

"""

import os
from typing import List
from requests import Response, post
from dotenv import load_dotenv

load_dotenv()


class MailgunException(Exception):
    """
    Class that is thrown when there is a Mailgun error.

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


class Mailgun:
    """
    Class that handles the logic of sending emails by using
    the `Mailgun API <https://documentation.mailgun.com/en/latest/quickstart-sending.html#>`_.

    Attributes
    ----------
    MAILGUN_API_KEY : str
        The Mailgun API key.
    MAILGUN_API_KEY : str
        The Mailgun API domain.
    FROM_TITLE : str
        The sender name shown in the email.
    FROM_EMAIL : str
        The sender email.

    """
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', None)
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN', None)

    FROM_TITLE = 'Pricing service'
    FROM_EMAIL = f'do-not-reply@{MAILGUN_DOMAIN}'

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        """
        Sends an email.

        Parameters
        ----------
        email : List[str]
            The list containing the emails of the recipients.
        subject : str
            The subject of the email message.
        text : str
            The text equivalent of the email message body.
        html : str
            The html equivalent of the email message body.

        Returns
        -------
        Response
            The response from the Mailgun API.

        Raises
        ------
        MailgunException
            If either the Mailgun API key or Mailgun domain failed to load.
            It will also be thrown if a bad API response was received from the post request.

        """
        if cls.MAILGUN_API_KEY is None:
            raise MailgunException("Failed to load Mailgun API key.")
        if cls.MAILGUN_DOMAIN is None:
            raise MailgunException("Failed to load Mailgun domain.")
        response = post(
            f'https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages',
            auth=('api', cls.MAILGUN_API_KEY),
            data={'from': f'{cls.FROM_TITLE} <{cls.FROM_EMAIL}>',
                  'to': email,
                  'subject': subject,
                  'text': text,
                  'html': html})
        if response.status_code != 200:
            raise MailgunException("An error occurred while sending e-mail.")
        return response
