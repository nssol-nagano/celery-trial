import time

import numpy as np
from celery_app import celery_app


@celery_app.task
def sleep_a_sec():
    time.sleep(5)
    return np.random.rand()
