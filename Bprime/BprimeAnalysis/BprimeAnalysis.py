#!/bin/env python
import os
import shutil
import optparse 

import subprocess
import sys
import glob
import math
import pickle

from os.path import join,exists

print 'Python version', sys.version_info
if sys.version_info < (2, 7):
    raise "Must use python 2.7 or greater. Have you forgotten to do cmsenv?"

workDir = 'work'
fileListDir = join(workDir,'files')
splitDir = 'split'
splitDescriptionFile = 'description.pkl'
resDirs = ['res','trees','txt']
hline = '-'*80

#localPath = "/mnt/t3nfs01/data01/shome/grauco/BprimeAna/CMSSW_7_6_3_patch2/src/ttDM/newTTDManalysis/"
localPath = "/mnt/t3nfs01/data01/shome/grauco/BprimeAna/CMSSW_7_6_3_patch2/src/Bprime/BprimeAnalysis/"
#t3Path = '//pnfs/psi.ch/cms/trivcat/store/user/grauco/BprimeAnalysis_76X_FwkV1p2/'
#t3Path = '//pnfs/psi.ch/cms/trivcat/store/user/grauco/JetMet_80Xv2p1_v1/' 

#t3Path = '//pnfs/psi.ch/cms/trivcat/store/user/grauco/Bprime_80Xv2p4_Mo17v4/'
t3Path = '//pnfs/psi.ch/cms/trivcat/store/user/decosa/Moriond17/'
#t3Path = '//pnfs/psi.ch/cms/trivcat/store/user/decosa/Moriond17_15Feb/'
#t3Path = '//pnfs/psi.ch/cms/trivcat/store/user/grauco/Bprime_80Xv2p4_Mo17v4/Trigger/'
#t3Path = '/pnfs/psi.ch/cms/trivcat/store/user/ggiannin/TprimeTrees_Fw80Xv2p1/'

t3Ls = 'xrdfs t3dcachedb03.psi.ch ls -u'

samples = []
#samples.append("JetHT_runB")                                                                                            
#samples.append("JetHT_runC")                                                                                              
#samples.append("JetHT_runD")                                                                                             
#samples.append("JetHT_runE")                                                                                             
#samples.append("JetHT_runF")                                                                                              
#samples.append("JetHT_runG")                                                                                              
#samples.append("JetHT_runHv2")                                                                                           
#samples.append("JetHT_runHv3")  

#samples.append("TT")
#samples.append("QCDHT2000toInf")                                                                                         
#samples.append("QCDHT1500to2000")                                                                                        
#samples.append("QCDHT1000to1500")                                                                                        #
#samples.append("QCDHT700to1000")                                                                                        # 
#samples.append("QCDHT500to700")                                                                                        
#samples.append("QCDHT300to500")
#samples.append("QCDHT2000toInfext")                                                                                    
#samples.append("QCDHT1500to2000ext")                                                                                   
#samples.append("QCDHT1000to1500ext")                                                                                    
#samples.append("QCDHT700to1000ext")                                                                                     
#samples.append("QCDHT500to700ext")                                                                                        
#samples.append("QCDHT300to500ext")  

#samples.append("WJetsHT600to800")
#samples.append("WJetsHT800to1200")
#samples.append("WJetsHT1200to2500")
#samples.append("WJetsHT2500toInf")
#samples.append("ZJetsHT600to800")
#samples.append("ZJetsHT800to1200")
#samples.append("ZJetsHT1200to2500")
#samples.append("ZJetsHT2500toInf")
#samples.append("WJetsHT600to800")
#samples.append("WJetsHT800to1200")
#samples.append("WJetsHT1200to2500")
#samples.append("WJetsQQ")
#samples.append("DYQQ")

#samples.append("BprimeBToHB800")
#samples.append("BprimeBToHB900")
#samples.append("BprimeBToHB1000")
#samples.append("BprimeBToHB1100")
#samples.append("BprimeBToHB1200")
##samples.append("BprimeBToHB1300") 
#samples.append("BprimeBToHB1400")
#samples.append("BprimeBToHB1500")
#samples.append("BprimeBToHB1600")
#samples.append("BprimeBToHB1700")
samples.append("BprimeBToHB1800")

######

#samples.append("Test_3")
#samples.append("SingleMubv1")
#samples.append("SingleMub")
#samples.append("SingleMuc")
#samples.append("SingleMud")
#samples.append("SingleMue")
#samples.append("SingleMuf")
#samples.append("SingleMug")
#samples.append("SingleMuhv1")
#samples.append("SingleMuhv2")
#samples.append("SingleMuhv3")

