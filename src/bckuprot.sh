#!/bin/bash

function bckuprot() {
    if (( $day <= 7 ))
    then
        wrot=0
        lw=3
    elif (( $day <= 14 ))
    then
        wrot=1
        lw=0
    elif (( $day <= 21 ))
    then
        wrot=2
        lw=1
    else
        wrot=3
        lw=2
    fi

    mrot=$( expr $month % 3 )

    if [[ $month == "1" && $day == "1" ]]
    then
        dest=$(expr $year - 1 )
    elif [[ $day == "1" ]]
    then
        dest=MONTH$mrot
    else
        dest=WEEK$wrot
    fi

    ldest=WEEK$lw
}

for month in $(seq -w 1 12 )
do
    for day in $(seq -w 1 31)
    do
        d=$(date -d "${month}/${day}/2010" "+%d" 2>/dev/null)
        if (( $? )); then break; fi
        day=${d#0}
        m=$(date -d "${month}/${day}/2010" "+%m")
        month=${m#0}
        year=$(date -d "${month}/${day}/2010" "+%Y" )

        bckuprot
        echo $dest $ldest
    done
done

