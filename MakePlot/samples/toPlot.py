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
from TT import *
from DYQQ import *
from WJetsQQ import *
from ZJets import *
from WJets import *
from QCD import *
from Data import *
#from QCDTT_v2 import *
#from otherBkg import *
#from BprimeBToHB import*
from BprimeBToHB1000 import*
#from BprimeBToHB800 import*
from BprimeBToHB900 import*
from BprimeBToHB1000 import*
from BprimeBToHB1100 import*
from BprimeBToHB1200 import*
#from BprimeBToHB1300 import*
from BprimeBToHB1400 import*
from BprimeBToHB1500 import*
from BprimeBToHB1600 import*
from BprimeBToHB1700 import*
from BprimeBToHB1800 import*
#from BprimeBToHB1800_v2 import*
samples = collections.OrderedDict()

#samples["MET_Prompt"] = MET_Prompt
#samples["MET_ReMiniAOD"] = MET_ReMiniAOD17Jul
#samples["SingleMu_MiniAOD17Jul"] = SingleMu_MiniAOD17Jul
#samples["SingleMu_Prompt"] = SingleMu_Prompt
#samples["SingleEl_MiniAOD17Jul"] = SingleEl_MiniAOD17Jul
#samples["SingleEl_Prompt"] = SingleEl_Prompt
#samples["BprimeBToHB800"] = BprimeBToHB800
#samples["BprimeBToHB1800"] = BprimeBToHB1800

samples["Data"] = Data
#samples["QCDTT_v2"] = QCDTT_v2
#samples["BprimeBToHB700"] = BprimeBToHB700
#samples["BprimeBToHB800_v2"] = BprimeBToHB800_v2                                                                                          
samples["BprimeBToHB900"] = BprimeBToHB900
#samples["BprimeBToHB1000_v2"] = BprimeBToHB1000_v2
samples["BprimeBToHB1000"] = BprimeBToHB1000
#samples["BprimeBToHB1200_v2"] = BprimeBToHB1200_v2
samples["BprimeBToHB1100"] = BprimeBToHB1100
samples["BprimeBToHB1200"] = BprimeBToHB1200
samples["BprimeBToHB1400"] = BprimeBToHB1400
samples["BprimeBToHB1500"] = BprimeBToHB1500
samples["BprimeBToHB1600"] = BprimeBToHB1600
samples["BprimeBToHB1700"] = BprimeBToHB1700
samples["BprimeBToHB1800"] = BprimeBToHB1800
#samples["BprimeBToHB1800_v2"] = BprimeBToHB1800_v2
samples["ZJets"] = ZJets
samples["WJets"] = WJets
samples["WJetsQQ"] = WJetsQQ
samples["DYQQ"] = DYQQ
samples["TT"]=TT
samples["QCD"] = QCD

#samples["BprimeBToHB800"] = BprimeBToHB800
#samples["BprimeBToHB1800"] = BprimeBToHB1800
#samples["BprimeBToHB1800"] = BprimeBToHB1800
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


