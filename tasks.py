"""
@file: tasks.py
@author: rrh
@time: 2020/2/4 8:14 下午
"""

from celery import Celery
import time

# app = Celery('tasks',
#              broker='redis://localhost:6379',
#              backend='redis://localhost:6379'
#              )

app = Celery('tasks',
             broker='amqp://yuruhao:123456@localhost:5672//',
             backend='redis://localhost:6379'
             )


@app.task
def add(x, y):
    time.sleep(60)
    print('running...')
    return x + y
