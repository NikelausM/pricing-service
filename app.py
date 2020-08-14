import json

from flask import Flask, render_template, request
from views.items import item_blueprint

from models.item import Item

app = Flask(__name__)

app.register_blueprint(item_blueprint, url_prefix='/items')

if __name__ == '__main__':
    app.run(debug=True)
