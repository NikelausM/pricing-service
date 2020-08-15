import logging

from flask import Flask, render_template, request

from views.alerts import alert_blueprint
from views.stores import store_blueprint

app = Flask(__name__)

app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')

if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s" +
        " [%(filename)s:%(lineno)d]" +
        " %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.DEBUG,
        filename="logs.txt"
    )

    logger = logging.getLogger("pricing-service")

    app.run(debug=True, port=5000)
