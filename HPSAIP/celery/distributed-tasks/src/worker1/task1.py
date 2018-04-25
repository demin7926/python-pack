# -*- coding: utf-8 -*-

import os, subprocess
from celery import Celery

app = Celery('DTQDemo', broker='amqp://rabbitmq')

#@app.task(name="mytask1")
def task2_func():
    cwd = os.path.dirname(os.path.realpath(__file__))
    cmd = os.path.join(cwd, "task1.sh")
    print("worker1.task_func() start: run command %s" % cmd)
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()
    retcode = proc.returncode
    print("worker1.task_func() finish: [%d]" % retcode)
    return retcode

task2_func = app.task(name="mytask1")(task2_func)


argv = ['worker', '--loglevel=INFO']
app.worker_main(argv)
	
