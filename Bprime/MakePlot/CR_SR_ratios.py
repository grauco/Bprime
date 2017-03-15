 #!/usr/bin/env python


######################################
#                                    #
# Deborah Pinna, May 2015            #
# dpinna@cern.ch                     #
#                                    #
######################################

import time
import sys
#sys.argv.append('-b')
import ROOT
import copy
import commands, os
import numpy as n
from services_ratio import Histo, Stack, Legend, deltaPhi, Histo1
from samples.toPlot_bkg import samples
import optparse 

import tdrstyle, CMS_lumi

ROOT.gROOT.Reset();
ROOT.gROOT.SetStyle('Plain')
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.TH1.SetDefaultSumw2()
ROOT.TH1.AddDirectory(False)

tdrstyle.setTDRStyle();

usage = 'usage: %prog -l lumi'
parser = optparse.OptionParser(usage)
parser.add_option('-l', '--lumi', dest='lumi', type='float', default = '2.666', help='Luminosity')
parser.add_option('-c', '--channel', dest='channel', type='string', default = 'singleH', help='Channel to analyze: semileptonic or fullhadronic')
parser.add_option('-C', '--category', dest='category', type='string', default = 'cat2', help='category')
parser.add_option('-s', '--sys', dest='sys', type='string', default = 'noSys', help='Systematics: noSys, jesUp, jesDown')

(opt, args) = parser.parse_args()

rebin = {"h_bprimemass":1}
scale =  {"h_bprimemass": 1 }

vars = {"h_bprimemass_c":"HT (GeV)"}

sample_name = [ "BprimeBToHB800", "QCD"]
legend_name = ["BprimeBToHB800", "QCD"]
#legend_name = ["QCD", "W+jets","t#bar{t}", "m(B')=800GeV", "m(B')=1500GeV"]  

plotsToStore = ["h_bprimemass"]    
histoSig = {}

def writeSummary(label, channel, h, lumi,region, var):
    filename = 'yields/'+region+label + "_"+var+"_"+channel+".txt"
    ofile = open( filename, 'w')
    #print "Opening file: ", filename
    ofile.write("Lumi: %.1f\n"%(lumi))
    ofile.write("---> %s\n"%(label))
    ofile.write("Events: %.2f\n" %(h.Integral()) )

def DrawStatBox(d, s, x, y, size):
    #text = ROOT.TLatex(x, y, ("KS = %.3f,  #chi^{2}/ndf = %.1f/%d" %( d.KolmogorovTest(s, "UO"), d.Chi2Test(s, "WW, CHI2"), d.GetNbinsX()-2)))
    text = ROOT.TLatex(x, y, 'ciao')
    text.SetNDC()
    text.SetTextSize(size)
    text.Draw("same")
#    return text
 
histo_met = []
#histo_CR=[]
histo_metNorm = []

