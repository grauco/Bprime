import sys
sys.argv.append('-b')
import ROOT
import array

ROOT.gROOT.Reset();
ROOT.gROOT.SetStyle('Plain')
ROOT.gROOT.SetBatch()  # don't pop up canvases


### INSTRUCTIONS
### Use this scripts to create root files containing histograms with weghts
### depending on eta and pt. To use it, please, check the Eta and Pt ranges definition.
### Set the name of the histo.
### Set the values in effArray, it is an array of arrays.


names = [ "EleIDEffTight"] 
#"MuIDEffTight", "EleIDEffLoose", "Ele8TriggerEff", "Ele17TriggerEff" ]

### ******* El ID eff: data/MC SF *******
### *************************************
name_EleWPTight = "EleIDEffTight"

arrayEta_EleWPTight  = array.array("f", [-2.5, -1.566, -1.4442, -0.8, -0.0, 0.8, 1.4442, 1.566, 2.5]) # Define eta and Pt ranges
arrayPt_EleWPTight = array.array("f", [10, 20, 30, 40, 50, 1000])

#Range di Pt            [10-20, 20-30, 30-40, 40-50, 50-1000]         
effArray_EleWPTight = [
                        [1.05, 0.98, 0.97, 0.99, 0.98],   # -2.5   < eta < -1.566  
                        [0.95, 1.04, 1.01, 0.94, 0.92],   # -1.566 < eta < 1.442
                        [1.02, 0.91, 0.97, 0.98, 0.96],   # -1.442 < eta < -0.8
                        [1.01, 0.95, 0.95, 0.97, 0.97],   # -0.8   < eta < 0.0
                        [1.01, 0.99, 0.97, 0.97, 0.99],   # 0.0    < eta < 0.8
                        [1.16, 0.99, 0.95, 0.98, 0.97],   # 0.8    < eta < 1.442
                        [0.99, 0.97, 0.98, 0.96, 1.04],   # 1.442    < eta < 1.566
                        [1.06, 0.95, 0.96, 0.99, 0.99]    # 1.566    < eta < 2.5
                      ]

errArray_EleWPTight = [
                        [0.06, 0.02, 0.01, 0.01, 0.02],   #2.5   < eta < -1.566  
                        [0.23, 0.06, 0.03, 0.02, 0.05],   # -1.566 < eta < 1.442
                        [0.09, 0.02, 0.01, 0.01, 0.01],   # -1.442 < eta < -0.8
                        [0.06, 0.02, 0.27, 0.01, 0.01],   # -0.8   < eta < 0.0
                        [0.06, 0.02, 0.01, 0.01, 0.01],   # 0.0    < eta < 0.8
                        [0.09, 0.02, 0.01, 0.01, 0.01],   # 0.8    < eta < 1.442
                        [0.24, 0.06, 0.03, 0.03, 0.06],   # 1.442    < eta < 1.566
                        [0.06, 0.02, 0.01, 0.01, 0.02]    # 1.566    < eta < 2.5
                      ]

### ******* Mu ID eff: data/MC SF *******
### *************************************
#name_MuWPTight = "MuIDEffTight"

#arrayEta_MuWPTight  = array.array("f", [0.00, 0.80, 2.10, 2.40]) # Define eta and Pt ranges
#arrayPt_MuWPTight = array.array("f", [20, 40, 100])

#Range di Pt            [20-40, 40-100]         
#effArray_MuWPTight = [
#                        [1.00425, 1.00119],   # 0.00 < eta < 0.80  
#                        [1.00740, 1.00425],   # 0.80 < eta < 2.10 
#                        [1.02159, 1.01404]   # 2.10 < eta < 2.40
#                      ]

#errArray_MuWPTight = [
#                        [0.00042, 0.00039],   # 0.00 < eta < 0.80  
#                        [0.00046, 0.00039],   # 0.80 < eta < 2.10 
#                        [0.00142, 0.00141]   # 2.10 < eta < 2.40
#                      ]


### ******* Ele8 trigger eff *******
### *******************************
#name_EleTrig8 = "Ele8TriggerEff"

### Define eta and Pt ranges

#arrayEta_EleTrig8  = array.array("f", [0.00, 0.80, 1.4442, 1.566, 2.00, 2.50])
#arrayPt_EleTrig8 = array.array("f", [10, 20, 40, 200])

#Range di Pt       [10-20, 20-40, 40-200]         
#effArray_EleTrig8 = [
#                      [0.9545, 0.9830, 0.9889],   # 0.00 < eta < 0.80  
#                      [0.8521, 0.9316, 0.9715],   # 0.80 < eta < 1.44 
#                      [1.,1.,1.],                 # 1.44 < eta < 1.55
#                      [0.8387, 0.8948, 0.9380],   # 1.56 < eta < 2.00
#                      [0.8677, 0.9331, 0.9508]    # 2.00 < eta < 2.50
#                    ]

