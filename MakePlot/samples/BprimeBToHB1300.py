from utils import *

BprimeBToHB1300 = sample()
BprimeBToHB1300.files = outlist (d,"BprimeBToHB1300")
BprimeBToHB1300.skimEff = 1.
#BprimeBToHB1300.sigma = 1.
BprimeBToHB1300.sigma = 0.679 * 0.25
BprimeBToHB1300.jpref = jetLabel
BprimeBToHB1300.jp = jetLabel
BprimeBToHB1300.color =  ROOT.kRed
BprimeBToHB1300.style = 1
BprimeBToHB1300.fill = 0
BprimeBToHB1300.leglabel = "B'(1300 GeV)"
BprimeBToHB1300.label = "BprimeBToHB1300"