for s in samples.itervalues():
    nEntries = 0       
    print s.label
    if(hasattr(s, "components")):
        histo_tmp = []
        histo_tmpNorm = []
        for c in s.components:
            if(c.label.startswith("MET") and opt.channel == "semileptonic"): continue
            if((c.label.startswith("SingleMu") or c.label.startswith("SingleEl")) and opt.channel == "fullhadronic"): continue
            
            #print "c.label " , c.label
            
            if(opt.sys=="noSys"): filename = '../newTTDManalysis/res/'+c.label+"_" + opt.category + "_" + opt.channel+".root"
            else: filename = '../newTTDManalysis/res/'+c.label+"_" + opt.channel + "_" + opt.category+ "_"+ opt.sys +".root"
            
            filename_nEvt = '../newTTDManalysis/res/'+c.label+ "_" + opt.category + "_" + opt.channel +".root"
            
            infile_nEvt = ROOT.TFile.Open(filename_nEvt)
            nEntries =  infile_nEvt.Get("h_cutFlow").GetBinContent(1)
            
            #print "nEntries ", nEntries
            infile =   ROOT.TFile.Open(filename)
            htmp = infile.Get("h_bprimemass")
            htmp_norm = infile.Get("h_bprimemass")
            
            htmp.Sumw2()
            htmp_norm.Sumw2()

            #print "bin ht", htmp.GetNbinsX()

            if(htmp_norm.Integral()!=0):htmp_norm.Scale((1./nEntries) * c.skimEff * c.sigma * 1000.* float(opt.lumi) )

            htmp.Sumw2()
            htmp_norm.Sumw2()
            htmp.Rebin(2)
            htmp_norm.Rebin(2)
            histo_tmp.append(htmp)
            histo_tmpNorm.append(htmp_norm)
          
        h1 = histo_tmp[0]
        [h1.Add(hi) for hi in histo_tmp[1:]]
        h1.SetLineColor(s.color)
        h1.SetLineWidth(3)
        #h1.Rebin(2)
        h1.Rebin(2)
        histo_met.append(h1)
   

        #print "bin metfinal sum ", h1.GetNbinsX()


        h2 = histo_tmpNorm[0]
        [h2.Add(hi) for hi in histo_tmpNorm[1:]]
        h2.Rebin(2)
        histo_metNorm.append(h2)

    else: 
        if(opt.sys=="noSys"):filename = '../newTTDManalysis/res/'+s.label+"_" + opt.category +"_" + opt.channel+".root"
        else:filename = '../newTTDManalysis/res/'+s.label+"_" + opt.channel +"_" + opt.category+"_"+ opt.sys +".root"
        
        filename_nEvt = '../newTTDManalysis/res/'+s.label+"_" + opt.category +"_" + opt.channel+".root"
        
        infile_nEvt = ROOT.TFile.Open(filename_nEvt)
        nEntries =  infile_nEvt.Get("h_cutFlow").GetBinContent(1)
        #print "nEntries ", nEntries
        infile =  ROOT.TFile.Open(filename)
        htmp = ROOT.TH1F(infile.Get("h_bprimemass"))
        htmp_norm = ROOT.TH1F(infile.Get("h_bprimemass"))

        #print "bin metfinal ", htmp.GetNbinsX()

        htmp.Sumw2()
        htmp_norm.Sumw2()
        htmp.Rebin(2)
        htmp_norm.Rebin(2)

        nEntries =  infile.Get("h_cutFlow").GetBinContent(1)
        if(htmp_norm.Integral()!=0):htmp_norm.Scale((1./nEntries) * s.skimEff * s.sigma * 1000.* float(opt.lumi) )
     
        htmp.SetLineColor(s.color)
        htmp.SetLineWidth(3)
        #htmp.Rebin(2)
        #htmp_norm.Rebin(2)

        #print "bin ht sum", htmp.GetNbinsX()

        histo_met.append(htmp)
        histo_metNorm.append(htmp_norm)
        
    
