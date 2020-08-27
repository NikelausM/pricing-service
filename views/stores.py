"""
This module handles the routes corresponding to the :class:`models.store.Store` model.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.

"""
import json
import logging

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.wrappers import Response
from typing import Union
from models.store import Store
from models.user import requires_login, requires_admin

logger = logging.getLogger("pricing-service.views.stores")

store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index() -> Union[str, Response]:
    """
    Handles the RESTful INDEX route.

    Returns
    -------
    str
        The INDEX template.
    """
    stores = Store.all()
    return render_template('stores/index.html', stores=stores)


@store_blueprint.route('/new', methods=['GET', 'POST'])
@requires_admin
def new() -> Union[str, Response]:
    """
    Handles the RESTful NEW (GET method) and CREATE (POST method) routes.

    Returns
    -------
    str
        The INDEX template if POST method, NEW template otherwise.
    """
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        store = Store(name, url_prefix, tag_name, query)
        logger.debug(f"store: {store}")
        store.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/new.html')


@store_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST'])
@requires_admin
def edit(store_id: str) -> Union[str, Response]:
    """
    Handles the RESTful EDIT (GET method) and UPDATE (POST method) routes.

    Parameters
    ----------
    store_id : str
        The :class:`models.store.Store` id

    Returns
    -------
    str
        The INDEX template if POST method, EDIT template otherwise.
    """
    store = Store.get_by_id(store_id)

    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        store.name = name
        store.url_prefix = url_prefix
        store.tag_name = tag_name
        store.query = query
        logger.debug(f"store: {store}")

        store.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/edit.html', store=store)


@store_blueprint.route('/delete/<string:store_id>')
@requires_admin
def delete(store_id: str) -> Union[str, Response]:
    """
    Handles the RESTful DESTROY route.

    Parameters
    ----------
    store_id : str
        The :class:`models.store.Store` id

    Returns
    -------
    str
        The INDEX template.
    """
    store = Store.get_by_id(store_id)
    logger.debug(f"deleting store: {store}")
    store.remove_from_mongo()
    return redirect(url_for('.index'))