#samples.append("JetHTbv3")
#samples.append("JetHTc")
##samples.append("JetHTd")
#samples.append("JetHTe")
#samples.append("JetHTf")
##samples.append("JetHTg")
#samples.append("JetHThv2")
#samples.append("JetHThv3")

#samples.append("WJets_100_200")
#samples.append("WJets_200_400")
#samples.append("WJets_400_600")
#samples.append("WJets_600_800")
#samples.append("WJets_800_1200")
#samples.append("WJets_1200_2500")
#samples.append("WJets_2500_Inf")
#samples.append("ZJets_100_200")
#samples.append("ZJets_200_400")
#samples.append("ZJets_400_600")
#samples.append("ZJets_600_800")
#samples.append("ZJets_800_1200")
#samples.append("ZJets_1200_2500")#
#samples.append("ZJets_2500_Inf")

#samples.append("TT_v2")                                                                                                                         #           
#samples.append("WJets_100_200")                                                                                                                            # 
#samples.append("WJets_200_400")                                                                                                                                 
#samples.append("WJets_400_600")                                                                                                                                    
#samples.append("WJets_600_Inf") 
#samples.append("ZJets_100_200")                                                                                                                              #   
#samples.append("ZJets_200_400")                                                                                                                                
#samples.append("ZJets_400_600")                                                                                                                                   
#samples.append("ZJets_600_Inf")  
#samples.append("SingleMuon_runB")
#samples.append("SingleMuon_runC")
#samples.append("SingleMuon_runD")
#samples.append("SingleMuon_runE")

#samples.append("TT")
#samples.append("QCDHT2000toInf")
#samples.append("QCDHT1500to2000")
#samples.append("QCDHT1000to1500")
#samples.append("QCDHT700to1000")
#samples.append("QCDHT500to700")
#samples.append("QCDHT300to500")

#samples.append("QCDHT2000toInf_v4")                                                                                                           
#samples.append("QCD_HT1000to1500_extv4") 
#samples.append("QCD_HT1000to1500_v4")                                                                              #                 #          \
#samples.append("QCDHT1500to2000_v4")                                                                                #                          
#samples.append("QCD_HT700to1000_v4")                                                                                                        
#samples.append("QCDHT2000toInf_extv4")
#samples.append("QCDHT1500to2000_v4")                                                                               #     #       # 
#samples.append("QCD_HT700to1000_extv4")
#samples.append("QCD_HT500to700_v4")                                                                              
#samples.append("QCD_HT500to700_extv4")  
#samples.append("QCD_HT300to500_v4")                                                                                                          
#samples.append("QCD_HT300to500_extv4") 

#samples.append("QCD_HT300to500")                                                                                                                                    
#samples.append("QCD_HT200to300")                                                                                                                                     
#samples.append("QCD_HT100to200")

#samples.append("BprimeBprime800")
#samples.append("BprimeBprime1000")
#samples.append("BprimeBprime1200")
#samples.append("BprimeBprime1400")
#samples.append("BprimeBprime1600")
#samples.append("BprimeBprime1800")

#samples.append("BprimeBToHB800")
#samples.append("BprimeBToHB1000")
#samples.append("BprimeBToHB1200")
#samples.append("BprimeBToHB1400")
#samples.append("BprimeBToHB1600")
#samples.append("BprimeBToHB1800")

#samples.append("BprimeBToHB1200")                                                                                            #                                       
#samples.append("BprimeBToHB1000_v2")                                                                                                            #           
#samples.append("BprimeBToHB1000")                                                                                 
#samples.append("BprimeBToHB1200_v2")                                                                                                                                 
#samples.append("BprimeBToHB1400_v4")                                                                                                                            
#samples.append("BprimeBToHB1600_v2")                                                                                                                                  
#samples.append("BprimeBToHB1600")                                                                                                                                   
#samples.append("BprimeBToHB1700")                                                                                                                                 
#samples.append("BprimeBToHB1800_v2")                                                                                                                               #
#samples.append("JetHT_runB")
#samples.append("JetHT_runC")
#samples.append("JetHT_runD")
#samples.append("JetHT_runE")
#samples.append("JetHT_runF")
##samples.append()
#samples.append("JetHT_runG")#

splitMap = {}
splitMap["TT"] = 50
splitMap["TT_v2"] = 30
splitMap["WJets_100_200"] = 8
splitMap["WJets_200_400"] = 8
splitMap["WJets_400_600"] = 5
splitMap["WJetsHT600to800"] = 8
splitMap["WJetsHT800to1200"] = 8
splitMap["WJetsHT1200to2500"] = 8
splitMap["WJetsHT2500toInf"] = 8
splitMap["ZJets_100_200"] = 8
splitMap["ZJets_200_400"] = 8
splitMap["ZJets_400_600"] = 5
splitMap["ZJetsHT600to800"] = 8
splitMap["ZJetsHT800to1200"] = 8
splitMap["ZJetsHT1200to2500"] = 8
splitMap["ZJetsHT2500toInf"] = 8
splitMap["WJetsQQ"] = 8
splitMap["DYQQ"] = 8

