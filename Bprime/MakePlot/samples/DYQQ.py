from utils import *

DYQQ = sample()
DYQQ.files = outlist (d,"DYQQ")
DYQQ.files = DYQQ.files[:1]
DYQQ.jpref = jetLabel 
DYQQ.jp = jetLabel 
DYQQ.skimEff = 1.23
DYQQ.sigma = 1187
#DYQQ.color = 9
DYQQ.color = ROOT.kGreen - 8
DYQQ.style = 1
DYQQ.fill = 1001
DYQQ.leglabel = "DY(qq)"
DYQQ.label = "DYQQ"

