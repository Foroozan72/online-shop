from celery import Celery
from celery.utils.log import get_task_logger
import time

app = Celery('one' , broker = 'amqp://guest:guest@localhost:5672' , backend ='rpc://')
logger = get_task_logger(__name__)

app.conf.update(
    task_time_limit = 60 ,
    task_soft_time_limit =50 ,
    worker_concurrency = 70 ,
    worker_prefetch_multiplier = 0 ,
    task_ignore_result = True ,
    task_acks_late = True ,
)


@app.task(bind=True , default_retry_delay=600)        # (name='one.adding')
def devided(self,a,b):
    try:
        return a / b  
    except ZeroDivisionError:
        print('Sorry')
        self.retry(countdown=10 , max_retries = 15)

# @app.task(bind=True)        # (name='one.adding')
# def add(self,a,b):
#     print(self.request)     # time.sleep(15)
#     return a+b

