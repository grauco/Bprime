from utils import *

WJetsQQ = sample()
WJetsQQ.files = outlist (d,"WJetsQQ")
WJetsQQ.files = WJetsQQ.files[:1]
WJetsQQ.jpref = jetLabel 
WJetsQQ.jp = jetLabel 
WJetsQQ.skimEff = 1.21
WJetsQQ.sigma = 95.14 
#WJetsQQ.color = 9
WJetsQQ.color = ROOT.kAzure - 9
WJetsQQ.style = 1
WJetsQQ.fill = 1001
WJetsQQ.leglabel = "W(qq)"
WJetsQQ.label = "WJetsQQ"

