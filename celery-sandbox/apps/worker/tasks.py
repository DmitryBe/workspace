import time
import uuid
import json
from celery import Celery
from celery.exceptions import Retry
from celery.signals import task_postrun

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

QS_CELERY_BROKER_URL='redis://192.168.99.100:6379/1'
QS_CELERY_RESULT_BACKEND_URL='redis://192.168.99.100:6379/2'
MAX_RETRY=3

class CError(Exception):
	pass

app = Celery('tasks', broker=QS_CELERY_BROKER_URL, backend=QS_CELERY_RESULT_BACKEND_URL)
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=None
)

@app.task(name='start', bind=True)
def start(self, p1):
	return '0001'

@app.task(name='pull', bind=True)
def pull(self, p1):
	retries = self.request.retries
        logger.info('Task retry: %s' % retries)
        if retries < 3:
                raise self.retry(countdown=3, max_retries=5)
        else:
                return p1 + '--end_pulling'

@app.task(name='task1', max_retries=MAX_RETRY, bind=True)
def task1(self, p1):
	ar = task2.apply_async((p1,), countdown=5)
	print(ar)
	return p1 + 5

@app.task(name='task2', bind=True)
def task2(self, p2):
	return p2 * 10

@app.task(name='task3', bind=True)
def task3(self, p1):
	task4.apply_async((p1,), countdown=5, link=task5.s(p1))

@app.task(name='task4', bind=True)
def task4(self, p1):
	return p1+1

@app.task(name='task5', bind=True)
def task5(self, p1, p2):
	raise CError('test')
	#return p1 * 10

@app.task(name='task7', bind=True)
def task7(self, p1):
	logger.info('--> %s' % p1)
	time.sleep(10)

@app.task(name='task6', bind=True)
def task6(self, p1):
	retries = self.request.retries
	logger.info('Task retry: %s' % retries)
	if retries < 3:
		raise self.retry(countdown=3, max_retries=5)
	else:
		return p1 * 100
