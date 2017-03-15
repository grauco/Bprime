from utils import *

BprimeBToHB1200 = sample()
BprimeBToHB1200.files = outlist (d,"BprimeBToHB1200")
BprimeBToHB1200.skimEff = 1.
BprimeBToHB1200.sigma = 0.896 * 0.25
#BprimeBToHB1200.sigma = 1.
BprimeBToHB1200.jpref = jetLabel
BprimeBToHB1200.jp = jetLabel
BprimeBToHB1200.color =  ROOT.kRed
BprimeBToHB1200.style = 1
BprimeBToHB1200.fill = 0
BprimeBToHB1200.leglabel = "B'(1200 GeV)"
BprimeBToHB1200.label = "BprimeBToHB1200"
