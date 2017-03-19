#!/bin/bash

declare -a sys=("noSys" "jerUp" "jerDown" "jesUp" "jesDown" "jmrUp" "jmrDown" "jmsUp" "jmsDown")
declare -a cat=("cat0" "cat1")
sysarraylength=${#sys[@]}
catarraylength=${#cat[@]}

for (( i=1; i<${sysarraylength}+1; i++ ))
do
    echo "Starting submit of systematic" ${sys[$i-1]}
    for (( j=1; j<${catarraylength}+1; j++ ))
    do  
        echo "Starting submit of category " ${cat[$j-1]} 
	python BprimeAnalysis.py -C ${cat[$j-1]} --sys ${sys[$i-1]}
       
	echo "Submit of category " ${cat[$j-1]} "finished!"
    done
    echo "Submit of systematic " ${sys[$i-1]} "finished!"
done