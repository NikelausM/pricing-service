"""
This module handles the routes corresponding to the :class:`models.user.user.User` model.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""
import logging

from flask import Blueprint, request, session, url_for, render_template, redirect
from models.user import User, UserErrors

logger = logging.getLogger("pricing-service.views.users")

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles the RESTful NEW (GET method) and CREATE (POST method) routes.

    Returns
    -------
    str
        The Alerts INDEX template if POST method, Users REGISTER template otherwise.

    Raises
    ------
    UserErrors.UserError
        If the user couldn't be created.

    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            logger.debug(f"Created user: {User}")
            session['email'] = email
            return redirect(url_for('alerts.index'))
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles the Log in route.

    Returns
    -------
    str
        The Users LOGIN template if POST method, Alerts INDEX template otherwise.

    Raises
    ------
    UserErrors.UserError
        If the user couldn't be created.

    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('alerts.index'))
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.html')


@user_blueprint.route('/logout')
def logout():
    """
    Handles the Log out route.

    Returns
    -------
    Response
        Redirects to the login route.

    """
    session['email'] = None
    return redirect('login')
