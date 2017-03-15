import os, commands

scratch = False

#cmdls = "gfal-ls "                                                                                                                                           
#cmdcp = "gfal-copy "
#srm = "srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="
#outdir="srm://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/testPerGiulia/"

cmdls = "lcg-ls"
srm = "  -b -D srmv2 srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="
#srm = "  -b -D srmv2 srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="
#srm = " -b -D srmv2 srm://t3se01.psi.ch"
### To store on t3 storage element
cmdcp = "globus-url-copy -continue-on-error -rst -nodcau -fast -vb -v -cd -r gsiftp://storage01.lcg.cscs.ch/"
#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/decosa/ttDM/Moriond_v3/jes/"
#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/JetMet_76X_v7/"

outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/Bprime_80Xv2p4_Mo17v4/Trigger/"#JetMet_80X_v1/"

### To store on t3 scratch area
if(scratch):
    cmdcp = "lcg-cp "
    outdir = "/scratch/grauco/"

samples = {}

####start samples for moriond 17 _ v4

##samples["WJetsHT2500toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172502/0000/"
##samples["WJetsHT1200to2500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172452/0000/"
##samples["WJetsHT800to1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172439/0000/"
##samples["WJetsHT600to800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172429/0000/"
#samples["ZJetsHT2500toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_08Feb17/170211_173016/0000/"
#samples["ZJetsHT1200to2500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_08Feb17/170211_173003/0000/"
#samples["ZJetsHT800to1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/ZJetsToNuNu_HT-800To1200_13TeV-madgraph//Root80xV2p4_ZJetsToNuNu_HT-800To1200_13TeV-madgraph_08Feb17//170211_172951/0000/"
#samples["ZJetsHT600to800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/ZJetsToNuNu_HT-600To800_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-600To800_13TeV-madgraph_08Feb17/170211_172939/0000/"
##samples["WJetsQQ"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172513/0000/"
#samples["DYQQ"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8/Root80xV2p4_DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8_08Feb17/170211_183356/0000/"
#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/Root80xV2p4_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_12F/170211_173501/0000/"

##samples["QCDHT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172624/0001/"
##samples["QCDHT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172634/0000/"
#samples["QCDHT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172645/0000/"
##samples["QCDHT1000to1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172656/0000/"
##samples["QCDHT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172706/0000/"
##samples["QCDHT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12F/170211_172717/0000/"

#samples["JetHTb"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016B-23Sep2016-v3_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_181738/0000/"
#samples["JetHTe"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016E-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175302/0000/"
#samples["JetHTg"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016G-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175332/0000/"
##samples["JetHThv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016H-PromptReco-v3_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175404/0000/"
#samples["JetHTf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016F-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175315/0000/"
#samples["JetHTc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016C-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175235/0000/"
##samples["JetHThv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016H-PromptReco-v2_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175350/0001/"
#samples["JetHTd"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016D-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175249/0000/"