#splitMap["ZJets_100_200"] = 2
#splitMap["ZJets_200_400"] = 2
#splitMap["ZJets_400_600"] = 2
#splitMap["ZJets_600_Inf"] = 2
#splitMap["QCD_HT100to200"]=10
#splitMap["QCD_HT200to300"]=10
#splitMap["QCD_HT300to500"]=10
splitMap["QCD_HT700to1000_v3"]=20
splitMap["QCDHT500to700"]=25
splitMap["QCDHT2000toInf"]=20
splitMap["QCDHT1500to2000"]=20
splitMap["QCDHT1000to1500"]=20
splitMap["QCDHT700to1000"]=20
splitMap["QCDHT300to500"]=35
splitMap["QCD_HT300to500_extv4"]=20
splitMap["QCD_HT500to700"]=10
splitMap["QCD_HT700to1000_v4"]=25
splitMap["QCD_HT1000to1500_v4"]=15
splitMap["QCDHT1500to2000_v4"]=15
splitMap["QCDHT2000toInf_v4"]=10
splitMap["QCD_HT500to700_extv4"]=15
splitMap["QCD_HT700to1000_extv4"]=20
splitMap["QCD_HT1000to1500_extv4"]=10
splitMap["QCDHT1500to2000_extv4"]=10
splitMap["QCDHT2000toInf_extv4"]=5

#splitMap["QCDHT700to1000"]=10

splitMap["SingleMub"]=20
splitMap["SingleMubv3"]=20

splitMap["SingleMud"]=20
splitMap["SingleMuc"]=20
splitMap["SingleMue"]=20
splitMap["SingleMuf"]=20
splitMap["SingleMug"]=20
splitMap["SingleMuhv1"]=20
splitMap["SingleMuhv2"]=20
splitMap["SingleMuhv3"]=20

splitMap["JetHT_runB"]=35
splitMap["JetHT_runC"]=25
splitMap["JetHT_runD"]=25
splitMap["JetHT_runE"]=25
splitMap["JetHT_runF"]=35
splitMap["JetHT_runG"]=25
splitMap["JetHT_runHv2"]=35
splitMap["JetHT_runHv3"]=25

#splitMap["JetHT_16Dec"]=30

def makedirs(subdirs,base=None):

    # Calculate the full path
    if base is not None:
        subdirs = [ join(base,sd) for sd in subdirs]

    # Loop over subdirs
    for sd in subdirs:
        # Check for existence
        if exists(sd): continue
        # Make directory and partents
        os.makedirs(sd)

def writeFileList(sample, files, opt):
    # Save it to a semi-temp file
    sampleFileList = join(fileListDir,sample+'_'+opt.channel+'_'+opt.cat+'_'+opt.sys+'.txt')
    print 'File list:',sampleFileList
    with open(sampleFileList,'w') as sl:
        sl.write('\n'.join(files))

    return sampleFileList

def run(sample, cmd, opt):

    print hline
    if opt.gdb:
        cmd = 'gdb --args '+cmd
    elif opt.t3batch:
        jid = '%s_%s_%s_%s' % (sample,opt.channel,opt.cat,opt.sys)
        cmd = 'qexe.py -w '+workDir+' '+jid+' -- '+cmd
    print cmd

    if opt.dryrun:
        print 'Dry Run (command will not be executed)'
        return

    subprocess.call(cmd,shell=True)


channels = ['singleH','fullhadronic']
systematics = ["noSys", "jesUp", "jesDown", "jerUp", "jerDown", "jmsUp", "jmsDown", "jmrUp", "jmrDown"]

usage = 'usage: %prog'
parser = optparse.OptionParser(usage)

parser.add_option('-c', '--channel', dest='channel', default='singleH', choices=channels, help='Channel to analyze: singleH or fullhadronic')
parser.add_option('-C', '--cat', dest='cat', type='string', default = 'cat_inclusive', help='Category to analyze: cat0 or cat1 or cat2')
parser.add_option('-s', '--sys', dest='sys', default = 'noSys', choices=systematics, help='Systematics: '+' '.join(systematics))
parser.add_option('--sync', dest='sync', type='string', default = 'noSync', help='Synchro exercise')
parser.add_option('-g','--gdb', dest='gdb', action='store_true', default=False)
parser.add_option('-n','--dryrun', dest='dryrun', action='store_true', default=False)
parser.add_option('-m','--mode', dest='mode', default='t3se', choices=['local','t3se'])
parser.add_option('--t3batch', dest='t3batch', action='store_true', default=False)

