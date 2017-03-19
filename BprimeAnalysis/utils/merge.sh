#!/bin/bash

declare -a sys=("noSys" "jerUp" "jerDown" "jesUp" "jesDown" "jmrUp" "jmrDown" "jmsUp" "jmsDown")
declare -a cat=("cat0" "cat1")
sysarraylength=${#sys[@]}
catarraylength=${#cat[@]}

for (( i=1; i<${sysarraylength}+1; i++ ))
do
    echo "Starting merge of systematic" ${sys[$i-1]}
    for (( j=1; j<${catarraylength}+1; j++ ))
    do  
        echo "Starting merge of category " ${cat[$j-1]} 
	python ttDMmerge.py split/TT_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/DYQQ_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsQQ_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT100to200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT200to400_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT400to600_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT600to800_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT800to1200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT1200to2500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT2500toInf_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT100to200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT200to400_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT400to600_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT600to800_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT800to1200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT1200to2500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT2500toInf_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT300to500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT500to700_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT700to1000_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT1000to1500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT1500to2000_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT2000toInf_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/TT_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/DYQQ_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsQQ_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT100to200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT200to400_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT400to600_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT600to800_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT800to1200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT1200to2500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/ZJetsHT2500toInf_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT100to200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT200to400_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT400to600_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT600to800_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT800to1200_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT1200to2500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/WJetsHT2500toInf_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT300to500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT500to700_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT700to1000_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT1000to1500_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT1500to2000_singleH_${cat[$j-1]}_${sys[$i-1]}/
	python ttDMmerge.py split/QCDHT2000toInf_singleH_${cat[$j-1]}_${sys[$i-1]}/
	
	if [ "${sys[$i-1]}" == "noSys" ]
	    python ttDMmerge.py split/JetHT_runB_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runC_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runD_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runE_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runF_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runG_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runHv2_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runHv3_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runB_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runC_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runD_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runE_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runF_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runG_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runHv2_singleH_${cat[$j-1]}_${sys[$i-1]}/
	    python ttDMmerge.py split/JetHT_runHv3_singleH_${cat[$j-1]}_${sys[$i-1]}/
	
	echo "merge of category " ${cat[$j-1]} "finished!"
    done
    echo "merge of systematic " ${sys[$i-1]} "finished!"
done