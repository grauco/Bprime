from utils import *

BprimeBToHB1400 = sample()
BprimeBToHB1400.files = outlist (d,"BprimeBToHB1400")
BprimeBToHB1400.skimEff = 1
#BprimeBToHB1400.sigma = 1.
BprimeBToHB1400.sigma = 0.529 * 0.25
BprimeBToHB1400.jpref = jetLabel
BprimeBToHB1400.jp = jetLabel
BprimeBToHB1400.color =  ROOT.kRed
BprimeBToHB1400.style = 1
BprimeBToHB1400.fill = 0
BprimeBToHB1400.leglabel = "B'(1400 GeV)"
BprimeBToHB1400.label = "BprimeBToHB1400"