for var, title in vars.iteritems():
 
    histo_CR = []
    histo_CRNorm = []

    for s in samples.itervalues():
        nEntries = 0       
        if(hasattr(s, "components")):
            histos = []
            histos_norm = []
            for c in s.components:

                if(c.label.startswith("MET") and opt.channel == "semileptonic"): continue
                if((c.label.startswith("SingleMu") or c.label.startswith("SingleEl")) and opt.channel == "fullhadronic"): continue
                
                #print "c.label " , c.label
                
                if(opt.sys=="noSys"): filename = '../newTTDManalysis/res/'+c.label+"_" + opt.category + "_" + opt.channel+".root"
                else: filename = '../newTTDManalysis/res/'+c.label+"_" + opt.channel+ "_" + opt.category + "_"+ opt.sys +".root"
                
                filename_nEvt = '../newTTDManalysis/res/'+c.label+"_" + opt.category + "_" + opt.channel+".root"
                
                infile_nEvt = ROOT.TFile.Open(filename_nEvt)
                nEntries =  infile_nEvt.Get("h_cutFlow").GetBinContent(1)
                
                #print "nEntries ", nEntries
                infile =   ROOT.TFile.Open(filename)
                htmp = infile.Get(var)
                htmp_norm = infile.Get(var)

                htmp.Multiply(infile.Get('h_bprimemass_b'))
                htmp.Divide(infile.Get('h_bprimemass_d'))

                htmp.Sumw2()
                htmp_norm.Sumw2()
                htmp.Rebin(2)
                htmp_norm.Rebin(2)

                #print "bin ", var, " ", htmp.GetNbinsX()
                
                if(htmp_norm.Integral() !=0): htmp_norm.Scale((1./nEntries) * c.skimEff * c.sigma * 1000.* float(opt.lumi) )
                
                histos.append(htmp)
                histos_norm.append(htmp_norm)

            h1 = histos[0]
            [h1.Add(hi) for hi in histos[1:]]
            h1.SetLineColor(s.color)
            h1.SetLineStyle(ROOT.kDotted)
            h1.SetLineWidth(3)
            h1.Rebin(2)
            histo_CR.append(h1)

            #print "bin ht ", h1.GetNbinsX()
        
            h2 = histos_norm[0]
            [h2.Add(hi) for hi in histos_norm[1:]]
            h2.SetLineColor(s.color)
            h2.SetLineStyle(ROOT.kDotted)
            h2.SetLineWidth(3)
            h2.Rebin(2)
            histo_CRNorm.append(h2)
        
        else:
            if(opt.sys=="noSys"):filename = '../newTTDManalysis/res/'+s.label+"_" + opt.category + "_" + opt.channel+".root"
            else:filename = '../newTTDManalysis/res/'+s.label+"_" + opt.channel+ "_" + opt.category +"_"+ opt.sys +".root"
            
            filename_nEvt = '../newTTDManalysis/res/'+s.label+"_" + opt.category + "_" + opt.channel+".root"
            
            infile_nEvt = ROOT.TFile.Open(filename_nEvt)
            nEntries =  infile_nEvt.Get("h_cutFlow").GetBinContent(1)
            #print "nEntries ", nEntries
            infile =  ROOT.TFile.Open(filename)
            htmp = ROOT.TH1F(infile.Get(var))
            htmp_norm = ROOT.TH1F(infile.Get(var))

            htmp.Sumw2()
            htmp_norm.Sumw2()

            htmp.Rebin(2)
            htmp_norm.Rebin(2)
            #print "bin ", var, " ", htmp.GetNbinsX()

            if(htmp_norm.Integral() !=0): htmp_norm.Scale((1./nEntries) * s.skimEff * s.sigma * 1000.* float(opt.lumi) )
  
            htmp.SetLineColor(s.color)
            htmp.SetLineStyle(ROOT.kDotted)
            htmp.SetLineWidth(3)
            #htmp.Rebin(2)
            #htmp_norm.Rebin(2)

            #print "bin metfinal sum", htmp.GetNbinsX()

            histo_CR.append(htmp)
            histo_CRNorm.append(htmp_norm)
                        
    c1 = ROOT.TCanvas()
    c1.cd()
    
    H=600
    W=700
    
    H_ref = 600
    W_ref = 700
    
    T = 0.08*H_ref
    B = 0.12*H_ref
    L = 0.12*W_ref
    R = 0.08*W_ref


    for i in range(0,len(histo_CR)):

        c1 = ROOT.TCanvas("c1","c1",50,50,W,H)
        c1.SetFillColor(0);
        c1.SetBorderMode(0);
        c1.SetFrameFillStyle(0);
        c1.SetFrameBorderMode(0);
        c1.SetLeftMargin( L/W );
        c1.SetRightMargin( R/W );
        c1.SetTopMargin( 1 );
        c1.SetBottomMargin(0);
        c1.SetTickx(0);
        c1.SetTicky(0);

        x1 = 0.
        x2 = 2000.
  
        integral_met = histo_met[i].Integral(histo_met[i].GetXaxis().FindBin(x1),histo_met[i].GetXaxis().FindBin(x2))
        integral_CR = histo_CR[i].Integral(histo_CR[i].GetXaxis().FindBin(x1),histo_CR[i].GetXaxis().FindBin(x2))
        
        histo_met[i].Sumw2()
        histo_CR[i].Sumw2()
        histo_met[i].SetTitle("")
        histo_CR[i].SetTitle("")

