import os, commands

scratch = False
cmdls = "lcg-ls"
srm = "  -b -D srmv2 srm://storage01.lcg.cscs.ch:8443/srm/managerv2\?SFN="


### To store on t3 storage element
cmdcp = "globus-url-copy -continue-on-error -rst -nodcau -fast -vb -v -cd -r gsiftp://storage01.lcg.cscs.ch/"
#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/decosa/ttDM/Moriond_v3/jes/"
#outdir = "gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/decosa/ttDM/TEST/"
outdir="gsiftp://t3se01.psi.ch/pnfs/psi.ch/cms/trivcat/store/user/grauco/BprimeAnalysis_76X_FwkV1p2/"

### To store on t3 scratch area
if(scratch):
    cmdcp = "lcg-cp"
    outdir = "/scratch/grauco/test/"


samples = {}

#samples["BprimeBToHB700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-700_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-700_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115443/0000/"
#samples["BprimeBToHB800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115449/0000/"
#samples["BprimeBToHB900"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115456/0000/"
#samples["BprimeBToHB1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115503/0000/"
#samples["BprimeBToHB1100"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115510/0000/"
#samples["BprimeBToHB1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115517/0000/"
#samples["BprimeBToHB1300"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1300_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1300_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115524/0000/"
#samples["BprimeBToHB1400"]=""
#samples["BprimeBToHB1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115532/0000/"
#samples["BprimeBToHB1600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115539/0000/"
#samples["BprimeBToHB1700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115546/0000/"
#samples["BprimeBToHB1800"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8/Root76xV1_BprimeBToHB_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8_1204v1/160415_115554/0000/"
#samples["JetHT_16Dec"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/JetHT/Root76xV1_JetHT_1204v1/160414_140245/0001/"
#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/Root76xV1_TT_TuneCUETP8M1_13TeV-powheg-pythia8_1204/160412_150943/0000/"
#samples["QCD_HT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180758/0000/"
#samples["QCD_HT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180750/0000/"
#samples["QCD_HT1000to1500"]="pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180738/0000/"
#samples["QCD_HT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180727/0000/"
#samples["QCD_HT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180712/0000/"
#samples["QCD_HT300to500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180703/0000/"
#samples["QCD_HT200to300"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204/160413_180652/0000/"
#samples["QCD_HT100to200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v1/160413_183640/0000/"


samples["WJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v1/160415_122742/0000/"
samples["WJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v1/160415_122748/0000/"
samples["WJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v1/160415_122755/0000/"
samples["WJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v2/160417_111148/0000/"

#samples["WJets_800_1200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v1/160415_122802/0000/"
#samples["WJets_600_800"]=""
#samples["WJets_1200_2500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v2/160415_123126/0000/"
#samples["WJets_2500_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1204v1/160415_122813/0000/"

#samples["ZJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-100To200_13TeV-madgraph_1204v1/160415_122900/0000/"
#samples["ZJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-200To400_13TeV-madgraph_1204v1/160415_122907/0000/"
#samples["ZJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-400To600_13TeV-madgraph_1204v1/160415_122914/0000/"
#samples["ZJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Fw76XV1p2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_1204v1/160415_122946/0000/"


#samples["JetHT_16Dec"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/JetHT/Root76xV1_JetHT_18Mar_v3/160317_214111/0001/"
#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar/160317_141140/0000/"
#samples["QCD_HT500to700"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar/160317_135241/0000/"
#samples["QCD_HT700to1000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar_v1/160317_152728/0000/"
#samples["QCD_HT1000to1500"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar/160317_135905/0000/"
#samples["QCD_HT1500to2000"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar/160317_135944/0000/"
#samples["QCD_HT2000toInf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar/160317_140003/0000/"
#samples["WJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar_v1/160317_141737/0000/"
#samples["WJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar_v1/160317_141848/0000/"
#samples["WJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar_v1/160317_141751/0000/"
#samples["WJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_18Mar_v1/160317_141800/0000/"
#samples["ZJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-100To200_13TeV-madgraph_18Mar_v3/160317_220603/0000/"
#samples["ZJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-200To400_13TeV-madgraph_18Mar_v3/160317_220610/0000/"
#samples["ZJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-400To600_13TeV-madgraph_18Mar_v1/160317_141931/0000/"
#samples["ZJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV2/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_18Mar_v1/160317_141949/0000/"

#samples["JetHT_16Dec"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/JetHT/Root76xV1_JetHT_12Mar/160312_192203/0000\
#/" #6                                                                                                                                          
#samples["ZJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-100To200_13TeV-madgraph_12Mar/160312_193254/0006/" #5                                            
#samples["TT"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160315_083130/0000/"                          
#samples["ZJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-200To400_13TeV-madgraph_12Mar/160312_193302/0005/" #8                                                                      
#samples["ZJets_400_600"]="/pnfs/lcg.cscs.ch/cms/tr7vcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root7\6xV1_ZJetsToNuNu_HT-400To600_13TeV-madgraph_12Mar/160312_193310/0003/" #2                                                                      
#samples["WJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160312_193211/0007/" #7                    
#samples["WJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160312_193157/0000/"#3                       
#samples["WJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160312_193204/0000/"#2                      
#samples["WJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160313_072235/0000/"                         
#samples["ZJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_12Mar/160313_070806/0002/"#2                                                                       


#samples["ZJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-100To200_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-100To200_13TeV-madgraph_12Mar/160312_193254/0000/" #5                                     
#samples["ZJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-200To400_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-200To400_13TeV-madgraph_12Mar/160312_193302/0000/" #8                                                                    
#samples["ZJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-400To600_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-400To600_13TeV-madgraph_12Mar/160312_193310/0000/" #2 
#samples["ZJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/Root76xV1_ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_12Mar/160313_070806/0000/"

#samples["JetHT_16Dec"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/JetHT/Root76xV1_JetHT_12Mar/160312_192203/0006/"
#samples["WJets_200_400"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-magraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160312_193211/0007/" 
#samples["WJets_400_600"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160312_193157/0002/"
#samples["WJets_600_Inf"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160312_193204/0001/"
#samples["WJets_100_200"]="/pnfs/lcg.cscs.ch/cms/trivcat/store/user/grauco/Analysis_Bprime_Fw76XV1/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Root76xV1_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_12Mar/160313_072235/0000/"
#732



#=====

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


    
    for f in files:
        workdir = 'work/' + sample + "_" + str(files.index(f))
        jobid = sample + "_" + str(files.index(f))
        #        newcmd = cmd_cp + f + " " + outdir + sample + "/" +f
        newcmd = "qexe.py -w " + workdir + " " +  jobid + " -- " + cmd_cp + f + " " + outdir + sample + "/" +f
        #print newcmd
        os.system(newcmd)
