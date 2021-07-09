from logging import getLogger
from celery import shared_task

logger = getLogger(__name__)


@shared_task
def say_hi():
    logger.debug("Hi DEBUG")
    logger.info("Hi INFO")
    logger.warning("Hi WARNING")


@shared_task
def say_hello():
    logger.debug("Hello DEBUG")
    logger.info("Hello INFO")
    logger.warning("Hello WARNING")
