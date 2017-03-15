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

void sign(){

  TFile *QCD = new TFile("output/singleh/histos_Mo17_njets_18Feb/QCD_cat1_singleH.root");
  TFile *B_1000 = new TFile("output/singleh/histos_Mo17_njets_18Feb/BprimeBToHB1000_cat1_singleH.root");
  TFile *B_1800 = new TFile("output/singleh/histos_Mo17_njets_18Feb/BprimeBToHB1800_cat1_singleH.root");

  TH1::SetDefaultSumw2() ;
  TH1F *h_QCD_0 = (TH1F*) QCD->Get("h_bprimemass_SR");
  TH1F *h_QCD_1 = (TH1F*) QCD->Get("h_bprimemass_SR_1");
  TH1F *h_QCD_2 = (TH1F*) QCD->Get("h_bprimemass_SR_2");
  TH1F *h_QCD_3 = (TH1F*) QCD->Get("h_bprimemass_SR_3");
  TH1F *h_QCD_4 = (TH1F*) QCD->Get("h_bprimemass_SR_4");
  TH1F *h_QCD_5 = (TH1F*) QCD->Get("h_bprimemass_SR_5");

  TH1F *h_B1000_0 = (TH1F*) B_1000->Get("h_bprimemass_SR");
  TH1F *h_B1000_1 = (TH1F*) B_1000->Get("h_bprimemass_SR_1");
  TH1F *h_B1000_2 = (TH1F*) B_1000->Get("h_bprimemass_SR_2");
  TH1F *h_B1000_3 = (TH1F*) B_1000->Get("h_bprimemass_SR_3");
  TH1F *h_B1000_4 = (TH1F*) B_1000->Get("h_bprimemass_SR_4");
  TH1F *h_B1000_5 = (TH1F*) B_1000->Get("h_bprimemass_SR_5");

  TH1F *h_B1800_0 = (TH1F*) B_1800->Get("h_bprimemass_SR");
  TH1F *h_B1800_1 = (TH1F*) B_1800->Get("h_bprimemass_SR_1");
  TH1F *h_B1800_2 = (TH1F*) B_1800->Get("h_bprimemass_SR_2");
  TH1F *h_B1800_3 = (TH1F*) B_1800->Get("h_bprimemass_SR_3");
  TH1F *h_B1800_4 = (TH1F*) B_1800->Get("h_bprimemass_SR_4");
  TH1F *h_B1800_5 = (TH1F*) B_1800->Get("h_bprimemass_SR_5");
  
  //float B1000_0=0, B1000_1=0, B1000_2=0, B1000_3=0, B1000_4=0, B1000_5=0;
  //float B1800_0=0, B1800_1=0, B1800_2=0, B1800_3=0,B1800_4=0, B1800_5=0;
  
  float x[6]={0,1,2,3,4,5};
  float B1000[6], B1800[6];
  B1000[0]=h_B1000_0->Integral()/sqrt(h_B1000_0->Integral() + h_QCD_0->Integral());
  B1000[1]=h_B1000_1->Integral()/sqrt(h_B1000_1->Integral() + h_QCD_1->Integral());
  cout << h_B1000_1->Integral()/sqrt(h_B1000_1->Integral() + h_QCD_1->Integral()) << endl;
  B1000[2]=h_B1000_2->Integral()/sqrt(h_B1000_2->Integral() + h_QCD_2->Integral());
  B1000[3]=h_B1000_3->Integral()/sqrt(h_B1000_3->Integral() + h_QCD_3->Integral());
  B1000[4]=h_B1000_4->Integral()/sqrt(h_B1000_4->Integral() + h_QCD_4->Integral());
  B1000[5]=h_B1000_5->Integral()/sqrt(h_B1000_5->Integral() + h_QCD_5->Integral());
  
  B1800[0]=h_B1800_0->Integral()/sqrt(h_B1800_0->Integral() + h_QCD_0->Integral());
  B1800[1]=h_B1800_1->Integral()/sqrt(h_B1800_1->Integral() + h_QCD_1->Integral());
  cout << h_B1800_1->Integral()/sqrt(h_B1800_1->Integral() + h_QCD_1->Integral()) << endl;
  B1800[2]=h_B1800_2->Integral()/sqrt(h_B1800_2->Integral() + h_QCD_2->Integral());
  B1800[3]=h_B1800_3->Integral()/sqrt(h_B1800_3->Integral() + h_QCD_3->Integral());
  B1800[4]=h_B1800_4->Integral()/sqrt(h_B1800_4->Integral() + h_QCD_4->Integral());
  B1800[5]=h_B1800_5->Integral()/sqrt(h_B1800_5->Integral() + h_QCD_5->Integral());

  TCanvas *c1 = new TCanvas("c1","c1",200,10,600,600);
  //c1->DrawFrame(0, 5, 6, 35);
  //c1->SetFillColor(42);
  c1->SetGrid();
  int n=6;

  TGraph *gr = new TGraph(n,x,B1000);
  gr->SetLineColor(kBlue);
  gr->SetLineWidth(4);
  gr->SetMarkerColor(kBlue);
  gr->SetMarkerStyle(21);
  gr->SetTitle("");
  gr->GetXaxis()->SetTitle("AK4 jets multiplicity cut");
  gr->GetYaxis()->SetTitle("#frac{S}{#sqrt{S+B}}");
  gr ->GetYaxis()->SetTitleOffset(1);
  //gr->SetLineColor(kBlue);
  //gr->SetMinimum(0);
  gr->Draw("ACP");

  TGraph *gr2 = new TGraph(n,x,B1800);
  gr2->SetLineColor(kRed);
  gr2->SetLineWidth(4);
  gr2->SetMarkerColor(kRed);
  gr2->SetMarkerStyle(21);
  gr2->SetTitle("");
  gr2->GetXaxis()->SetTitle("AK4 jets multiplicity cut");
  //gr2->GetYaxis()->SetTitle("Punzi significance");
  gr2->GetYaxis()->SetTitle("#frac{S}{#sqrt{S+B}}");
  gr2 ->GetYaxis()->SetTitleOffset(1);
  //gr2->SetMinimum(0);
  //gr2->SetMaximum(40);
  //gr2->Draw("ACP");

  //  c1->Modified();
  //c1->Update();
  c1->Print("test.pdf");

}