#        if(integral_met !=0): histo_met[i].Scale(1/integral_met)
#        if(integral_CR !=0): histo_CR[i].Scale(1/integral_CR)
     
        #writeSummary(sample_name[i], opt.channel, histo_metNorm[i] , opt.lumi,"reg A",var)
        #writeSummary(sample_name[i], opt.channel, histo_CRNorm[i] , opt.lumi,"CR", var)
        
        histo_met[i].GetXaxis().SetRangeUser(x1,x2)
        histo_CR[i].GetXaxis().SetRangeUser(x1,x2)

        pad1= ROOT.TPad("pad1", "pad1", 0, 0.30 , 1, 1)
        pad1.SetTopMargin(0.1)
        pad1.SetBottomMargin(0.026)
        pad1.SetLeftMargin(0.12)
        pad1.SetRightMargin(0.05)
        pad1.SetBorderMode(0);
        pad1.SetTickx(0);
        pad1.SetTicky(0);
        pad1.Draw()
        pad1.SetLogy()
        pad1.cd()

        leg = ROOT.TLegend(0.58,0.54,0.86,0.88)

        histo_met[i].Sumw2()
        histo_CR[i].Sumw2()

        histo_met[i].Draw("e1hist")
        histo_CR[i].Draw("e1histsame")
    
        print '', infile.Get('h_bprimemass').Integral()
        print '', infile.Get('h_bprimemass_b').Integral()
        print '', infile.Get('h_bprimemass_c').Integral()
        print '', infile.Get('h_bprimemass_d').Integral()
 #print '========>', histo_met[i].GetBinWidth(1)
        #print '========>', histo_met[i].GetBinWidth(2)
        #print '========>', histo_met[i].GetBinWidth(3)
        #print '========>', histo_met[i].GetBinWidth(4)
        #print '========>', histo_met[i].GetBinWidth(5)
        #print '========>', histo_met[i].GetBinWidth(6)
        #print '========>', histo_met[i].GetBinWidth(7)
        #print '========>', histo_met[i].GetBinWidth(8)
        #print '========>', histo_met[i].GetBinWidth(9)


        maximum = max([histo_met[i].GetMaximum(),histo_CR[i].GetMaximum()])
        minimum = min([histo_met[i].GetMinimum(),histo_CR[i].GetMinimum()])

        #Maximum for log scale                                                                                                  
        histo_met[i].SetMaximum(maximum*50)
        #Maximum for non log scale                                                                                               
        #histo_met[i].SetMaximum(maximum*1.8)
        if(minimum > 0):
            histo_met[i].SetMinimum(0.01*minimum)
        else:
            histo_met[i].SetMinimum(0.01)

        leg.AddEntry(histo_met[i], legend_name[i]+" (reg A)", "l")
#        leg.AddEntry(histo_CR[i], legend_name[i]+" (reg C)", "l")
        leg.AddEntry(histo_CR[i], legend_name[i]+" reg (C#times #frac{B}{D})", "l") 
        leg.SetTextSize(0.05)
        leg.SetTextFont(42)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)                                                                                                                 
        leg.SetFillStyle(0)  
        leg.Draw("same")

        text = ROOT.TLatex(0.6, 0.50, ("KS = %.3f,  #chi^{2}/ndf = %.1f/%d" %( histo_met[i].KolmogorovTest(histo_CR[i], "UO"), histo_met[i].Chi2Test(histo_CR[i], "WW, CHI2"), histo_met[i].GetNbinsX()-2)))
        #text = ROOT.TLatex(0.6, 0.5, 'ciao')                                                                                                                         
        text.SetNDC()
        text.SetTextSize(0.03)
        text.Draw("same")