#errArray_EleTrig8 = [
#                      [0.0038, 0.0005, 0.0004],   # 0.00 < eta < 0.80  
#                      [0.0062, 0.0011, 0.0007],   # 0.80 < eta < 1.44 
#                      [0.,0.,0.],                 # 1.44 < eta < 1.55
#                      [0.0106, 0.0021, 0.0014],   # 1.55 < eta < 2.00
#                      [0.0102, 0.0019, 0.0016]    # 2.00 < eta < 2.50
#                    ]

### ******* Ele17 trigger eff *******
### *********************************
#name_EleTrig17 = "Ele17TriggerEff"

### Define eta and Pt ranges

#arrayEta_EleTrig17  = array.array("f", [0.00, 0.80, 1.4442, 1.566, 2.00, 2.50])
#arrayPt_EleTrig17 = array.array("f", [10, 20, 40, 200])

#Range di Pt       [10-20, 20-40, 40-200]         
#effArray_EleTrig17 = [
#                       [0.4735, 0.9856, 0.9913],   # 0.00 < eta < 0.80  
#                       [0.3426, 0.9360, 0.9763],   # 0.80 < eta < 1.44 
#                       [1.,1.,1.],                 # 1.44 < eta < 1.56
#                       [0.4439, 0.9006, 0.9447],   # 1.56 < eta < 2.00
#                       [0.4519, 0.9444, 0.9624]    # 2.00 < eta < 2.50
#                     ]

#errArray_EleTrig17 = [
#                       [0.0089, 0.0004, 0.0003],   # 0.00 < eta < 0.80  
#                       [0.0082, 0.0011, 0.0006],   # 0.80 < eta < 1.44 
#                       [0.,0.,0.],                 # 1.44 < eta < 1.55
#                       [0.0142, 0.0020, 0.0014],   # 1.55 < eta < 2.00
#                       [0.0148, 0.0018, 0.0014]    # 2.00 < eta < 2.50
#                     ]



arraysEta = {
#    "MuIDEffTight" : arrayEta_MuWPTight,
    "EleIDEffTight" : arrayEta_EleWPTight,
#    "Ele8TriggerEff" : arrayEta_EleTrig8,
#    "Ele17TriggerEff" : arrayEta_EleTrig17,
   }

arraysPt = {
 #   "MuIDEffTight" : arrayPt_MuWPTight,
    "EleIDEffTight" : arrayPt_EleWPTight,
  #  "Ele8TriggerEff" : arrayPt_EleTrig8,
  #  "Ele17TriggerEff" : arrayPt_EleTrig17,
   }

effArrays = {
   # "MuIDEffTight" : effArray_MuWPTight,
    "EleIDEffTight" : effArray_EleWPTight,
   # "Ele8TriggerEff" : effArray_EleTrig8,
   # "Ele17TriggerEff" : effArray_EleTrig17,
   }

errArrays = {
   # "MuIDEffTight" : errArray_MuWPTight,
    "EleIDEffTight" : errArray_EleWPTight,
   # "Ele8TriggerEff" : errArray_EleTrig8,
   # "Ele17TriggerEff" : errArray_EleTrig17,
   }



#wfile = ROOT.TFile.Open("Weights.root", "UPDATE")
wfile = ROOT.TFile.Open("Weights.root", "RECREATE")

for name in names:

    print name
    print len(arraysEta[name])-1
    print arraysEta[name]
    print len(arraysPt[name])-1
    print arraysPt[name]
    
    title = name
    histoEff = ROOT.TH2F(name, title, len(arraysEta[name])-1, arraysEta[name], len(arraysPt[name])-1, arraysPt[name])

    for iEta, values in enumerate(effArrays[name]):
        [histoEff.SetBinContent(iEta+1, iPt+1, weight) for iPt, weight in enumerate(values)]
        print iEta, values
        print iPt, weight
    for iEta, values in enumerate(errArrays[name]):
        [histoEff.SetBinError(iEta+1, iPt+1, weight) for iPt, weight in enumerate(values)]
    histoEff.Write()
    
#    histoEff = ROOT.TH2F(name, title, len(arrayEta)-1, arrayEta, len(arrayPt)-1, arrayPt)
#
#    for iEta, values in enumerate(effArray):
#        [histoEff.SetBinContent(iEta+1, iPt+1, weight) for iPt, weight in enumerate(values)]

#wfile.Write()
wfile.Close()
