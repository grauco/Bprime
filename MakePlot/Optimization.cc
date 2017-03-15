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
#include "TLatex.h"

#define PATH "output/singleh/histos_lin/"

void Optimization(){

  TFile *qcd = new TFile((PATH+string("QCD_cat_inclusive_singleH.root")).c_str());
  TFile *tt = new TFile((PATH+string("TT_cat_inclusive_singleH.root")).c_str());
  TFile *Bprime800 = new TFile((PATH+string("BprimeBToHB800_cat_inclusive_singleH.root")).c_str());
  TFile *Bprime1800 = new TFile((PATH+string("BprimeBToHB1800_cat_inclusive_singleH.root")).c_str());
  
  TH1F *h_nfatjet_opt_qcd = (TH1F*)qcd->Get("h_nfatjet_opt");
  TH1F *h_nfatjet_opt_tt = (TH1F*)tt->Get("h_nfatjet_opt");
  TH1F *h_nfatjet_opt_b800 = (TH1F*)Bprime800->Get("h_nfatjet_opt");
  TH1F *h_nfatjet_opt_b1800 = (TH1F*)Bprime1800->Get("h_nfatjet_opt");

  TH1F *h_significance_b800 = new TH1F("h_significance_b800", "Significance for m(B')=800 GeV", 10, -0.5, 9.5);
  
  TH1F *h_significance_b1800 = new TH1F("h_significance_b1800", "Significance for m(B')=1800 GeV", 10, -0.5, 9.5);
  
  for(int i=1; i< h_nfatjet_opt_qcd->GetNbinsX()+1; i++){
    
    if(h_nfatjet_opt_b800->GetBinContent(i) +  h_nfatjet_opt_qcd->GetBinContent(i) + h_nfatjet_opt_tt->GetBinContent(i) !=0 )  h_significance_b800 -> SetBinContent(i, (float)(h_nfatjet_opt_b800->GetBinContent(i)/sqrt(h_nfatjet_opt_qcd->GetBinContent(i) + h_nfatjet_opt_tt->GetBinContent(i) + h_nfatjet_opt_b800->GetBinContent(i))));
    cout << (float)(h_nfatjet_opt_b800->GetBinContent(i)/sqrt(h_nfatjet_opt_qcd->GetBinContent(i) + h_nfatjet_opt_tt->GetBinContent(i) + h_nfatjet_opt_b800->GetBinContent(i))) << endl;
    if(h_nfatjet_opt_b1800->GetBinContent(i) +  h_nfatjet_opt_qcd->GetBinContent(i) + h_nfatjet_opt_tt->GetBinContent(i) !=0 ) h_significance_b1800 -> SetBinContent(i, (float)(h_nfatjet_opt_b1800->GetBinContent(i)/sqrt(h_nfatjet_opt_qcd->GetBinContent(i) + h_nfatjet_opt_tt->GetBinContent(i) + h_nfatjet_opt_b1800->GetBinContent(i) )));     
    
  }

  TCanvas *c1 = new TCanvas("c1","Root Canvas",0,0,600,600);
  gStyle->SetOptStat(0);
    
  gStyle->SetPaintTextFormat("1.2f");
  
  h_significance_b800->Draw("HISTO TEXT0");
  h_significance_b800->SetLineColor(kGreen+2);
  h_significance_b800->SetMarkerColor(kGreen+2);
  h_significance_b800->SetMarkerStyle(2);
  h_significance_b800->SetMarkerSize(1);
  h_significance_b1800->Draw("HISTO TEXT0 SAME");
  h_significance_b1800->SetLineColor(kMagenta);
  h_significance_b1800->SetMarkerColor(kMagenta);
  h_significance_b1800->SetMarkerStyle(2);
  h_significance_b1800->SetMarkerSize(1);

  h_significance_b800->SetTitle("");
  h_significance_b800->SetMinimum(0);
  h_significance_b800->SetMaximum(2);
  h_significance_b800->GetYaxis()->SetTitle("#frac{S}{#sqrt{S+B}}");
  h_significance_b800->GetXaxis()->SetTitle("AK8 jets multiplicity");

  leg = new TLegend(0.6,0.7,0.85,0.85);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);
  leg->AddEntry(h_significance_b800,"m(B')=800 GeV","f");
  leg->AddEntry(h_significance_b1800,"m(B')=1800 GeV","f");
  leg->Draw();
   
  c1->SaveAs("ak8mult_opt.pdf");
 
}
