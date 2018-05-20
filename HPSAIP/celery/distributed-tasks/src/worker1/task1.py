# -*- coding: utf-8 -*-

import os, subprocess
from celery import Celery
from kombu.common import Broadcast

app = Celery('DTQDemo', broker='amqp://rabbitmq')
app.conf.task_queues = (Broadcast('BroadcastTask'),)
app.conf.task_routes = {'my.t1': {'queue': 'BroadcastTask'}}

#@app.task(name="my.t1")
def task_func():
    cwd = os.path.dirname(os.path.realpath(__file__))
    cmd = os.path.join(cwd, "task1.sh")
    print("worker1.task_func() start: run command %s" % cmd)
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()
    retcode = proc.returncode
    print("worker1.task_func() finish: [%d]" % retcode)
    return retcode


task_func = app.task(name="my.t1")(task_func)

argv = ['worker', '--loglevel=INFO']
app.worker_main(argv)
	
