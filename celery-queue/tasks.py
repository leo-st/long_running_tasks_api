import os
import time
from celery import Celery

import json
import csv

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.extraction')
def extraction():
    start_time = time.time()
    time.sleep(20)
    return "The time required to extract information: " + str(time.time() - start_time) + " seconds"