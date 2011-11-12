#!/bin/bash

for task in bigtask1 bigtask2 bigtask3 bigtask4 bigtask5
do
    # the result of processing this task
    RES=${task}.res

    # if no result exists, yet...
    if [[ ! -f $RES ]]
    then
        # ...try to get a lock for processing this bit.
        # if another process is already running this will (deliberately) fail!
        if ln -s "$RES" "$RES.lock"
        then
            # make sure to clean-up in case something happens:
            # e.g. ^C, kill -SIGTERM, etc. 
            # in particular, make sure to clean-up before the SGE scheduler
            # quits (qdel).
            trap "rm -v $RES $RES.lock; exit 1" ERR INT QUIT TERM USR1 USR2 

            # be verbose about the task at hand
            echo $RES

            # do some fancy processing
            cat <(echo -n "$task with SGE_TASK_ID:${SGE_TASK_ID:-"none"} ") \
                <(echo "on HOST:$(hostname)." ) \
                <(sleep 2) \
                | tee $RES \
            || rm -v $RES $RES.lock

            # do some more processing only if the preceding one succeeded
            if [ -s $RES ]
            then
                # do something 
                echo > /dev/null
            fi

            # remove the lock - that's important...!
            rm "$RES.lock"
        else
            echo >&2 "Failed to lock: $RES"
        fi

    else

        echo "SKIP $RES"
        continue
    fi

done
