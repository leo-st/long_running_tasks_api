import os
from celery import Celery


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')


celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

# kwargs = {'CELERY_TRACK_STARTED': True,
# 'CELERY_TASK_RESULT_EXPIRES': 3600}

# celery.conf.update(**kwargs)