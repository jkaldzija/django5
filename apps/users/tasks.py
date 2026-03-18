import logging
import time

from celery import shared_task
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)


@shared_task
def log_total_users():
    total_users = get_user_model().objects.count()
    logger.info("Total users in database: %s", total_users)
    time.sleep(10)
    logger.info("End default")
    return total_users


@shared_task
def long_count_users_sleep_and_recount():
    user_model = get_user_model()
    first_count = user_model.objects.count()
    logger.info("Long task started. First users count: %s", first_count)

    time.sleep(10)

    second_count = user_model.objects.count()
    logger.info("End long")
    return {
        "first_count": first_count,
        "second_count": second_count,
    }
