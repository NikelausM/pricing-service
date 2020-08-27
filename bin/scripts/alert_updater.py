"""
This module runs using CRON jobs to periodically notify users by email 
if alert item price is within desired user range.

Attributes
----------
logger : logging.Logger
    The logger used to log information of module.
alerts : List[Alert]
    The list of alerts to be checked for price changes.
"""

import logging

from models.alert import Alert
from dotenv import load_dotenv
from common.database import Database
from typing import List

load_dotenv()

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s" +
    " [%(filename)s:%(lineno)d]" +
    " %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename="logs.txt"
)

logger = logging.getLogger("pricing-service.alert_updater")

Database.initialize()

logger.debug("Sending alerts...")

alerts = Alert.all()

for alert in alerts:
    logger.debug("Email sent.")
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")
