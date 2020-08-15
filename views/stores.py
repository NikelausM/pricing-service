import json
import logging

from flask import Blueprint, render_template, request, url_for

from models.store import Store

logger = logging.getLogger("pricing-service.views.stores")

store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
    stores = Store.all()
    return render_template('stores/index.html', stores=stores)


@store_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        store = Store(name, url_prefix, tag_name, query)
        logger.debug(f"store: {store}")
        store.save_to_mongo()

    return render_template('stores/new.html')
