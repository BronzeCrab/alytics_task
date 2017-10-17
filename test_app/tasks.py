from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from .models import DataSet

logger = get_task_logger(__name__)


@shared_task()
def test_func(dataset_id):
    logger.info("Start task")
    dataset = DataSet.objects.get(id=dataset_id)
    try:
        result = dataset.a + dataset.b
    except Exception as e:
        dataset.exceptions = e
    else:
        dataset.result = result
        dataset.result_calculated_on = datetime.now()
    dataset.save()
    return {'result': result}
