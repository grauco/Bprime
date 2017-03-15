#include "TH1.h"
#include "TMath.h"
#include "TF1.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TFile.h"
#include "TStyle.h"
#include "TDirectory.h"
#include "TString.h"
#include "TLine.h"
#include "TLatex.h"
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;


void checkBinning(){
  
    TH1::SetDefaultSumw2 (kTRUE);
    
    TFile *qcd = new TFile("output/singleh/histos_Mo17/QCD_cat1_singleH.root");    
    TH1F *h_qcd = (TH1F*)qcd->Get("h_bprimemass_SR");

    TFile *B1600 = new TFile("output/singleh/histos_Mo17/BprimeBToHB1600_cat1_singleH.root");    
    TH1F *h_b1600 = (TH1F*)B1600->Get("h_bprimemass_SR");
    TFile *B1000 = new TFile("output/singleh/histos_Mo17/BprimeBToHB1000_cat1_singleH.root");
    TH1F *h_b1000 = (TH1F*)B1000->Get("h_bprimemass_SR");
    
    float value_qcd[h_qcd->GetNbinsX()-2];
    float value_b1600[h_b1600->GetNbinsX()-2];
    float value_b1000[h_b1000->GetNbinsX()-2];

    TH1F *h_qcd_output = new TH1F("h_output", "",h_qcd->GetNbinsX()-2, 400, 2000);
    TH1F *h_b1600_output = new TH1F("h_output", "",h_b1600->GetNbinsX()-2, 400, 2000);
    TH1F *h_b1000_output = new TH1F("h_output", "",h_b1000->GetNbinsX()-2, 400, 2000);

    for(int i=3; i<h_qcd->GetNbinsX()+1; i++){
      value_qcd[i] = h_qcd->GetBinError(i)/h_qcd->GetBinContent(i);
      value_qcd[i] = value_qcd[i];
      cout << value_qcd[i] << endl;
      if(value_qcd[i]>0.) h_qcd_output->SetBinContent(i-2, value_qcd[i]);

      value_b1600[i] = h_b1600->GetBinError(i)/h_b1600->GetBinContent(i);
      value_b1600[i] = value_b1600[i];
 
      if(value_b1600[i]>0.) h_b1600_output->SetBinContent(i-2, value_b1600[i]);

      value_b1000[i] = h_b1000->GetBinError(i)/h_b1000->GetBinContent(i);
      value_b1000[i] = value_b1000[i];

      if(value_b1000[i]>0.) h_b1000_output->SetBinContent(i-2, value_b1000[i]);
      
    }

    TCanvas *c1 = new TCanvas("c1","",600,600);
    TPad *pad1 = new TPad("pad1", "pad1", 0., 0.08, 1, 1.0);
    pad1->SetBottomMargin(0.08); // Upper and lower plot are joined
    //pad1->SetGridx();         // Vertical grid
    pad1->Draw();             // Draw the upper pad: pad1
    pad1->cd();               // pad1 becomes the current pad
    gStyle->SetOptStat(0);

    h_qcd_output->SetLineColor(kGreen+2);
    h_qcd_output->SetLineWidth(2);
    h_qcd_output->Draw("hist");
    h_qcd_output->GetXaxis()->SetTitle("m(B') (GeV)");
    h_qcd_output->GetYaxis()->SetTitle("BinError/BinContent");
    h_qcd_output->SetMinimum(0.001);
    h_qcd_output->SetMaximum(1.2);

    h_b1600_output->SetLineColor(kRed+2);
    h_b1600_output->SetLineWidth(2);
    h_b1600_output->Draw("hist same");

    h_b1000_output->SetLineColor(kRed-2);
    h_b1000_output->SetLineStyle(3);
    h_b1000_output->SetLineWidth(2);
    h_b1000_output->Draw("hist same");

    leg = new TLegend(0.13,0.65,0.37,0.85);
    leg->SetTextSize(0.03);
    leg->SetFillColor(0);
    leg->SetBorderSize(0);
    leg->AddEntry(h_qcd_output,"QCD","l");
    leg->AddEntry(h_b1600_output,"B'(1600)","l");
    leg->AddEntry(h_b1000_output,"B'(1000)","l");
    leg->Draw();
    
    c1->Print("test.pdf");
    
}




