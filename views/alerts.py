import logging

from flask import Blueprint, render_template, request
from models.alert import Alert
from models.store import Store
from models.item import Item

logger = logging.getLogger("pricing-service.views.alerts")

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    alerts = Alert.all()
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        alert_name = request.form['name']
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        logger.debug(f"item: {item}")
        item.save_to_mongo()

        alert = Alert(alert_name, price_limit, item._id)
        logger.debug(f"alert: {alert}")
        alert.save_to_mongo()

    return render_template('alerts/new.html')
