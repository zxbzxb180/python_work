import time
from celery import Celery

broker = 'redis://:6222580@127.0.0.1:6379/1'
backend = 'redis://:6222580@127.0.0.1:6379/2'
app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    print('enter call func...')
    time.sleep(4)
    return x + y