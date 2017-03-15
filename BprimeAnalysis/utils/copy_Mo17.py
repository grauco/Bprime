

import os, commands
from os.path import exists

scratch = False


#cmdls = "gfal-ls "                                                                                                                                                 
#cmdcp = "gfal-copy "
#srm = "srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="
#outdir="srm://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/testPerGiulia/"

cmdls = "lcg-ls"

srm = "  -b -D srmv2 srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="


ifile = " root://storage01.lcg.cscs.ch/"

#srm = "  -b -D srmv2 srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="
#srm = " -b -D srmv2 srm://t3se01.psi.ch"
### To store on t3 storage element
#cmdcp = "globus-url-copy -continue-on-error -rst -nodcau -fast -vb -v -cd -r gsiftp://storage01.lcg.cscs.ch/"
cmdcp = "xrdcp -d 1 "
#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/decosa/ttDM/Moriond_v3/jes/"
#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/JetMet_76X_v7/"

#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/Bprime_80Xv2p4_v1/"#JetMet_80X_v1/"
outdir = "root://t3dcachedb.psi.ch:1094///pnfs/psi.ch/cms/trivcat/store/user/decosa/Moriond17_15Feb/"#JetMet_80X_v1/"

### To store on t3 scratch area
if(scratch):
    cmdcp = "lcg-cp "
    outdir = "/scratch/grauco/"

samples = {}


#samples["BprimeBToHB900"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170214_090654/0000/"
#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170213_133703/0000/"
#samples["BprimeBToHB1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170213_133721/0000/"
#samples["BprimeBToHB1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170213_133740/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170213_104548/0000/"
#samples["BprimeBToHB1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170213_133802/0000/"
#samples["BprimeBToHB1100"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170214_090705/0000/"
#samples["BprimeBToHB1300"]=""
#samples["BprimeBToHB1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170214_090735/0000/"
#samples["BprimeBToHB1700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/BprimeBToHB_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8_08Feb17/170214_090756/0000/"



#samples["JetHT_runB"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016B-23Sep2016-v3_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_181738/0000/"
#samples["JetHT_runB"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016B-23Sep2016-v3_B2GAnaFW_80X_V2p4_v1_08Feb17/170211\_181738/0001/"
samples["JetHT_runB"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016B-23Sep2016-v3_B2GAnaFW_80X_V2p4_v1_08Feb17/170211\_181738/0002/"
#samples["JetHT_runC"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016C-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175235/0000/"
#samples["JetHT_runD"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT//Root80xV2p4_JetHTRun2016D-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175249/0000/"
#samples["JetHT_runD"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT//Root80xV2p4_JetHTRun2016D-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175249/0001/"
#samples["JetHT_runE"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016E-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175302/0000/"
#samples["JetHT_runF"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016F-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175315/0000/"
#samples["JetHT_runHv3"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016H-PromptReco-v3_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175404/0000/"
#samples["JetHT_runHv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016H-PromptReco-v2_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175350/0000/"
#samples["JetHT_runHv2"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016H-PromptReco-v2_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175350/0001/"
#samples["JetHT_runG"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016G-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175332/0000/"
samples["JetHT_runG"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/decosa/Bprime_Mo17/JetHT/Root80xV2p4_JetHTRun2016G-23Sep2016-v1_B2GAnaFW_80X_V2p4_v1_08Feb17/170211_175332/0001/"




####start samples for moriond 17 _ v1
#samples["BprimeBToHB800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081857/0000/"
#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081913/0000/"
#samples["BprimeBToHB1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081932/0000/"
#samples["BprimeBToHB1400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081940/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_081949/0000/"
#samples["BprimeBToHB1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Bprime_Fw80Xv2p4/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root80xV2p4_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_13J/170110_082001/0000/"

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


newpath = 'work/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

for sample ,path in samples.iteritems():
    cmd = cmdls + srm + path
    print "lgc-ls: ", cmd
    status,ls_la = commands.getstatusoutput( cmd )
    dir = [ ]
    list = ls_la.split(os.linesep)
    #print list
    if(scratch): cmd_cp = cmdcp + srm + path
    else: cmd_cp = cmdcp + ifile +  path
    files =[ l.split('/')[-1] for l in list]
    #print files
    cmd = "gfal-mkdir " + outdir + sample
    print "===>Mkdir command: ", cmd
    os.system(cmd)


#    for f in files:
#        newcmd = cmd_cp + f + " " + outdir + sample + "/" +f
#        print newcmd
#        os.system(newcmd)

#    writer =open("Logs/"+sample+".log", 'a+')

    dirLogs = "Logs/"
    if exists(dirLogs):
        print 'Logs/ folder already exists'
    else: os.makedirs(dirLogs)

    with open("Logs/"+sample+".log",'w') as of:

        for f in files:
            workdir = 'work/' + sample + "_" + str(files.index(f))
            jobid = sample + "_" + str(files.index(f))
            #        newcmd = cmd_cp + f + " " + outdir + sample + "/" +f
            #        newcmd = "qexe.py -w " + workdir + " " +  jobid + " -- " + cmd_cp + f + " " + outdir + sample + "/" +f
            newcmd = cmd_cp + f + " " + outdir + sample + "/ -f"
            of.write(newcmd + "\n")
            os.system(newcmd)

 


