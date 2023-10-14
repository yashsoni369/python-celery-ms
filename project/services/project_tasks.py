import logging

from vulcan.celery_instance import celery_app

@celery_app.task
def add_t(x, y):
    """
    Adds two numbers.

    This is a dummy test task.
    """
    logging.info("Adding in Project {} + {} with result {}".format(x, y, x + y))
    return x + y
