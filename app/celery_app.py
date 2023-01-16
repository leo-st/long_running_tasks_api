import os
from celery import Celery

CELERY_BROKER_URL = 'redis://redis:6379/0',
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

kwargs = {'CELERY_TRACK_STARTED': True,
'CELERY_TASK_RESULT_EXPIRES': 3600*24}

celery.conf.update(**kwargs)

from services.calculation_service import waiting_function

@celery.task(name='tasks.extraction')
def extraction():
    return waiting_function()