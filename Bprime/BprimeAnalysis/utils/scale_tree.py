import sys
import os, commands
import shutil
from ROOT import *
import ROOT
from optparse import OptionParser

argv = sys.argv
parser = OptionParser()

(opts, args) = parser.parse_args(argv) 

inDirName = '/mnt/t3nfs01/data01/shome/grauco/BprimeAna/CMSSW_7_6_3_patch2/src/Bprime/BprimeAnalysis/trees_b0'
outDirName = '/mnt/t3nfs01/data01/shome/grauco/BprimeAna/CMSSW_7_6_3_patch2/src/Bprime/BprimeAnalysis/trees_out'
inTreeName = 'BprimeTree'
targetFile = "qcd_b0"
addcmd = "hadd -f %s/%s.root " %(outDirName,targetFile)
rmcmd = "rm "

n = 0 
for inFileName in os.listdir(inDirName):
#  print inFileName
  if inFileName.endswith("singleH.root") and inFileName.startswith("tree_QCD_HT1"):
    n += 1
    print "copying file %i" %n
    shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
    inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
    #if inFileName=="tree_QCD_HT100to200_singleH.root" :
    #  xSec = 27850000. 
    #  genEv = 82048343#82048490. 
    #elif inFileName=="tree_QCD_HT200to300_singleH.root" :
    #  xSec = 1717000.
    #  genEv = 18784379#18784460.
    #elif inFileName=="tree_QCD_HT300to500_singleH.root" :
    #  xSec = 351300.
    #  genEv = 16909004#16909260. 
    #elif inFileName=="tree_QCD_HT500to700_singleH.root" :
    #  xSec = 31630.
    #  genEv = 19665695#19760630.
    #elif inFileName=="tree_QCD_HT700to1000_singleH.root" :
    #  xSec = 6802. 
    #  genEv = 15547962#26956700.
    if inFileName=="tree_QCD_HT1000to1500_singleH.root" :
      xSec = 1206.
      genEv = 100000.#5049267
    elif inFileName=="tree_QCD_HT1500to2000_singleH.root" :  
      xSec = 120.4 
      genEv = 100000.#3939077
    #elif inFileName=="tree_QCD_HT2000toInf_singleH.root" :
    #  xSec = 25.25 
    #  genEv =1981228. #8873794. 
    else:
      print " Cross section not defined! Exiting..."
      sys.exit()

    weight = (xSec*2600.)/genEv
    print "--------"
    print inFileName
    print weight
    print "--------"
    myTree = inFile.Get( inTreeName )
    myTree.SetWeight(weight)
    myTree.AutoSave()

    addcmd+= ' %s/%s' %(outDirName, inFileName)
    rmcmd += ' %s/%s' %(outDirName, inFileName)

os.system(addcmd)
#print "Removing temporary files"
#os.system(rmcmd)
inFile.Close()
del myTree
