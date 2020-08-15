import functools

from typing import Callable
from flask import session, flash, redirect, url_for


def requires_login(f: Callable) -> Callable:
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash("You need to be signed in for this page.", 'danger')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function
