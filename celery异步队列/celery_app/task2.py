import time

from celery_app import app

@app.task
def mutiply(x, y):
    time.sleep(4)
    return x*y
