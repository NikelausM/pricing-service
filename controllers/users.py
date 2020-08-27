"""
This module handles the routes corresponding to the :class:`models.user.user.User` model.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""
import logging

from flask import Blueprint, request, session, url_for, render_template, redirect, flash
from werkzeug.wrappers import Response
from models.user import User, UserErrors
from models.user import requires_login
from typing import Union
from common.utils import Utils

logger = logging.getLogger("pricing-service.controllers.users")

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
                flash(f"Welcome back, {email}!", 'success')
                return redirect(url_for('alerts.index'))
        except UserErrors.UserError as err:
            flash(err.message, 'danger')
            return redirect(url_for('users.login'))

    return render_template('users/login.html')


@user_blueprint.route('/edit', methods=['GET', 'POST'])
@requires_login
def edit() -> Union[str, Response]:
    """
    Handles the RESTful NEW (GET method) and CREATE (POST method) routes.

    Returns
    -------
    str
        The Alerts INDEX template if POST method, Alerts INDEX template otherwise.

    Raises
    ------
    UserErrors.UserError
        If the user couldn't be created.

    """
    email = session['email']
    user = User.find_by_email(email)

    if request.method == 'POST':
        logger.info(f"request.form: {request.form}")
        email = request.form['email']
        current_password = request.form['current-password']
        new_password = request.form['new-password']

        try:
            if User.is_login_valid(email, current_password):
                user.password = Utils.hash_password(new_password)
                user.save_to_mongo()
                flash(f"Profile edited, {user.email}", 'success')
                return redirect(url_for('alerts.index'))

        except UserErrors.UserError as err:
            flash(err.message, 'danger')
            return redirect(url_for('.edit'))

    return render_template('users/edit.html', user=user)


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
