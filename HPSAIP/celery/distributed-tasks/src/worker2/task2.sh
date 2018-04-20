#!/bin/bash

CWD=$(cd "$( dirname "$0")"; pwd)
LOG_PATH="$CWD/task2.log"

echo "`date`" > $LOG_PATH

for i in {1..5}; do
    echo $i >> $LOG_PATH
    sleep 1
done

exit 100
