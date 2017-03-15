######################################
#
# Deborah Pinna, August 2015
#
######################################


from utils import *

JetHTbv3 = sample()
JetHTbv3.files = outlist (d,"JetHTbv3")
JetHTbv3.skimEff = 1
JetHTbv3.sigma = 1
JetHTbv3.color = ROOT.kBlack
JetHTbv3.jpref = jetLabel 
JetHTbv3.jp = jetLabel
JetHTbv3.style = 1
JetHTbv3.fill = 1001
JetHTbv3.leglabel = "JetHTbv3"
JetHTbv3.label = "JetHTbv3"

JetHTc = sample()
JetHTc.files = outlist (d,"JetHTc")
JetHTc.skimEff = 1
JetHTc.sigma = 1
JetHTc.color = ROOT.kBlack
JetHTc.jpref = jetLabel
JetHTc.jp = jetLabel
JetHTc.style = 1
JetHTc.fill = 1001
JetHTc.leglabel = "JetHTc"
JetHTc.label = "JetHTc"

JetHT_runD = sample()
JetHT_runD.files = outlist (d,"JetHT_runD")
JetHT_runD.skimEff = 1
JetHT_runD.sigma = 1
JetHT_runD.color = ROOT.kBlack
JetHT_runD.jpref = jetLabel
JetHT_runD.jp = jetLabel
JetHT_runD.style = 1
JetHT_runD.fill = 1001
JetHT_runD.leglabel = "JetHT_runD"
JetHT_runD.label = "JetHT_runD"


JetHTe = sample()
JetHTe.files = outlist (d,"JetHTe")
JetHTe.skimEff = 1
JetHTe.sigma = 1
JetHTe.color = ROOT.kBlack
JetHTe.jpref = jetLabel
JetHTe.jp = jetLabel
JetHTe.style = 1
JetHTe.fill = 1001
JetHTe.leglabel = "JetHTe"
JetHTe.label = "JetHTe"

JetHTf = sample()
JetHTf.files = outlist (d,"JetHTf")
JetHTf.skimEff = 1
JetHTf.sigma = 1
JetHTf.color = ROOT.kBlack
JetHTf.jpref = jetLabel
JetHTf.jp = jetLabel
JetHTf.style = 1
JetHTf.fill = 1001
JetHTf.leglabel = "JetHTf"
JetHTf.label = "JetHTf"

JetHThv2 = sample()
JetHThv2.files = outlist (d,"JetHThv2")
JetHThv2.skimEff = 1
JetHThv2.sigma = 1
JetHThv2.color = ROOT.kBlack
JetHThv2.jpref = jetLabel
JetHThv2.jp = jetLabel
JetHThv2.style = 1
JetHThv2.fill = 1001
JetHThv2.leglabel = "JetHThv2"
JetHThv2.label = "JetHThv2"


JetHThv3 = sample()
JetHThv3.files = outlist (d,"JetHThv3")
JetHThv3.skimEff = 1
JetHThv3.sigma = 1
JetHThv3.color = ROOT.kBlack
JetHThv3.jpref = jetLabel
JetHThv3.jp = jetLabel
JetHThv3.style = 1
JetHThv3.fill = 1001
JetHThv3.leglabel = "JetHThv3"
JetHThv3.label = "JetHThv3"


Data = sample()
Data.color = ROOT.kBlack
Data.style = 1
Data.fill = 1001
Data.leglabel = "Data"
Data.label = "Data"
#Data.components = [JetHT_runC]
#Data.components = [SingleMu_05Oct, SingleEl_05Oct, JetHT_05Oct, JetHT_Promptv4]
Data.components = [JetHTbv3, JetHTc, JetHTf, JetHTe, JetHThv2, JetHThv3]



