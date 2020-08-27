import logging
import os

from flask import Flask, render_template

from controllers.alerts import alert_blueprint
from controllers.stores import store_blueprint
from controllers.users import user_blueprint
from common.utils import Utils
from common.database import Database
from dotenv import load_dotenv  # type: ignore

app = Flask(__name__)
app.secret_key = Utils.random_string_generator()
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

load_dotenv()


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')

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
