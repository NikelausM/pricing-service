"""
This module handles the routes corresponding to the :class:`models.alert.Alert` model.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""

import logging
import pdb

from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.wrappers import Response
from models.alert import Alert
from models.store import Store
from models.item import Item
from models.user import requires_login
from typing import Union

logger = logging.getLogger("pricing-service.views.alerts")

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
@requires_login
def index() -> Union[str, Response]:
    """
        Handles the RESTful INDEX route.

        Returns
        -------
        str
            The INDEX template.
        """
    alerts = Alert.find_many_by('user_email', session['email'])
    logger.debug(f"alerts: {alerts}")
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
@requires_login
def new() -> Union[str, Response]:
    """
    Handles the RESTful NEW (GET method) and CREATE (POST method) routes.

    Returns
    -------
    str
        The INDEX template if POST method, NEW template otherwise.
    """
    if request.method == 'POST':
        alert_name = request.form['name']
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        logger.debug(f"item: {item}")
        item.save_to_mongo()

        alert = Alert(alert_name, price_limit,
                      session['email'], item._id)
        logger.debug(f"alert: {alert}")
        alert.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('alerts/new.html')


@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
@requires_login
def edit(alert_id: str) -> Union[str, Response]:
    """
    Handles the RESTful EDIT (GET method) and UPDATE (POST method) routes.

    Parameters
    ----------
    alert_id : str
        The :class:`models.alert.Alert` id

    Returns
    -------
    str
        The INDEX template if POST method, EDIT template otherwise.
    """
    alert = Alert.get_by_id(alert_id)

    if request.method == 'POST':
        price_limit = float(request.form['price_limit'])

        alert.price_limit = price_limit
        alert.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('alerts/edit.html', alert=alert)


@alert_blueprint.route('/delete/<string:alert_id>')
@requires_login
def delete(alert_id: str) -> Union[str, Response]:
    """
    Handles the RESTful DESTROY route.

    Parameters
    ----------
    alert_id : str
        The :class:`models.alert.Alert` id

    Returns
    -------
    str
        The INDEX template.
    """
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session['email']:
        logger.debug(f"deleting alert: {alert}")
        alert.remove_from_mongo()
    return redirect(url_for('.index'))
