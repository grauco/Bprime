import sys
import os, commands
import shutil
from ROOT import *
import ROOT
from optparse import OptionParser

argv = sys.argv
parser = OptionParser()

parser.add_option("-d", "--useDAS", dest="useDAS", default=True, action="store_true",
                              help="Use # gen events from DAS")

(opts, args) = parser.parse_args(argv) 

inDirName = '/mnt/t3nfs01/data01/shome/grauco/BprimeAna/CMSSW_7_6_3_patch2/src/Bprime/BprimeAnalysis/trees_b0'
outDirName = '/mnt/t3nfs01/data01/shome/grauco/BprimeAna/CMSSW_7_6_3_patch2/src/Bprime/BprimeAnalysis/trees_out'
inTreeName = 'BprimeTree'
histName = "ht"
targetFile = "qcd_b0"
addcmd = "hadd -f %s/%s.root " %(outDirName,targetFile)
rmcmd = "rm "

n = 0 
for inFileName in os.listdir(inDirName):
  print inFileName
  if inFileName.endswith(".root") and inFileName.startswith("tree_QCD_"):
    n += 1
    print "copying file %i" %n
    shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
    inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
    if inFileName.find("HT100") != -1:
      xSec = 27850000. 
      genEv = 82048343#82048490. 
    elif inFileName.find("HT200") != -1:
      xSec = 1717000.
      genEv = 18784379#18784460.
    elif inFileName.find("HT300") != -1:
      xSec = 351300.
      genEv = 16909004#16909260. 
    elif inFileName.find("HT500") != -1:
      xSec = 31630.
      genEv = 19665695#19760630.
    elif inFileName.find("HT700") != -1:
      xSec = 6802. 
      genEv = 15547962#26956700.
    elif inFileName.find("HT1000") != -1:
      xSec = 1206.
      genEv = 5049267#19228700.
    elif inFileName.find("HT1500") != -1:  
      xSec = 120.4 
      genEv = 3939077#17555450. 
    elif inFileName.find("HT2000") != -1:
      xSec = 25.25 
      genEv =1981228. #8873794. 
    else:
      print " Cross section not defined! Exiting..."
      sys.exit()
    if not opts.useDAS:
      print inFile
      print histName
      genEv = inFile.Get(histName).GetBinContent(1)
      print 'Not using gen events from DAS! Using %i events stored in %s' %(genEv,inFileName)
    weight = (xSec*2600.)/genEv
    print weight
    myTree = inFile.Get( inTreeName )
    myTree.SetWeight(weight)
    myTree.AutoSave()

    addcmd+= ' %s/%s' %(outDirName, inFileName)
#    rmcmd += ' %s/%s' %(outDirName, inFileName)

os.system(addcmd)
print "Removing temporary files: ..."
# os.system(rmcmd)
inFile.Close()
del myTree
