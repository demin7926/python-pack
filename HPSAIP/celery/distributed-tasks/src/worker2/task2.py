# -*- coding: utf-8 -*-

import os, subprocess
from celery import Celery

app = Celery('DTQDemo', backend='redis://redis', broker='redis://redis')

@app.task(name="mytask2")
def task2_func():
    cwd = os.path.dirname(os.path.realpath(__file__))
    cmd = os.path.join(cwd, "task2.sh")
    print("worker2.task_func() start: run command %s" % cmd)
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()
    retcode = proc.returncode
    print("worker2.task_func() finish: [%d]" % retcode)
    return retcode

	
