import logging

from models.alert import Alert
from dotenv import load_dotenv
from common.database import Database

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

alerts: = Alert.all()

for alert in alerts:
    if alert.user_email == "jnickm@gmail.com":
        logger.debug("Email sent.")
        alert.load_item_price()
        alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")
