from utils import *

BprimeBToHB1000 = sample()
BprimeBToHB1000.files = outlist (d,"BprimeBToHB1000")
BprimeBToHB1000.skimEff = 1.
BprimeBToHB1000.sigma = 1.653 * 0.25
#BprimeBToHB1000.sigma = 1.
BprimeBToHB1000.jpref = jetLabel
BprimeBToHB1000.jp = jetLabel
BprimeBToHB1000.color =  ROOT.kRed 
BprimeBToHB1000.style = 1
BprimeBToHB1000.fill = 0
BprimeBToHB1000.leglabel = "B'(1000 GeV)"
BprimeBToHB1000.label = "BprimeBToHB1000"
