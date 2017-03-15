from utils import *

BprimeBToHB1500 = sample()
BprimeBToHB1500.files = outlist (d,"BprimeBToHB1500")
BprimeBToHB1500.skimEff = 1.
BprimeBToHB1500.sigma = 0.415 * 0.25
#BprimeBToHB1500.sigma = 1.
BprimeBToHB1500.jpref = jetLabel
BprimeBToHB1500.jp = jetLabel
BprimeBToHB1500.color =  ROOT.kRed
BprimeBToHB1500.style = 1
BprimeBToHB1500.fill = 0
BprimeBToHB1500.leglabel = "B'(1500 GeV)"
BprimeBToHB1500.label = "BprimeBToHB1500"