#       DrawStatBox(histo_met[i], histo_CR[i], 0.5, 0.5, 0.3)
        
        histo_met[i].GetYaxis().SetTitle("Events") 
        histo_met[i].GetXaxis().SetLabelOffset(4.) 
        histo_met[i].GetYaxis().SetLabelFont(42)
        histo_met[i].GetYaxis().SetLabelSize(0.055)

        histo_met[i].GetYaxis().SetTitleSize(0.055)
        histo_met[i].GetYaxis().SetTitleFont(42)
        histo_met[i].GetYaxis().SetTitleOffset(1.)

        c1.cd()
        
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.03, 1, 0.29)
        pad2.SetTopMargin(0.05)
        pad2.SetBottomMargin(0.36)
        pad2.SetLeftMargin(0.12)
        pad2.SetRightMargin(0.05)        

        c1.cd()
        pad2.Draw()
        pad2.cd()
       
        ratio  = histo_met[i].Clone("ratio")
        ratio.SetLineColor(ROOT.kBlack)
        ratio.SetMinimum(0.1) 
        #ratio.SetMaximum(3.0)
        ratio.Sumw2()
        ratio.SetStats(0)
        
        denom = histo_CR[i].Clone("denom")
        denom.Sumw2()

        #if(integral_met !=0 and integral_CR !=0): 
        if(1>0):
            ratio.Divide(denom)
            ratio.SetMarkerStyle(20)
            ratio.Draw("epx0")
            ratio.SetTitle("")

        ratio.Sumw2()

        f1 = ROOT.TF1("myfunc","[0]",-100000,10000);
        f1.SetLineColor(ROOT.kBlack)
        f1.SetLineStyle(ROOT.kDashed)
        f1.SetParameter(0,1);
        f1.Draw("Same")

        ratio.Draw("epx0same")
