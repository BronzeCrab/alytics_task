from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
import json

logger = get_task_logger(__name__)


@shared_task(bind=True)
def test_func(data):
    logger.info("Start task")
    d = json.loads(data)
    return {'result': d['a'] + d['b']}
