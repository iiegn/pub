#!/bin/bash
#$-M egon.stemle@unitn.it
#$-m n 
#$-S /bin/bash
#$-N metabatch 
#$-o $HOME/metabatch.$JOB_ID-$TASK_ID.out -j y
#$-l vf=900M
#$-q *@compute-0-*

export OMP_NUM_THREADS=1
. /etc/profile
. $HOME/.bash_profile

cd $HOME
./metabatch.sh

#-l h=compute-0-5|compute-0-6|compute-0-7|compute-0-10
#cf.: http://gridengine.info/page/9

# start with:
# qsub -notify -t 1-20 ./sge_metabatch.sh
# -t 1
# -tc max_running_tasks
#
# http://wikis.sun.com/display/gridengine62u2/How+to+Configure+Array+Task+Dependencies+From+the+Command+Line
# qsub -hold_jid 101 ~/sge/mail.sh

# [ https://wiki.duke.edu/display/SCSC/SGE+Array+Jobs ]
# There are a few environment variables that SGE sets during array tasks: $SGE_TASK_FIRST, $SGE_TASK_LAST, $SGE_STEP_SIZE. So the following script may be useful if you need certain things to happen at the start or end of the job:
#if( $SGE_TASK_ID == $SGE_TASK_FIRST ) then
## do first-task stuff here
#endif
## do normal processing here
#if( $SGE_TASK_ID == $SGE_TASK_LAST ) then
## do last-task stuff here
#endif