#        ratio.GetYaxis().SetTitle("A/C")
        ratio.GetYaxis().SetTitle("A/(C #times B/D)")

        ratio.GetYaxis().SetNdivisions(503)
        ratio.GetXaxis().SetLabelFont(42);
        ratio.GetYaxis().SetLabelFont(42);
        ratio.GetXaxis().SetTitleFont(42);
        ratio.GetYaxis().SetTitleFont(42);
        
        ratio.GetXaxis().SetTitleOffset(1.2);
        ratio.GetYaxis().SetTitleOffset(0.29);#0.31
        
        ratio.GetXaxis().SetLabelSize(0.12);
        ratio.GetYaxis().SetLabelSize(0.12);
        ratio.GetXaxis().SetTitleSize(0.14);
        ratio.GetYaxis().SetTitleSize(0.16);
        
        #max_tmp = ratio.GetMaximum()

        ratio.GetYaxis().SetRangeUser(0.,2.)
        
        ratio.GetXaxis().SetTitle("mass (GeV)")
        
        ratio.GetXaxis().SetLabelOffset(0.06)
        ratio.GetYaxis().SetLabelOffset(0.015)
        
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Simulation"
        CMS_lumi.lumi_sqrtS = " 13 TeV"
        
        iPeriod = 0
        iPos = 11
        
        CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)

        if(1>0):
        #if(integral_met !=0 and integral_CR !=0):
            c1.Print("bkg_CR_SR/log/"+sample_name[i]+var+"_"+opt.channel+"_ACBD.pdf")
            c1.Print("bkg_CR_SR/log/"+sample_name[i]+var+"_"+opt.channel+".png")
            c1.Print("bkg_CR_SR/log/"+sample_name[i]+var+"_"+opt.channel+".root")

        pad1.Close()
        pad2.Close()

        tdrstyle.setTDRStyle();
        
        c3 = ROOT.TCanvas("c1","c1",50,50,W,H)
        c3.SetFillColor(0);
        c3.SetBorderMode(0);
        c3.SetFrameFillStyle(0);
        c3.SetFrameBorderMode(0);
        c3.SetLeftMargin( 0.15 );#L/W                       
        c3.SetRightMargin( R/W );
        c3.SetTopMargin( T/H );
        c3.SetBottomMargin(0.14);
        c3.SetTickx(0);
        c3.SetTicky(0);
        c3.Draw()

        leg_sign = ROOT.TLegend(.68, .79, 0.75, .91)
        leg_sign.SetFillColor(0)
        leg_sign.SetTextSize(0.04)
        leg_sign.SetTextFont(42)

        histo_metNorm[i].GetXaxis().SetRangeUser(x1,x2)
        histo_CRNorm[i].GetXaxis().SetRangeUser(x1,x2)

        ratioTF  = histo_metNorm[i].Clone("ratioTF")
        ratioTF.SetLineColor(ROOT.kBlue)
        ratioTF.Sumw2()
        ratioTF.SetStats(0)

        denomTF = histo_CRNorm[i].Clone("denomTF")
        denomTF.Sumw2()

        if(histo_metNorm[i].Integral() !=0 and histo_CRNorm[i].Integral() !=0):
            ratioTF.Divide(denomTF)
            ratioTF.SetMarkerStyle(20)
            ratioTF.SetMarkerColor(ROOT.kBlue)
            ratioTF.Draw("e1p")
            ratioTF.SetTitle("")

        ratioTF.Sumw2()
        ratioTF.GetXaxis().SetLabelFont(42);
        ratioTF.GetYaxis().SetLabelFont(42);
        ratioTF.GetXaxis().SetTitleFont(42);
        ratioTF.GetYaxis().SetTitleFont(42);
        ratioTF.GetXaxis().SetTitleOffset(0.9);
        ratioTF.GetYaxis().SetTitleOffset(1.1);
        #ratioTF.GetXaxis().SetLabelOffset(0.6);
        ratioTF.GetYaxis().SetLabelOffset(0.01);
        ratioTF.SetTitleFont(42);
        ratioTF.SetTitle("");
        
        ratioTF.GetXaxis().SetLabelSize(0.04);
        ratioTF.GetYaxis().SetLabelSize(0.04);
        ratioTF.GetXaxis().SetTitleSize(0.055);
        ratioTF.GetYaxis().SetTitleSize(0.055);
        
        ratioTF.SetLineWidth(2)
        #ratioTF.SetLineColor()
        ratioTF.SetStats(0)
        
        leg_sign.AddEntry(ratioTF, " "+legend_name[i], "p")

        maximum = ratioTF.GetMaximum()
        minimum = ratioTF.GetMinimum()
 
        if(minimum<=0):
            minimum = 0.000000000000000001
            
        ratioTF.SetMaximum(maximum*1.5)
        ratioTF.SetMinimum(0.001*minimum)
        #else: ratioTF.SetMinimum(0.4)
        
        #ratioTF.Draw("e1p")
        ratioTF.GetYaxis().SetTitle("#rho_{i} (reg A)")
        ratioTF.GetXaxis().SetTitle("H_{T} (GeV)")

        leg_sign.Draw("same")

        CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
        CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Simulation"
        CMS_lumi.lumi_sqrtS = " 13 TeV"
        
        iPeriod = 0
        iPos = 11
        
        CMS_lumi.CMS_lumi(c3, iPeriod, iPos)
        
        c3.cd()
        c3.Update();
        c3.RedrawAxis();
        #c3.GetFrame().Draw();

        if((var=="h_bprimemass_b") ):

            #print "********** max ", maximum
            #print "********** min ", minimum
            
            c3.Print("bkg_CR_SR/"+"TF"+sample_name[i]+var+"_"+opt.channel+"ACBD.pdf")
            c3.Print("bkg_CR_SR/"+"TF"+sample_name[i]+var+"_"+opt.channel+".png")
            c3.Print("bkg_CR_SR/"+"TF"+sample_name[i]+var+"_"+opt.channel+".root")        
        
