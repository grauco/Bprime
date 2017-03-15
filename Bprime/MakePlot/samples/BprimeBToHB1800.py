from utils import *

BprimeBToHB1800 = sample()
BprimeBToHB1800.files = outlist (d,"BprimeBToHB1800")
BprimeBToHB1800.skimEff = 1.
BprimeBToHB1800.sigma = 0.195 * 0.25
#BprimeBToHB1800.sigma = 1.
BprimeBToHB1800.jpref = jetLabel
BprimeBToHB1800.jp = jetLabel
BprimeBToHB1800.color =  ROOT.kRed
BprimeBToHB1800.style = 2
BprimeBToHB1800.fill = 0
BprimeBToHB1800.leglabel = "B'(1800 GeV)"
BprimeBToHB1800.label = "BprimeBToHB1800"
