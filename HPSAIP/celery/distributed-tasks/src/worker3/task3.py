# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('DTQDemo', broker='amqp://rabbitmq')

# inspect worker | task
from celery.task.control import inspect
i = inspect()
i.active()      # active workers
i.active_queues()   # active queues
i.registered_tasks()

app.conf.update(
    task_routes = {
        'mytask1': {'queue': 'Queue1'},
        'mytask2': {'queue': 'Queue2'},
    },
)

#app.send_task('mytask1')
app.send_task('mytask1', queue='Queue1')
#app.send_task('mytask2')
app.send_task('mytask2', queue='Queue2')