#samples["SingleMub"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_20F/170220_121413/0000/"
#samples["SingleMuc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runC_20F/170220_122003/0000/"
#samples["SingleMud"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runD_20F/170220_122029/0000/"
#samples["SingleMue"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runE_20F/170220_122131/0000/"
#samples["SingleMuf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runF_20F/170220_122249/0000/"
#samples["SingleMug"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runG_20F/170220_122530/0000/"
samples["SingleMuhv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runHv2_20F/170220_122727/0000/"
samples["SingleMuhv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v3/Trigger/SingleMuon/Root80xV2p4_SingleMuon_runHv3_20F/170220_123327/0000/"

#samples["BprimeBToHB800"]=""
#samples["BprimeBToHB1000"]=""
#samples["BprimeBToHB1200"]=""
#samples["BprimeBToHB1400"]=""
#samples["BprimeBToHB1600"]=""
#samples["BprimeBToHB1800"]=""

#***************

#samples["SingleMub"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runB_08F/170208_142816/0000/"
#samples["JetHTc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runC_08F/170208_142712/0000/"
#samples["JetHTd"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runD_08F/170208_142640/0000/"
#samples["JetHTe"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runE_08F/170208_134205/0000/"
#samples["JetHThv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runHv2_08F/170208_140016/0000/"
##samples["JetHTg"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runG_08F/170208_135658/0000/"
#samples["JetHTf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runF_08F/170208_135421/0000/"
#samples["JetHThv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runHv3_08F/170208_140135/0000/"

####start samples for moriond 17 _ v3
#samples["BprimeBToHB800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_04F/170204_065332/0000/"
#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_04F/170204_065342/0000/"
#samples["BprimeBToHB1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_04F/170204_065356/0000/"
#samples["BprimeBToHB1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_04F/170204_065407/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_04F/170204_065419/0000/"
#samples["BprimeBToHB1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_04F/170204_065430/0000/"

#samples["JetHTbv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runB_04F/170204_080622/0001/"
#samples["JetHTc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runC_04F/170204_080708/0001/"
#samples["JetHTd"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runD_04F/170204_080734/0001/"
#samples["JetHTe"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_rune_04F/170204_081041/0000/"
#samples["JetHTf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runF_04F/170204_080946/0001/"
#samples["JetHTg"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runG_04F/170204_081150/0000/"
#samples["JetHThv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runH2_04F/170204_081240/0001/"
#samples["JetHThv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/JetHT/Root80xV2p4_JetHT_runH3_04F/170204_081324/0001/"

#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/Root80xV2p4_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_04F/170204_080218/0000/"

#samples["ZJetsHT600to800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-600To800_13TeV-madgraph_04F/170205_160415/0000/"
#samples["ZJetsHT800to1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-800To1200_13TeV-madgraph_04F/170205_160425/0001/"
#samples["ZJetsHT1200to2500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_04F/170205_160436/0001/"
#samples["ZJetsHT2500toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/Root80xV2p4_ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_04F/170205_160446/0001/"
#samples["WJetsHT600to800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04F/170205_155902/0001/"
#samples["WJetsHT800to1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04F/170205_155917/0001/"
#samples["WJetsHT1200to2500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04F/170205_155932/0001/"
#samples["WJetsHT2500toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04F/170205_160251/0001/"
#samples["WJetsQQ"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04F/170205_160006/0001/"
#samples["DYQQ"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Mo17v1/DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8/Root80xV2p4_DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8_04F/170205_160500/0001/"

#samples["QCDHT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120626/0000/"
#samples["QCDHT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120606/0000/"
#samples["QCDHT1000to1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120553/0000/"

#samples["QCDHT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120534/0001/"
#samples["QCDHT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120517/0001/"
#samples["QCDHT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120454/0004/"

#samples["QCDHT2000toInfext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120759/0000/"
#samples["QCDHT1500to2000ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120747/0000/"
#samples["QCDHT1000to1500ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120553/0000/"
#samples["QCDHT700to1000ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120723/0000/"
#samples["QCDHT500to700ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120711/0000/"
#samples["QCDHT300to500ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Feb17/170204_120659/0000/"




####start samples for moriond 17 _ v2
#samples["SingleMubv1"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jbv1/170120_145831/0000/"
#samples["SingleMubv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jbv3/170120_150018/0000/"
#samples["SingleMuc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jc/170120_150200/0000/"
#samples["SingleMud"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jd/170120_150456/0000/"
#samples["SingleMue"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Je/170120_150612/0000/"
#samples["SingleMuf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jf/170120_153256/0000/"
#samples["SingleMug"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jg/170120_153332/0000/"
#samples["SingleMuhv1"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jhv1/170120_153508/0000/"
#samples["SingleMuhv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jhv2/170120_153539/0000/"
#samples["SingleMuhv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/Trigger/SingleMuon/Root80xV2p4_SingleMuon_13Jhv3/170120_153616/0000/"#

#samples["BprimeBToHB800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170118_180945/0000/"
#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170118_180952/0000/"
#samples["BprimeBToHB1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170118_181007/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170118_181014/0000/"

#samples["JetHTbv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/JetHT/Root80xV2p4_JetHT_13Jbv3/170113_202046/00001/"
#samples["JetHTc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/JetHT/Root80xV2p4_JetHT_13Jc/170113_202110/00001/"
#samples["JetHTe"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/JetHT/Root80xV2p4_JetHT_13Je/170113_202200/00001/"
#samples["JetHTf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/JetHT/Root80xV2p4_JetHT_13Jf/170113_202221/00001/"
#samples["JetHThv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/JetHT/Root80xV2p4_JetHT_13Jhv2/170113_202341/00001/"
#samples["JetHThv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/JetHT/Root80xV2p4_JetHT_13Jhv3/170113_202317/00001/"

#samples["QCDHT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13Jhv2/170115_151330/00001/"
#samples["QCDHT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13Jhv2/170115_151323/00001/"
#samples["QCDHT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170113_201823/00001/"
#samples["QCDHT1000to1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170113_201833/00001/"
#samples["QCDHT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170113_201843/00001/"
#samples["QCDHT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170113_201850/00001/"
#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4_v2/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/Root80xV2p4_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_13J/170113_201907/00001/"

####start samples for moriond 17 _ v1
#samples["BprimeBToHB800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081857/0000/"
#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081913/0000/"
#samples["BprimeBToHB1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081932/0000/"
#samples["BprimeBToHB1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081940/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081949/0000/"
#samples["BprimeBToHB1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_082001/0000/"

#samples["JetHThv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_15Jhv3/170112_095222/0000/"
#samples["JetHTf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_15Jf/170112_095447/0002/"
#samples["JetHTc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_15Jc/170112_095616/0002/"
#samples["JetHTbv3"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_15Jbv3/170112_095705/0002/"
#samples["JetHThv2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_15Jhv2/170112_095247/0002/"
#samples["JetHTe"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_15Je/170112_095508/0002/"

#samples["SingleMubv1"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Jbv1/170110_182114/0000/"
#samples["SingleMubv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Jbv3/170110_182007/0000/"
#samples["SingleMuc"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Jc/170110_181913/0000/"
#samples["SingleMud"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Jd/170110_181450/0000/"
#samples["SingleMue"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Je/170110_181411/0000/"
#samples["SingleMuf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Jf/170110_181308/0000/"
#samples["SingleMug"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13Jg/170110_181232/0000/"
#samples["SingleMuhv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13hv2/170110_180858/0000/"
#samples["SingleMuhv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/SingleMuon/Root80xV2p4_SingleMuon_13hv3/170110_180549/0000/"

#samples["QCDHT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170111_083748/0001/"
#samples["QCDHT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170111_083734/0000/"
#samples["QCDHT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170110_081723/0000/"
#samples["QCDHT1000to1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170110_081745/0000/"
#samples["QCDHT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170110_081753/0000/"
#samples["QCDHT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p4_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_13J/170110_081812/0000/"

#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/Root80xV2p4_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_13Jv1/170110_090645/0001/"

#samples["JetHTbv3"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13Jbv3/170110_092311/0001/"
#samples["JetHTc"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13Jc/170110_092422/0001/"
#samples["JetHTd"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13Jd/170110_093259/0001/"
#samples["JetHTe"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13Je/170110_093339/0001/"
#samples["JetHTf"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13Jf/170110_093408/0001/"
#samples["JetHTg"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13Jg/170110_093450/0001/"
#samples["JetHThv2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13hv2/170110_093534/0001/"
#samples["JetHThv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/JetHT/Root80xV2p4_JetHT_13hv3/170110_093605/0001/"
####end samples for moriond 17 _ v1


#samples["TT_v2"] ="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/Root80xV2p1_TT_TuneCUETP8M1_13TeV-powheg-pythia8_16Nov/161116_195117/0000/"
#samples["BprimeBToHB1000_v2"] = "pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_16Nov/161116_180001/0000/"
#samples["BprimeBToHB800_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_16Nov/161116_175847/0000/"
#samples["BprimeBToHB1200_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_16Nov/161116_180023/0000/"
#samples["BprimeBToHB1400_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_16Nov/161116_180023/0000/"
#samples["BprimeBToHB1600_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_16Nov/161116_180107/0000/"

#samples["BprimeBprime800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_29Nov/161201_101301/0000/"
#samples["BprimeBprime1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBprime_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBprime_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_29Nov/161201_101316/0000/"
#samples["BprimeBprime1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_29Nov/161201_101325/0000/"
#samples["BprimeBprime1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBprime_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBprime_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_29Nov/161201_101334/0000/"
#samples["BprimeBprime1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBprime_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBprime_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_29Nov/161201_101343/0000/"
#samples["BprimeBprime1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBprime_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBprime_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_29Nov/161201_101350/0000/"

#samples["QCDHT2000toInf_extv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext28Nov/161129_160003/0000/"
#samples["QCDHT1500to2000_extv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext28Nov/161129_160014/0000/"
#samples["QCD_HT1000to1500_v4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_29Nov/161130_184545/0000/"
#samples["QCD_HT700to1000_extv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext28Nov/161129_160024/0000/"
#samples["QCD_HT500to700_extv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext28Nov/161129_160033/0000/"
#samples["QCD_HT300to500_extv4"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext28Nov/161129_160042/0000/"

#samples["QCDHT2000toInf_v4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_28Nov/161129_155830/0000/"
#samples["QCDHT1500to2000_v4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_28Nov/161129_155840/0000/"
#samples["QCD_HT1000to1500_extv4"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext28Nov/161130_184003/0000/"
#samples["QCD_HT700to1000_v4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_28Nov/161129_155857/0000/"
#samples["QCD_HT500to700_v4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_28Nov/161129_155907/0000/"
#samples["QCD_HT300to500_v4"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_28Nov/161129_155916/0000/"

#samples["QCDHT2000toInf_extv2"]= "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext16Nov/161121_162535/0000/"
#samples["QCDHT1500to2000_extv2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext16Nov/161121_162528/0000/"
#samples["QCD_HT700to1000_extv2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext16Nov/161121_162521/0000/"
#samples["QCD_HT500to700_extv3"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext16Nov/161121_162511/0000/"

#samples["BprimeBToHB1800_v2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_16Nov/161116_180309/0000/"
#samples["QCDHT2000toInf_v2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_16Nov/161116_175551/0000/"
#samples["QCDHT1500to2000_v2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_16Nov/161116_175528/0000/"
#samples["QCD_HT1000to1500_v2"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_16Nov/161116_175505/0000/"
#samples["QCD_HT700to1000_v3"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_16Nov/161116_175448/0000/"
#samples["QCD_HT500to700_v3"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_16Nov/161116_175429/0000/"

#samples["BprimeBToHB800"] ="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135054/0000/"
#samples["BprimeBToHB800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135404/0000/"

#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135118/0000/"
#samples["BprimeBToHB1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135206/0000/"
#samples["BprimeBToHB1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135242/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135348/0000/"
#samples["BprimeBToHB1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p1_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_27Oct/161027_135404/0000/"

#samples["JetHT_runB"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/JetHT/Root80xV2p1_JetHT_runB_27Oct/161027_152901/0000/"
#samples["JetHT_runC"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/JetHT/Root80xV2p1_JetHT_runC_27Oct/161027_153519/0000/"
#samples["JetHT_runD"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/JetHT/Root80xV2p1_JetHT_runD_27Oct/161027_153621/0000/"
#samples["JetHT_runE"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/JetHT/Root80xV2p1_JetHT_runE_27Oct/161027_153827/0000/"
#samples["JetHT_runF"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/JetHT/Root80xV2p1_JetHT_runF_27Oct/161027_154002/0000/"
##samples["JetHT_runH"]=""
#samples["JetHT_runG"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/JetHT/Root80xV2p1_JetHT_runG_27Oct/161027_154236/0000/"

#samples["QCDHT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_02Nov/161102_161137/0000/"
#samples["QCDHT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_02Nov/161102_161130/0000/"
#samples["QCDHT1000to1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_04Nov/161104_085832/0000/"
#samples["QCDHT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV2p1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_02Nov/161102_161119/0000/"
#samples["QCDHT500to700"]=""

#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/Root80xV2p1_TT_TuneCUETP8M1_13TeV-powheg-pythia8_04Nov/161104_084952/0000/"

#samples["SingleMuon_runB"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/SingleMuon/Root80xV2p1_SingleMuon_C_02Nov/161103_142027/0009/"
#samples["SingleMuon_runC"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/SingleMuon/Root80xV2p1_SingleMuon_C_02Nov/161103_142027/0009/"
#samples["SingleMuon_runD"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/SingleMuon/Root80xV2p1_SingleMuon_D_02Nov/161103_142142/0009/"
#samples["SingleMuon_runE"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p1/SingleMuon/Root80xV2p1_SingleMuon_E_02Nov/161103_142425/0009/"
#######
#samples["QCD_HT50to100_ext1"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_18Oct/161018_135931/0000/"
#samples["QCD_HT50to100"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_10Octv1/161010_072137/0000/"
#samples["QCD_hpp"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root76xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_JetMet_21Sepv1/160921_140956/0000/"
#samples["DY_hpp"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-herwigpp/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-herwigpp_JetMet_17Sep/160917_163312/0000/"
#samples["QCD_hpp"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root80xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_18Sep/160917_163805/0000/"
#samples["prova1"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_05Aug/160805_074516/0000/"

#samples["SingleMuon_B_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/SingleMuon/Root80xV1_SingleMuon_B_05Aug/160805_075417/0001/"
#samples["SingleMuon_C_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/SingleMuon/Root80xV1_SingleMuon_C_05Aug/160805_075453/0001/"
#samples["SingleMuon_D_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/SingleMuon/Root80xV1_SingleMuon_D_05Aug/160805_075659/0001/"

#samples["QCD_HT300to500_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_03Aug_1/160803_091231/0001/"
#samples["QCD_HT300to500ext_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_03Aug/160803_090952/0001/"
#samples["QCD_HT200to300ext_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_03Aug/160803_090944/0001/"
#samples["QCD_HT200to300_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_03Aug_1/160803_091223/0001/"
#samples["QCD_Flat_Herwig_3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root80xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_03Aug_1/160803_091240/0001/"

#samples["QCD_HT200to300_2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_02Aug/160802_174122/0000/"
#samples["QCD_HT200to300ext_2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_02Aug/160802_174517/0000/"
#samples["QCD_HT300to500_2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_02Aug/160802_174130/0000/"
#samples["QCD_HT300to500ext_2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_02Aug/160802_174525/0000/"
#samples["QCD_Flat_Herwig_2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root80xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_02Aug/160802_174138/0000/"

#samples["ZeroBias_B"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/ZeroBias/Root80xV1_ZeroBias_B_01Aug/160801_072735/0002/"
#samples["ZeroBias_C"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/ZeroBias/Root80xV1_ZeroBias_01Aug/160801_072338/0002/"
#samples["ZeroBias_D"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/ZeroBias/Root80xV1_ZeroBias_D_01Aug/160801_072827/0002/"
#samples["QCD_HT200to300"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_01Aug/160801_073040/0002/"
#samples["QCD_HT200to300ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_01Aug/160801_073137/0002/"
#samples["QCD_HT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_01Aug/160801_073047/0002/"
#samples["QCD_HT300to500ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_01Aug/160801_073143/0002/"
#samples["QCD_Flat_Herwig"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root80xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_01Aug/160801_073054/0002/"

#samples["DY_ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root80xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_16Jul/160717_130942/0000/"
#samples["SingleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_ntuples_Fw80Xv1/SingleMuon/Root80xV1_SingleMuon_16Julv2/160717_152600/0001/"

#samples["QCD_HT100to200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_30May/160530_162044/0000/"

#samples["DY_ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_3Jun/160603_114203/0002/"
#samples["DY_v2_ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_8Jun/160607_221309/0002/"
#samples["test"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_2Jun/160602_061436/0000/"
#samples["QCD_HT200to300_ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_2Junv2/160602_061628/0000/"
#samples["QCD_HT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_2Junv2/160602_061635/0000/"
#samples["QCD_HT300to500_ext"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_2Jun/160602_061444/0000/"
#samples["QCD_HT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_2Jun/160602_061451/0000/"

#samples["QCD_Pt50to80"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160510_102950/0000/"
#samples["QCD_Pt85to120"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160510_102943/0000/"
#samples["QCD_Pt600to800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160510_102958/0000/"
#samples["QCD_Pt800to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160510_103009/0000/"

#samples["QCD_Pt15to30"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145730/0000/"
#samples["QCD_Pt30to50"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145816/0000/"
#samples["QCD_Pt120to170"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145715/0000/"
#samples["QCD_Pt170to300"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145738/0000/"
#samples["QCD_Pt300to470"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145804/0000/"
#samples["QCD_Pt470to600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145823/0000/"
#samples["QCD_Pt1000to1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145707/0000/"
#samples["QCD_Pt1400to1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145723/0000/"
#samples["QCD_Pt1800to2400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145744/0000/"
#samples["QCD_Pt2400to3200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/Root76xV1_QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8_JetMet_09May/160509_145752/0000/"

#samples["SingleMuon_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/SingleMuon/Root76xV1_SingleMuon_JetMet_09May/160509_191020/0000/"
#samples["DY_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_09May/160509_190925/0000/"
#samples["SingleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/SingleMuon/Root76xV1_SingleMuon_JetMet_03May/160504_071706/0000/"
#samples["Template"]="/pnfs/psi.ch/cms/trivcat/store/user/grauco/PixelResolution_2016/ZeroBias1/PixRes_ZeroBias1_Run2016B-PromptReco-v1_272022_Templatev1/160509_124935/0000/"
#samples["Generic"]="/pnfs/psi.ch/cms/trivcat/store/user/grauco/PixelResolution_2016/ZeroBias1/PixRes_ZeroBias1_Run2016B-PromptReco-v1_272022_Genericv1/160509_125434/0000/"
#samples["ZeroBias"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/ZeroBias/Root76xV1_ZeroBias_JetMet_03May/160503_193838/0002/"

#samples["QCD_herwig"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root76xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_JetMet_03May/160504_071801/0000/"
#samples["QCD_pythia"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/Root76xV1_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_JetMet_03May/160504_071747/0000/"
#samples["DY"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_03May/160503_193712/0000/"
#samples["SingleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/SingleMuon/Root76xV1_SingleMuon_JetMet_23Aprv3/160423_100059/0000/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DoubleMuon/Root76xV1_DoubleMuon_JetMet_23Aprv3/160423_100043/0000/"
#samples["JetHT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/JetHT/Root76xV1_JetHT_JetMet_23Aprv3/160423_100052/0000/"
#samples["DY"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_JetMet_23Aprv4/160424_200443/0000/"
#samples["QCD_pythia"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/Root76xV1_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_JetMet_23Aprv4/160424_200458/0000/"
#samples["QCD_herwig"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV2/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root76xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_JetMet_23Aprv4/160424_200507/0000/"
#samples["DY_v2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_16Apr/160416_173648/0000/"

#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_JetMet_07Apr_v1/160407_121304/0003/"
#samples["DY"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_JetMet_07Apr_v1/160407_121733/0003/"
#samples["QCD_pythia"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/Root76xV1_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_JetMet_08Apr_v1/160408_090651/0003/"
#samples["QCD_herwig"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root76xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_JetMet_08Apr_v1/160408_090658/0003/"
#samples["QCD_pythia"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/Root76xV1_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_JetMet_20Mar/160320_080906/0003/"
#samples["QCD_pythiav"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/Root76xV1_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_JetMet_22Mar_v1/160322_115225/0000/"
#samples["QCD_herwigg"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/Root76xV1_QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp_JetMet_20Mar/160320_080914/0003/"
#samples["GJets"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/Root76xV1_GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8_JetMet_20Mar/160320_080923/"
#samples["SinglePhoton"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/SinglePhoton/Root76xV1_SinglePhoton_JetMet_20Mar/160320_081218/"
#samples["JetHT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/JetHT/Root76xV1_JetHT_JetMet_08Apr_v1/160408_090954/0003/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0000/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0001/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0002/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0003/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0004/"
#samples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0005/"
#xssamples["DoubleMuon"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/JetMet_Fw76XV1/DoubleMuon/Root76xV1_DoubleMuon_12Mar/160312_045353/0006/"

##samples["MET"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/TTDM_CMSSW_74X_V4/MET/MET25ns_Root1Oct/151001_143915/0000/"

#samples["DMtt_sc_Mchi1Mphi10"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172953/0000/" 
#samples["DMtt_sc_Mchi10Mphi10"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172915/0000/"

#samples["DMtt_sc_Mchi1Mphi20"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173007/0000/" 

#samples["DMtt_sc_Mchi1Mphi50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172900/0000/"
#samples["DMtt_sc_Mchi10Mphi50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172923/0000/"
#samples["DMtt_sc_Mchi50Mphi50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173114/0000/"

#samples["DMtt_sc_Mchi1Mphi100"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172945/0000/"
#samples["DMtt_sc_Mchi10Mphi100"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172908/0000/"

#samples["DMtt_sc_Mchi1Mphi200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172959/0000/"
#samples["DMtt_sc_Mchi50Mphi200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173043/0000/"
#samples["DMtt_sc_Mchi150Mphi200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-150_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-150_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172930/0000/"

#samples["DMtt_sc_Mchi1Mphi300"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173015/0000/"
#samples["DMtt_sc_Mchi50Mphi300"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173051/0000/"

#samples["DMtt_sc_Mchi1Mphi500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173024/0000/"
#samples["DMtt_sc_Mchi500Mphi500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-500_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-500_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173033/0000/"

#samples["DMtt_sc_Mchi1Mphi1000"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_scalar_Mchi-1_Mphi-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_scalar_Mchi-1_Mphi-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_172936/0000/"


#samples["DMtt_ps_Mchi1Mphi10"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173216/0000/"
#samples["DMtt_ps_Mchi10Mphi10"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173130/0000/"

#samples["DMtt_ps_Mchi1Mphi20"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173238/0000/"

#samples["DMtt_ps_Mchi1Mphi50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173317/0000/"
#samples["DMtt_ps_Mchi50Mphi50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173137/0000/"
#samples["DMtt_ps_Mchi50Mphi50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173347/0000/"

#samples["DMtt_ps_Mchi1Mphi100"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173208/0000/"
#samples["DMtt_ps_Mchi10Mphi100"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173122/0000/"

#samples["DMtt_ps_Mchi1Mphi200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173225/0000/"
#samples["DMtt_ps_Mchi50Mphi200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173332/0000/"
#samples["DMtt_ps_Mchi150Mphi200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-150_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-150_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173153/0000/"

#samples["DMtt_ps_Mchi1Mphi300"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173246/0000/"
#samples["DMtt_ps_Mchi50Mphi300"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173339/0000/"

#samples["DMtt_ps_Mchi1Mphi500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173305/0000/"
#samples["DMtt_ps_Mchi150Mphi500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-150_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-150_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173200/0000/"
#samples["DMtt_ps_Mchi500Mphi500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/TTbarDMJets_pseudoscalar_Mchi-500_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_TTbarDMJets_pseudoscalar_Mchi-500_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173325/0000/"


#samples["WJets_HT100to200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT100to200noSyst_10Feb_jesmet/160213_031229/0000/"
#samples["WJets_HT200to400"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT200to400noSyst_10Feb_jesmet/160213_031243/0000/"
#samples["WJets_HT400to600"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT400to600noSyst_10Feb_jesmet/160213_031300/0000/"
#samples["WJets_HT600to800"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT600to800noSyst_10Feb_jesmet/160213_031314/0000/"
#samples["WJets_HT800to1200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT800to1200noSyst_10Feb_jesmet/160213_031328/0000/"
#samples["WJets_HT1200to2500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT1200to2500noSyst_10Feb_jesmet/160213_031341/0000/"
#samples["WJets_HT2500toInf"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJets_HT2500toInfnoSyst_10Feb_jesmet/160213_031355/0000/"

#samples["ZJets_HT100to200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root_ZJetsToNuNu_HT-100To200_13TeV-madgraph_jes_2F/160305_131158/0000/"
#samples["ZJets_HT200to400"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root_ZJetsToNuNu_HT-200To400_13TeV-madgraph_jes_2F/160305_131205/0000/"
#samples["ZJets_HT400to600"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root_ZJetsToNuNu_HT-400To600_13TeV-madgraph_jes_2F/160305_131211/0000/"
#samples["ZJets_HT600toInf"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_jes_2F/160305_130518/0000/"


#samples["ZJets_HT100to200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root_ZJetsToNuNu_HT-100To200_13TeV-madgraph_jer_2F/160211_172716/0000/"
#samples["ZJets_HT200to400"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root_ZJetsToNuNu_HT-200To400_13TeV-madgraph_jer_2F/160211_172725/0000/"
#samples["ZJets_HT400to600"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root_ZJetsToNuNu_HT-400To600_13TeV-madgraph_jer_2F/160211_172735/0000/"
#samples["ZJets_HT600toInf"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_jer_2F/160211_172741/0000/"


#samples["ZJets_HT100to200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root_ZJetsToNuNu_HT-100To200_13TeV-madgraph_met_2F/160211_173849/0000/"
#samples["ZJets_HT200to400"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root_ZJetsToNuNu_HT-200To400_13TeV-madgraph_met_2F/160211_173902/0000/"
#samples["ZJets_HT400to600"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root_ZJetsToNuNu_HT-400To600_13TeV-madgraph_met_2F/160211_173911/0000/"
#samples["ZJets_HT600toInf"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_met_2F/160211_173919/0000/"


#samples["SingleEl_05Oct"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/SingleElectron/Root_SingleElectrondecosa-SingleEl_Run2015D_miniAODv2_13Nov-ff3168b63d5cee365f49bf7ea3ba6ef3_2F/160222_002842/0000/"
#samples["SingleEl_Promptv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/SingleElectron/Root_SingleElectrondecosa-SingleEl_Run2015D_PromptV4_13Nov-5daaa7fbf157b0642c1d3dfb260fbeff_2F/160222_002835/0000/"
#samples["SingleMu_05Oct"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/SingleMuon/Root_SingleMuondecosa-SingleMu_Run2015D_miniAODv2_v2_13Nov-ff3168b63d5cee365f49bf7ea3ba6ef3_2F/160222_002828/0000/"
#samples["SingleMu_Promptv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/SingleMuon/Root_SingleMuondecosa-SingleMu_Run2015D_PromptV4_v2_13Nov-5daaa7fbf157b0642c1d3dfb260fbeff_2F/160222_002822/0000/"


#samples["MET_05Oct"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/MET/Root_METdecosa-MET_Run2015D_miniAODv2_13Nov-ff3168b63d5cee365f49bf7ea3ba6ef3_2F/160222_002855/0000/"
#samples["MET_Promptv4"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/MET/Root_METdecosa-MET_Run2015D_PromptV4_13Nov-5daaa7fbf157b0642c1d3dfb260fbeff_2F/160222_002849/0000/"


#samples["TT"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/oiorio/ttDM/trees/2016/Feb/10Feb/TT_TuneCUETP8M1_13TeV-powheg-pythia8/TTnoSyst_10Feb_jesmet/160213_031017/0000/"



#samples["QCD_HT100_200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/dpinna/Samples_v2_Fw7_4_15_2016/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_njes_14J/160114_173407/0000/"



#samples["QCD_HT100_200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131431/0000/"
#samples["QCD_HT200_300"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131437/0000/"
#samples["QCD_HT300_500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131443/0000/"
#samples["QCD_HT500_700"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131449/0000/"
#samples["QCD_HT700_1000"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131456/0000/"
#samples["QCD_HT1000_1500"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131502/0000/"
#samples["QCD_HT1500_2000"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131508/0000/"
#samples["QCD_HT2000_Inf"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/7_4_15_Moriond2016_v3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_jes_2F/160305_131518/0000/"


#samples["ttDM1"] ="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Synchro/TTDMDMJets_M1GeV_Tune4C_13TeV-madgraph-tauola/DM1/150603_132943/0000/"
#samples["ttDM10"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Tree_sys_v4/TTDMDMJets_M10GeV_Tune4C_13TeV-madgraph-tauola/DM10/150523_175813/0000/"
#samples["ttDM50"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Tree_sys_v4/TTDMDMJets_M50GeV_Tune4C_13TeV-madgraph-tauola/DM50/150523_180045/0000/"
#samples["ttDM100"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Tree_sys_v4/TTDMDMJets_M100GeV_Tune4C_13TeV-madgraph-tauola/DM100/150523_175839/0000/"
#samples["ttDM200"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Tree_sys_v4/TTDMDMJets_M200GeV_Tune4C_13TeV-madgraph-tauola/DM200/150523_175936/0000/"
#samples["ttDM600"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Tree_sys_v4/TTDMDMJets_M600GeV_Tune4C_13TeV-madgraph-tauola/DM600/150523_180003/0000/"
#samples["ttDM1000"] = "/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/ttDM/Phys14_Tree_sys_v4/TTDMDMJets_M1000GeV_Tune4C_13TeV-madgraph-tauola/DM1000/150524_174542/0000/"

#samples.append("SingleTop_T_tchan")
#samples.append("SingleTop_Tbar_tchan")
#samples.append("T_tW")
#samples.append("Tbar_tW")

newpath = 'work/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

for sample ,path in samples.iteritems():
    cmd = cmdls + srm + path
    status,ls_la = commands.getstatusoutput( cmd )
    dir = [ ]
    list = ls_la.split(os.linesep)
    #print list
    if(scratch): cmd_cp = cmdcp + srm + path
    else: cmd_cp = cmdcp +  path
    files =[ l.split('/')[-1] for l in list]
    #print files
    cmd = "gfal-mkdir " + outdir + sample
    os.system(cmd)


#    for f in files:
#        newcmd = cmd_cp + f + " " + outdir + sample + "/" +f
#        print newcmd
#        os.system(newcmd)

    
    for f in files:
        workdir = 'work/' + sample + "_" + str(files.index(f))
        jobid = sample + "_" + str(files.index(f))
        #        newcmd = cmd_cp + f + " " + outdir + sample + "/" +f
        newcmd = "qexe.py -w " + workdir + " " +  jobid + " -- " + cmd_cp + f + " " + outdir + sample + "/" +f
        print newcmd
        os.system(newcmd)