isData="MC"
#isData="DATA"
(opt, args) = parser.parse_args()

if opt.sys not in systematics:
    parser.error('Please choose an allowed value for sys: "noSys", "jesUp", "jesDown", "jerUp", "jerDown", "jmsUp", "jmsDown", "jmrUp", "jmrDown"')


# Create working area if it doesn't exist
if not exists(fileListDir):
    os.makedirs(fileListDir)
    

for s in samples:
    if (s.startswith("JetHT") or s.startswith("SingleMu") or s.startswith("SingleEl") or  s.startswith("MET")): isData="DATA"
    print s
    print str(opt.sync)
    ## cmd = "ttDManalysis "+ s + " " + path + s  + " " + opt.channel + " " + opt.sys + " " + opt.sync + " " + isData
    ## print cmd
    ## os.system(cmd)

    if opt.mode == 'local':
        sPath = join(localPath,s,'*.root')
        
        print sPath
        # print ' '.join([lLs,sPath])
        # Get the complete list of files
        # listing = subprocess.check_output(lLs.split()+[sPath])
        allFiles = glob.glob(sPath)
        print 'Sample',s,'Files found',len(allFiles)

    elif opt.mode == 't3se':
        # Build the full path of sample files
        sT3Path = join(t3Path,s)
        print ' '.join([t3Ls,sT3Path])

        # Get the complete list of files
        listing = subprocess.check_output(t3Ls.split()+[sT3Path])
        allFiles = listing.split()
        print 'Sample',s,'Files found',len(allFiles)



    if not (s in splitMap and opt.t3batch):

        if not opt.t3batch:
            print 'WARNING: Batch mode not active: Sample',s,'will not be split even if it appears in the splitMap'

        # Save it to a semi-temp file
        sampleFileList = join(fileListDir,s+'_'+opt.channel+'_'+opt.cat+'_'+opt.sys+'.txt')
        print 'File list:',sampleFileList
        with open(sampleFileList,'w') as sl:
            sl.write('\n'.join(allFiles))


        cwd = os.getcwd()

        makedirs(resDirs,cwd)
        print 'ciao'
        cmd = 'BprimeAnalysis '+ s + ' ' + sampleFileList  + ' ' + opt.channel + ' ' + opt.cat + ' ' + opt.sys + ' ' + opt.sync + ' ' + isData + ' ' +  cwd
        
        run(s,cmd,opt)

    else:

        # 
        nsplit = splitMap[s]

        if len(allFiles) < nsplit:
            nsplit = len(allFiles)
            print 'Warning: split level larger than number of files. Splitlevel set to nfiles (',nsplit,')'

        # Pretty format
        ndigits = int(math.floor(math.log10(nsplit))+1)
        nfmt = '%%s_%%s_%%s_j%%0%dd' % ndigits

        # Calculate the size of each file block
        chunkSize = len(allFiles)/nsplit
        # The reminder is the number of jobs that get one file more
        nExtra = len(allFiles)%nsplit

        print ' * Split level',nsplit
        print ' * Files per job (base):',chunkSize
        print ' * Jobs with 1 extra file:',nExtra

        resRootDir = join(splitDir,'%s_%s_%s_%s' % (s,opt.channel,opt.cat,opt.sys))

        print ' * Result root folder',resRootDir

        subsamples = {}
        lastFileIdx = 0
        for k in xrange(nsplit):
            name = nfmt % (s,opt.channel,opt.sys,k)
            wd = join(resRootDir,name)
            # Start from last idx
            firstFileIdx = lastFileIdx
            # add chunk size. add 1 if k<nExtra
            lastFileIdx = firstFileIdx+chunkSize+(k<nExtra)
            files = allFiles[firstFileIdx:lastFileIdx]

            subsamples[name] = (wd,files)

        # Cleanup previous result areas
        if exists(resRootDir):
            print 'Cleaning directory',resRootDir
            shutil.rmtree(resRootDir)

        # Recreate the target directory
        os.makedirs(resRootDir)

        ssDesc = { 'sample':s, 'components': subsamples.keys() }
        pickle.dump(ssDesc, open(join(resRootDir,splitDescriptionFile),'w') )

        for ss in sorted(subsamples):
            # Fetch output directory and file list
            wd,files = subsamples[ss]
            # Make the subdirectories
            makedirs(resDirs,wd)

            sampleFileList = writeFileList(ss, files,opt)

            cmd = 'BprimeAnalysis '+ s + ' ' + sampleFileList  + ' ' + opt.channel + ' ' + opt.cat + ' ' + opt.sys + ' ' + opt.sync + ' ' + isData + ' ' +  wd

            run(ss,cmd,opt)
