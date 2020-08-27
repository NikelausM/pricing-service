"""
This module contains decorator functions used as middleware in the Flask application.


"""

import functools

from typing import Callable
from flask import session, flash, redirect, url_for, current_app
from werkzeug.wrappers import Response
from typing import Union, Any


def requires_login(f: Callable) -> Union[Callable, Response]:
    """
    Returns the passed function only if login is verified.

    Parameters
    ----------
    f : Callable
        The function to be returned.

    Returns
    -------
    Union[Callable, Response]
        The function returned.

    """
    @functools.wraps(f)
    def decorated_function(*args: Any, **kwargs: Any) -> Union[Callable, Response]:
        """
        Verifies if the user is logged in using the parameters to the returned function.

        Parameters
        ----------
        args : Any
            The positional arguments, if any.
        kwargs : Any
            The keyword arguments, if any.

        Returns
        -------
        Union[Callable, Response]
            The function to be returned if login is verified.

        """
        if not session.get('email'):
            flash("You need to be signed in for this page.", 'danger')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f: Callable) -> Union[Callable, Response]:
    """
    Returns the passed function only if the
    Admin is the logged in user.

    Parameters
    ----------
    f : Callable
        The function to be returned.

    Returns
    -------
    Union[Callable, Response]
        The function returned.

    """
    @functools.wraps(f)
    def decorated_function(*args: Any, **kwargs: Any) -> Union[Callable, Response]:
        """
        Verifies if the logged in user is the Admin
        using the parameters to the returned function.

        Parameters
        ----------
        args : Any
            The positional arguments, if any.
        kwargs : Any
            The keyword arguments, if any.

        Returns
        -------
        Union[Callable, Response]
            The function to be returned if login is verified.

        """
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash("You need to be an administrator to access this page.", 'danger')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function
