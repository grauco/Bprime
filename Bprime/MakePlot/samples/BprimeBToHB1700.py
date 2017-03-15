from utils import *

BprimeBToHB1700 = sample()
BprimeBToHB1700.files = outlist (d,"BprimeBToHB1700")
BprimeBToHB1700.skimEff = 1.
#BprimeBToHB1700.sigma = 1.
BprimeBToHB1700.sigma = 0.249 * 0.25
BprimeBToHB1700.jpref = jetLabel
BprimeBToHB1700.jp = jetLabel
BprimeBToHB1700.color =  ROOT.kRed
BprimeBToHB1700.style = 1
BprimeBToHB1700.fill = 0
BprimeBToHB1700.leglabel = "B'(1700 GeV)"
BprimeBToHB1700.label = "BprimeBToHB1700"
