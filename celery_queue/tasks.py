
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import time
from celery import Celery

# this is needed so the 'above' modules are visible. Must come before imports
print('==================================================')
print(parentdir)
print('==================================================')

from app.services.calculation_service import long_calculation

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

kwargs = {'CELERY_TRACK_STARTED': True,
'CELERY_TASK_RESULT_EXPIRES': 3600*24}

celery.conf.update(**kwargs)

@celery.task(name='tasks.extraction')
def extraction():
    start_time = time.time()
    time.sleep(20)
    return "The time required to extract information: " + str(time.time() - start_time) + " seconds"

@celery.task(name='tasks.long_calc')
def long_calc():
    return long_calculation()