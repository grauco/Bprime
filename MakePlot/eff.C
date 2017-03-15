/**********************************************************************************************
 1;95;0c                                      Giorgia Rauco 
                                        06.11.2015

1) define the paths of the histos files in #define PATH
21;95;0c) create a folder called Plots_syst, where the output plots will be saved
3) the macro has 3 options:
          i) channel: semileptonic, fullhadronic
         ii) syst: jes, mistag, btag
        iii) histo: metFinal, metFinal_outtop, metFinal_2lep, metFinal_met_0btag, metFinal_SR_1lep
4) to run the macro (example):  root -l -b -q 'ttDM_syst.C("semileptonic", "jes", "metFinal")'
5) plot.csh, script already including all the combination
***************************************************************** *******************************/
#include "TEfficiency.h"
#include "TStyle.h"
#include "TColor.h"
#include "TLorentzVector.h"
#include "TClonesArray.h"
#include "TTree.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include "TF1.h"
#include "TAxis.h"
#include "TString.h"
#include "THStack.h"
#include "TPaveText.h"

#include <math.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>

//define path for taking histos
//#define PATH "output/singleh/histos/"

void eff(){
  
  //  TEfficiency* pEff = 0;
  //TEfficiency* pEffh = 0;

  TFile *QCD_bg = new TFile("../BprimeAnalysis/res_Mo17_AN_22Feb/SingleMubcdefg.root");
  TFile *QCD_h = new TFile("../BprimeAnalysis/res_Mo17_AN_22Feb/SingleMuh.root");

  TH1::SetDefaultSumw2() ;
  TH1F *h_QCD_bg_ratio = (TH1F*) QCD_bg->Get("h_Ht_trigaft");
  TH1F *h_QCD_bg_without = (TH1F*) QCD_bg->Get("h_Ht_bef");
  TH1F *h_QCD_h_ratio = (TH1F*) QCD_h->Get("h_Ht_trigaft");
  TH1F *h_QCD_h_without = (TH1F*) QCD_h->Get("h_Ht_bef");
  //TH1F *h_ratio = new TH1F("ratio", "ratio", 300, 0, 3000);
  //gStyle->SetErrorY(0.);
  //if(TEfficiency::CheckConsistency(*h_QCD_bg_ratio,*h_QCD_bg_without)) pEff = new TEfficiency(*h_QCD_bg_ratio,*h_QCD_bg_without);
  
  TH1::SetDefaultSumw2();
  h_QCD_bg_ratio->Sumw2();
  h_QCD_h_without->Sumw2();
  h_QCD_bg_ratio->Sumw2();
  h_QCD_h_without->Sumw2();

  h_QCD_h_ratio->Rebin(4); 
  h_QCD_bg_ratio->Rebin(4); 
  h_QCD_bg_without->Rebin(4); 
  h_QCD_h_without->Rebin(4); 


  //if(TEfficiency::CheckConsistency(*h_QCD_bg_ratio,*h_QCD_bg_without)) pEff = new TEfficiency(*h_QCD_bg_ratio,*h_QCD_bg_without);
  //if(TEfficiency::CheckConsistency(*h_QCD_h_ratio,*h_QCD_h_without)) pEffh = new TEfficiency(*h_QCD_h_ratio,*h_QCD_h_without);
  //h_ratio->Clone(h_QCD_bg_with);

  h_QCD_bg_ratio->Divide(h_QCD_bg_without);
  h_QCD_bg_ratio->GetXaxis()->SetRangeUser(300,2000);
  h_QCD_h_ratio->Divide(h_QCD_h_without);
  h_QCD_h_ratio->GetXaxis()->SetRangeUser(300,2000);

  //if(TEfficiency::CheckConsistency(*h_QCD_bg_ratio,*h_QCD_bg_without)) pEff = new TEfficiency(*h_QCD_bg_ratio,*h_QCD_bg_without);             
  //if(TEfficiency::CheckConsistency(*h_QCD_h_ratio,*h_QCD_h_without)) pEffh = new TEfficiency(*h_QCD_h_ratio,*h_QCD_h_without); 

  int b1250= h_QCD_bg_ratio-> GetXaxis()->FindBin(1250);
  int b1300= h_QCD_bg_ratio-> GetXaxis()->FindBin(1300);

  cout << "bin 1250: " << h_QCD_bg_ratio-> GetBinContent(b1250) << endl;
  cout << "bin 1300: " << h_QCD_bg_ratio-> GetBinContent(b1300) << endl;

  //TEffiency *pEff_bg = new TEfficiency(h_QCD_bg_ratio,h_QCD_bg_without);
  //TEffiency *pEff_h = new TEfficiency(h_QCD_h_ratio,h_QCD_h_without);

  //h_QCD_h_ratio->Rebin(4);
  //h_QCD_bg_ratio->Rebin(4);
  TF1 *erf1 = new TF1("erf1", "0.5*1*(1+TMath::Erf( (x-[0]) / ([1]*sqrt(2)) ) )", 800.,2000);
  erf1->SetParameter(0,850);
  erf1->SetParLimits(0, 800, 880);
  erf1->SetParameter(1,300);
  erf1->SetParameter(2,1);
  erf1->SetLineColor(kBlue+2);
  TF1 *erf2 = new TF1("erf2", "0.5*1*(1+TMath::Erf( (x-[0]) / ([1]*sqrt(2)) ) )", 800.,2000);
  erf2->SetParameter(0,1000);
  erf2->SetParameter(1,600);
  erf2->SetParLimits(0, 800, 900);
  erf2->SetParLimits(1, 100, 200);
  erf2->SetParameter(2,1);
  erf2->SetLineColor(kRed+2);
  h_QCD_bg_ratio->Fit("erf1", "r");
  h_QCD_h_ratio->Fit("erf2", "r");
  
  h_QCD_bg_ratio->SetLineColor(kBlue+2);
  h_QCD_bg_ratio->SetMarkerColor(kBlue+2);
  h_QCD_bg_ratio->SetMarkerStyle(20);
  h_QCD_bg_ratio->SetMarkerSize(1);
  h_QCD_bg_ratio->SetLineWidth(2);
  
  h_QCD_h_ratio->SetLineColor(kRed+2);
  h_QCD_h_ratio->SetMarkerColor(kRed+2);
  h_QCD_h_ratio->SetMarkerStyle(21);
  h_QCD_h_ratio->SetMarkerSize(1);
  h_QCD_h_ratio->SetLineWidth(2);

  
  h_QCD_bg_ratio->GetYaxis()->SetTitle("Events (Normalized to unity)");
  //h_QCD_bg_ratio->GetYaxis()->SetTitleOffset(1.2);                                                                                                                               
  //h_QCD_bg_ratio->GetXaxis()->SetTitleOffset(1.2);                                                                                                                               
  h_QCD_bg_ratio->GetXaxis()->SetTitle("H_{T} (GeV)");
  h_QCD_bg_ratio->SetTitle("");
  h_QCD_bg_ratio->SetMinimum(-0.1);
  //h_QCD_bg_ratio->SetMaximum(1.1);

  //canvas booking
  TCanvas *canvas = new TCanvas("canvas", "canvas", 600, 600);
  TPad *pad1 = new TPad("pad1", "pad1", 0.01, 0.01, 1.,1.);
  pad1->SetBottomMargin(0.15);
  pad1->Draw();
  pad1->cd();

  gStyle->SetOptStat(0);
  
  h_QCD_bg_ratio->GetXaxis()->SetRangeUser(300,2000);
  h_QCD_h_ratio->GetXaxis()->SetRangeUser(300,2000);
  h_QCD_bg_ratio->GetYaxis()->SetTitle("Events (Normalized to unity)");
  //h_QCD_bg_ratio->GetYaxis()->SetTitleOffset(1.2);
  //h_QCD_bg_ratio->GetXaxis()->SetTitleOffset(1.2);
  h_QCD_bg_ratio->GetXaxis()->SetTitle("H_{T} (GeV)");
  h_QCD_bg_ratio->SetTitle("");
  h_QCD_bg_ratio->SetMinimum(-0.1);
  //h_QCD_bg_ratio->SetMaximum(1.1);

  h_QCD_bg_ratio->DrawCopy("p9");
  h_QCD_h_ratio->DrawCopy("p9 same");
  //pEff->Draw("AP");                                                                                                            
  // pEffh->Draw("p same");   

  h_QCD_h_ratio->GetYaxis()->SetTitle("Events (Normalized to unity)");
  //h_QCD_h_ratio->GetYaxis()->SetTitleOffset(0.8);
  h_QCD_h_ratio->GetXaxis()->SetTitle("H_{T} (GeV)");
  h_QCD_h_ratio->SetTitle("");
  h_QCD_h_ratio->SetMinimum(0.0);
  //h_QCD_h_ratio->SetMaximum(1.1);

  TLegend *leg = new TLegend(0.12,0.65,0.3,0.85); 
  leg->SetNColumns(1);
  leg->SetTextSize(0.02);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);
  leg->AddEntry(h_QCD_bg_ratio, "PFHT900 in B-G" ,"ep");
  leg->AddEntry(h_QCD_h_ratio, "(PFHT900||PFJet450) in H" ,"ep");
  //leg->AddEntry(erf1, "ERF fit in eras B-G", "l");
  //leg->AddEntry(erf2, "ERF fit in era H", "l");
  leg->Draw();

  TString cmsText     = "CMS";
  float cmsTextFont   = 61;  // default is helvetic-bold                                                                                             
  bool writeExtraText = true;
  TString extraText   = "Preliminary";
  float extraTextFont = 52;  // default is helvetica-italics                                                                                         
  // text sizes and text offsets with respect to the top frame in unit of the top margin size                                                        
  float lumiTextSize     = 0.6;
  float lumiTextOffset   = 0.2;
  float cmsTextSize      = 0.45;
  float cmsTextOffset    = 0.1;  // only used in outOfFrame version                                                                                  
  float relPosX    = 0.045;
  float relPosY    = 0.035;
  float relExtraQCD_bg_pythia = 1.2;
  // ratio of "CMS" and extra text size                                                                                                              
  float extraOverCmsTextSize  = 0.76;
  TString lumi_13TeV = "37.9 fb^{-1} (13 TeV)";
  TString lumi_8TeV  = "19.7 fb^{-1}";
  TString lumi_7TeV  = "5.1 fb^{-1}";
  TString lumiText;
  lumiText = "#sqrt{s} = 13 TeV ";
  float t = pad1->GetTopMargin();
  float b = pad1->GetBottomMargin();
  float r = pad1->GetRightMargin();
  float l = pad1->GetLeftMargin();
  TLatex latex;
  latex.SetNDC();
  latex.SetTextAngle(0);
  latex.SetTextColor(kBlack);
  float extraTextSize = extraOverCmsTextSize*cmsTextSize;
  latex.SetTextFont(42);
  latex.SetTextAlign(31);
  latex.SetTextSize(lumiTextSize*t*1.0);
  latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumi_13TeV);
  latex.SetTextFont(cmsTextFont);
  latex.SetTextAlign(11);
  latex.SetTextSize(cmsTextSize*t);
  latex.DrawLatex(l+0.03, 1-t+lumiTextOffset*t,cmsText);
  latex.SetTextFont(extraTextFont);
  latex.SetTextSize(extraTextSize*t);
  latex.DrawLatex(l+0.14, 1-t+lumiTextOffset*t, extraText);

  TPaveText *cat = new TPaveText(.6,.18,.8,.23, "brNDC");
  cat->AddText("at least 1 forward jet region");
  cat->SetBorderSize(0); 
  //  cat->Draw();

  canvas->cd();
  
  h_QCD_bg_ratio->GetXaxis()->SetTitle("H_{T} (GeV)");
  h_QCD_bg_ratio->SetTitle("");
  h_QCD_bg_ratio->SetMinimum(0.0);
  //h_QCD_bg_ratio->SetMaximum(1.1);

  h_QCD_h_ratio->GetXaxis()->SetTitle("H_{T} (GeV)");
  h_QCD_h_ratio->SetTitle("");
  h_QCD_h_ratio->SetMinimum(0.0);
  //h_QCD_h_ratio->SetMaximum(1.1);

  //canvas->Print("PFHT800_eff_cat_inclusive.png");
  canvas->Print("CHECK_PFHT900_eff_cat_inclusive.pdf");
  
}
