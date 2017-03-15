######################################
#
# Annapaola de Cosa, January 2015
#
######################################

import ROOT
import collections
import os, commands
#from SingleTopWJets import *
#from ttDM import *
#from TT import *
#from DYJetsToLL import *
#from ZJets import *
#from WJets import *
from QCD import *
#from Data import *
#from otherBkg import *
from BprimeBToHB800 import*
#from BprimeBToHB1800 import*
#from BprimeBToHB1200 import*
samples = collections.OrderedDict()

#samples["MET_Prompt"] = MET_Prompt
#samples["MET_ReMiniAOD"] = MET_ReMiniAOD17Jul
#samples["SingleMu_MiniAOD17Jul"] = SingleMu_MiniAOD17Jul
#samples["SingleMu_Prompt"] = SingleMu_Prompt
#samples["SingleEl_MiniAOD17Jul"] = SingleEl_MiniAOD17Jul
#samples["SingleEl_Prompt"] = SingleEl_Prompt
#samples["Data"] = Data
#samples["TT"] = TT
#samples["DY"] = DY
#samples["ZJets"] = ZJets
#samples["SingleTop"] = SingleTop
samples["QCD"] = QCD
#samples["WJets"] = WJets
#samples["TT"]=TT
#samples["otherBkg"] = otherBkg
#samples["Data"]=Data
samples["BprimeBToHB800"] = BprimeBToHB800
#samples["BprimeBToHB1800"] = BprimeBToHB1800
#samples["BprimeToHB1200"] = BprimeToHB1200
#samples["DMtt_sc_Mchi1Mphi10"] = DMtt_sc_Mchi1Mphi10
#samples["DMtt_sc_Mchi10Mphi10"] = DMtt_sc_Mchi10Mphi10

#samples["DMtt_sc_Mchi1Mphi20"] = DMtt_sc_Mchi1Mphi20

#samples["DMtt_sc_Mchi10Mphi50"] = DMtt_sc_Mchi10Mphi50
#samples["DMtt_sc_Mchi50Mphi50"] = DMtt_sc_Mchi50Mphi50

#samples["DMtt_sc_Mchi1Mphi100"] = DMtt_sc_Mchi1Mphi100
#samples["DMtt_sc_Mchi10Mphi100"] = DMtt_sc_Mchi10Mphi100

#samples["DMtt_sc_Mchi1Mphi200"] = DMtt_sc_Mchi1Mphi200
#samples["DMtt_sc_Mchi50Mphi200"] = DMtt_sc_Mchi50Mphi200
#samples["DMtt_sc_Mchi150Mphi200"] = DMtt_sc_Mchi150Mphi200

#samples["DMtt_sc_Mchi1Mphi300"] = DMtt_sc_Mchi1Mphi300
#samples["DMtt_sc_Mchi50Mphi300"] = DMtt_sc_Mchi50Mphi300

#samples["DMtt_sc_Mchi1Mphi500"] = DMtt_sc_Mchi1Mphi500
#samples["DMtt_sc_Mchi500Mphi500"] = DMtt_sc_Mchi500Mphi500

#samples["DMtt_sc_Mchi1Mphi1000"] = DMtt_sc_Mchi1Mphi1000


#samples["DMtt_ps_Mchi1Mphi10"] = DMtt_ps_Mchi1Mphi10
#samples["DMtt_ps_Mchi10Mphi10"] = DMtt_ps_Mchi10Mphi10

#samples["DMtt_ps_Mchi1Mphi20"] = DMtt_ps_Mchi1Mphi20

#samples["DMtt_ps_Mchi1Mphi50"] = DMtt_ps_Mchi1Mphi50
#samples["DMtt_ps_Mchi10Mphi50"] = DMtt_ps_Mchi10Mphi50
#samples["DMtt_ps_Mchi50Mphi50"] = DMtt_ps_Mchi50Mphi50

#samples["DMtt_ps_Mchi1Mphi100"] = DMtt_ps_Mchi1Mphi100
#samples["DMtt_ps_Mchi10Mphi100"] = DMtt_ps_Mchi10Mphi50

#samples["DMtt_ps_Mchi1Mphi200"] = DMtt_ps_Mchi1Mphi200
#samples["DMtt_ps_Mchi50Mphi200"] = DMtt_ps_Mchi50Mphi200
#samples["DMtt_ps_Mchi150Mphi200"] = DMtt_ps_Mchi150Mphi200

#samples["DMtt_ps_Mchi1Mphi300"] = DMtt_ps_Mchi1Mphi300
#samples["DMtt_ps_Mchi50Mphi300"] = DMtt_ps_Mchi50Mphi300

#samples["DMtt_ps_Mchi1Mphi500"] = DMtt_ps_Mchi1Mphi500
#samples["DMtt_ps_Mchi150Mphi500"] = DMtt_ps_Mchi150Mphi500
#samples["DMtt_ps_Mchi500Mphi500"] = DMtt_ps_Mchi500Mphi500


