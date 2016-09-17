#!/bin/bash

#mkdir -p /data/days

LOGNAME=rizhi.log

line_n=`wc -l $LOGNAME | awk '{print $1}'`

n1=1

FILE=1

while [ $n1 -lt $line_n ]
do
	n2=`expr $n1 + 999`
	sed -n "${n1}, ${n2}p" $LOGNAME>file_$FILE.log

	n1=`expr $n2 + 1`
	FILE=`expr $FILE + 1`
done

#缺陷：无法批量分割日志
