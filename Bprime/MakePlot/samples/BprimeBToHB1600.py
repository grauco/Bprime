from utils import *

BprimeBToHB1600 = sample()
BprimeBToHB1600.files = outlist (d,"BprimeBToHB1600")
BprimeBToHB1600.skimEff = 1.
#BprimeBToHB1600.sigma = 1.
BprimeBToHB1600.sigma = 0.319 * 0.25
BprimeBToHB1600.jpref = jetLabel
BprimeBToHB1600.jp = jetLabel
BprimeBToHB1600.color =  ROOT.kRed
BprimeBToHB1600.style = 1
BprimeBToHB1600.fill = 0
BprimeBToHB1600.leglabel = "B'(1600 GeV)"
BprimeBToHB1600.label = "BprimeBToHB1600"
