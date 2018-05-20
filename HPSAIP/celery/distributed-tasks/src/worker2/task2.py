# -*- coding: utf-8 -*-

import os, subprocess
from celery import Celery
from kombu.common import Broadcast

app = Celery('DTQDemo', broker='amqp://rabbitmq')
app.conf.task_queues = (Broadcast('BroadcastTask'),)
app.conf.task_routes = {'my.t2': {'queue': 'BroadcastTask'}}

@app.task(name="my.t2")
def task_func():
    cwd = os.path.dirname(os.path.realpath(__file__))
    cmd = os.path.join(cwd, "task2.sh")
    print("worker2.task_func() start: run command %s" % cmd)
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()
    retcode = proc.returncode
    print("worker2.task_func() finish: [%d]" % retcode)
    return retcode

	
