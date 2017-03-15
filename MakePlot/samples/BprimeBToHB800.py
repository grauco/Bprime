from utils import *

BprimeBToHB800 = sample()
BprimeBToHB800.files = outlist (d,"BprimeBToHB800")
BprimeBToHB800.skimEff = 1.
BprimeBToHB800.sigma = 3.016 * 0.5
#BprimeBToHB800.sigma = 1.
BprimeBToHB800.jpref = jetLabel 
BprimeBToHB800.jp = jetLabel 
BprimeBToHB800.color =  ROOT.kRed
BprimeBToHB800.style = 1
BprimeBToHB800.fill = 0
BprimeBToHB800.leglabel = "B'(800 GeV)"
BprimeBToHB800.label = "BprimeBToHB800"
