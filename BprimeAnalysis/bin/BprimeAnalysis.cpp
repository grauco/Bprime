#include "TFile.h"
#include "TChain.h"
#include "TTree.h"
#include "TBranch.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include <vector>
#include <assert.h>
#include <TMVA/Reader.h>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cassert>
#include <sstream>
#include <string>
#include "TFileCollection.h"
#include "THashList.h"
#include "TBenchmark.h"
#include <iostream>
#include <typeinfo>

#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Bprime/BprimeAnalysis/interface/Weights.h"
#include "Bprime/BprimeAnalysis/interface/MT2Utility.h"
#include "Bprime/BprimeAnalysis/interface/mt2w_bisect.h"
#include "Bprime/BprimeAnalysis/interface/mt2bl_bisect.h"
#include "Bprime/BprimeAnalysis/interface/Mt2Com_bisect.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "Bprime/BprimeAnalysis/interface/kFactors.h"

using namespace std;

typedef vector<double> vdouble;
typedef vector<float> vfloat;
typedef vector<int> vint;
typedef vector<bool> vbool;
typedef vector<string> vstring;

enum weightedSysts { NOSYST=0, BTAGUP = 1,BTAGDOWN=2, MISTAGUP=3,MISTAGDOWN=4, PUUP=5, PUDOWN=6, MISTAGHIGGSUP=7, MISTAGHIGGSDOWN=8, MAXSYSTS=9};
enum theoSysts {SCALEUP=101,SCALEDOWN=102, NNPDF1=100, NNPDF2=102};
int wLimit =150;

struct systWeights{
  void initHistogramsSysts(TH1F** histo, TString name, TString, int, float, float);
  void createFilesSysts(TFile ** allFiles, TString basename, TString opt="RECREATE");
  void fillHistogramsSysts(TH1F** histo, float v, float W, double *wcats= NULL,bool verbose=false);
  void fillHistogramsSysts(TH1F** histo, float v, float W,  float *systWeights, int nFirstSysts=(int)MAXSYSTS, double *wcats=NULL, bool verbose=false);
  void writeHistogramsSysts(TH1F** histo, TFile ** allFiles );
  void writeSingleHistogramSysts(TH1F* histo,TFile ** allMyFiles);
  void setMax(int max);
  void setMaxNonPDF(int max);
  void setSystValue(string name, double value, bool mult=false);
  void setSystValue(int systPlace, double value, bool mult=false);
  void setPDFWeights(float * wpdfs, double * xsections, int numPDFs, float wzero=1.0, bool mult=true);
  void setQ2Weights(float q2up, float q2down, float wzero=1.0,bool mult=true);
  void setTWeight(float tweight, float wtotsample=1.0,bool mult=true);
  void setVHFWeight(int vhf,bool mult=true, double shiftval=0.65);
  void setPDFValue(int numPDF, double value);
  double getPDFValue(int numPDF);
  void setWeight(string name, double value, bool mult=false);
  void setWeight(int systPlace, double value, bool mult=false);
  void prepareDefault(bool addDefault, bool addPDF, bool addQ2, bool addTopPt, bool addVHF, bool addTTSplit, int numPDF=102);
  void addSyst(string name);
  void addSystNonPDF(string name);
  void setWCats(double *wcats);
  
  void addkFact(string name);
  void setkFact(string name,float kfact_nom, float kfact_up,float kfact_down,  bool mult=true);

  void copySysts(systWeights sys);
  void calcPDFHisto(TH1F** histos, TH1F* singleHisto, double scalefactor=1.0, int c = 0);
  void setOnlyNominal(bool useOnlyNominal=false);
  bool onlyNominal;
  bool addPDF, addQ2, addTopPt, addVHF, addTTSplit;
  int maxSysts, maxSystsNonPDF;
  int nPDF;
  int nCategories;
  float weightedSysts[150];
  double wCats[10];
  string weightedNames[150];
  string categoriesNames[10];
};

void callme(){
  std::cout<<" NaN value"<<std::endl;
}

int main(int argc, char **argv) {

  TBenchmark bench;
  
  std::cout<<"Let's start"<<endl;
 
  string sample(argv[1]) ;
  std::cout<<"sample: "<<sample<<endl;

  string path(argv[2]);
  std::cout<<"File list to open: "<<path<<endl;

  string channel(argv[3]);
  std::cout<<"channel: "<<channel<<endl;
  
  string cat(argv[4]);
  std::cout<<"category:" <<cat<<endl;
    
  string sys(argv[5]);
  std::cout<<"systematics: "<<sys<<endl;

  string sync(argv[6]);
  std::cout<<"synchro: "<<sync<<endl;

  string isData(argv[7]);
  std::cout<<"isData: "<<isData<<endl;

  std::string outdir(argv[8]);
  std::cout<<"Output directory: "<<outdir<<endl;

  //  std::string outdir(argv[8]);
  //std::cout<<"Output directory: "<<outdir<<endl;

  //  TString path_ = path + "/trees*.root";
  TString path_ = path ; 
  std::cout<<"File to open: "<<path_<<endl;
  
  std::cout << "Loading file collection from " << path << std::endl;
  TFileCollection fc(sample.c_str(),sample.c_str(),path.c_str());
  std::cout << "Files found : " << fc.GetNFiles() << std::endl;

  TH1F * initproduct(TH1F * h_A,TH1F* h_B, int rebinA = 1, int rebinB=1,double integral = -1.);
  TH1F * makeproduct(TH1F * h_A,TH1F* h_B, int rebinA = 1, int rebinB=1,double integral = -1.);
  TH1F * makeproduct(TH2F * h);

  TString syststr = "";
  string syststrname = "";
  // if (lepton != "" && lepton != "any")lepstr= "_"+ lepton;
  if (sys != "noSys"){syststr= "_"+ sys; syststrname= "_"+ sys;}
  
  string reportDir = outdir+"/txt";
  string reportName = reportDir+"/SelectedEvents_"+channel+"_"+sample+syststrname+".txt";
  
  TString weightedSystsNames (weightedSysts sy);
  void initHistogramsSysts(TH1F* histo[(int)MAXSYSTS],TString, TString, int, float, float , bool useOnlyNominal=false);
  void createFilesSysts(  TFile * allFiles[(int)MAXSYSTS], TString basename, bool useOnlyNominal=false, TString opt="RECREATE");
  void fillHistogramsSysts(TH1F* histo[(int)MAXSYSTS], float v, float W, float systWeight[(int)MAXSYSTS] , bool useOnlyNominal=false);
  void writeHistogramsSysts(TH1F* histo[(int)MAXSYSTS], TFile * allFiles[(int)MAXSYSTS] , bool useOnlyNominal=false);
  void writeSingleHistogramSysts(TH1F* histo,TFile * allMyFiles[(int)MAXSYSTS],bool useOnlyNominal=false);

  systWeights syst0B0sB, syst2B0sB, syst1B2sB, syst1B1sB, syst1B0sB, systZero;
  int maxSysts=0;
  bool addPDF=false,addQ2=false, addTopPt=false,addVHF=false,addWZNLO=false, addTTSplit=false;
  addPDF=true;
  addQ2=true;

  int nPDF=102;
  if(isData=="DATA"){addPDF=false, addQ2=false;}
  systZero.prepareDefault(true, addQ2, addPDF, addTopPt,addVHF,addTTSplit);
  
  maxSysts= systZero.maxSysts;

  ofstream fileout;
  fileout.open(reportName.c_str(),ios::in | ios::out | ios::trunc);
  fileout<<"RunNumber EvtNumber Lumi "<<std::endl;

  TFile * allMyFiles[maxSysts];
  TString outfile = outdir + "/res/"+sample + "_" +cat+"_"+channel+".root";
  //TFile fout(outfile, "recreate");
  
  std::cout<<"File to open: "<<path_<<endl;
  TString treePath = "DMTreesDumper/ttDM__noSyst";
  TString treePathNEvents = "DMTreesDumper/WeightHistory";
  if(sys=="jesUp") treePath = "DMTreesDumper/ttDM__jes__up";
  else if(sys=="jesDown") treePath = "DMTreesDumper/ttDM__jes__down";
  else if(sys=="jerUp") treePath = "DMTreesDumper/ttDM__jer__up";
  else if(sys=="jerDown")treePath = "DMTreesDumper/ttDM__jer__down";
   
  bench.Start("NEvents");
  TChain chainNEvents(treePathNEvents);
  chainNEvents.AddFileInfoList(fc.GetList());
  //Int_t nEvents = (Int_t)chainNEvents.GetEntries();
  Int_t nEvents = (Int_t)chainNEvents.GetEntries();
  bench.Stop("NEvents");
  bench.Print("NEvents");

  bench.Start("NEventsPrePres");

  TH1D totalWeightTop("w_top_total","Top pt reweighting: overall sample weight",2000,0,2.0);
  chainNEvents.Project("w_top_total","Event_T_Weight","Event_T_Weight!=1.00");
  double topWeight=totalWeightTop.GetMean();
  cout << "totaltopweight is "<< topWeight<<endl;
  if(topWeight==0)topWeight=1;

  TChain chain(treePath);
  chain.AddFileInfoList(fc.GetList());
  Int_t nEventsPrePres = (Int_t)chain.GetEntries();
  //nEventsPrePres=3000;
  std::cout<<"--> --> Number of Events: "<<nEvents<< " after preselection "<< nEventsPrePres << endl;
  bench.Stop("NEventsPrePres");
  bench.Print("NEventsPrePres");

  std::string samplestr(sample.c_str());
  
  //Q2 and PDF splitting                                                                                                                                                                                                    
  double q2SplittedWeight=1.;
  if(addQ2){
    if((samplestr).find("BprimeBToHB") != std::string::npos){
      TH1D splittedWeightQ2("w_q2_splitted","Q2 splitting: overall sample weight",2000,0,2.0);
      chain.Project("w_q2_splitted","Event_LHEWeight4/Event_LHEWeight0");
      q2SplittedWeight=splittedWeightQ2.GetMean();
    }
    cout << "q2SplittedWeight is "<< q2SplittedWeight<<endl;
  }
  
  double PDFsplittedWeight[nPDF];

  if(addPDF){
      for (int i = 1 ; i <= nPDF ; ++i) 
	{
	  PDFsplittedWeight[i]=1.;
	  if((samplestr).find("BprimeBToHB") != std::string::npos){
	    stringstream pdfss;
	    pdfss<<(i+8);
	    string pstr=(pdfss.str());
	    TH1D splittedWeightPDF("w_pdf_splitted","PDF splitting: overall sample weight",2000,0,2.0);
	    chain.Project("w_pdf_splitted",(("Event_LHEWeight"+pstr+"/Event_LHEWeight0").c_str())); 
	    PDFsplittedWeight[i]=splittedWeightPDF.GetMean();
	    cout << "PDFSplittedWeight " << i << " is " << PDFsplittedWeight[i]<<endl;
	  }
    }
  }

  int sizeMax=50;
  Int_t jetSize, fatjetSize;
  float  Ht(0.);
  float passTrigHT900(0.), passTrigPFJet450(0.), passTrigHT800(0.), passTrigSingleMu(0.);
  float  k_fact(1.), ZPt(-1.), WPt(-1);
  
  float numTrueInt(0), nPV(0.), nGoodPV(0.);
  float w(1.), runNumber(0.), lumiSec(0.);
  double evtNumber(0.);
  float n_closure(0.), nA(0.), nB(0.), nC(0.), nD(0.), n_trig(0.), n_cat(0.), n_Bosonjets(0.), n_bjets(0.), n_ht(0.),n_fatjet(0.), n_jet(0.), n_bjet(0.);
  float jete[sizeMax], jetpt[sizeMax], jetphi[sizeMax], jeteta[sizeMax], jetcsv[sizeMax], jetiscsvm[sizeMax], jetptcorr[sizeMax];
  float fatjete[sizeMax], fatjetpt[sizeMax], fatjeteta[sizeMax], fatjetphi[sizeMax],  fatjetprunedmass[sizeMax], fatjetprunedmasscorr[sizeMax], fatjetptcorr[sizeMax], fatjetnj[sizeMax], fatjetnCSVsubj[sizeMax], fatjetnCSVsubjtm[sizeMax],fatjettau2OVERtau1[sizeMax], fatjetistype1[sizeMax], fatjetistype2[sizeMax], fatjettau3OVERtau2[sizeMax], fatjettau2[sizeMax], fatjettau1[sizeMax];
  
  float bWeightZero = 1.,bWeightZeroBTagUp= 1., bWeightZeroBTagDown=1.0, bWeightZeroMisTagUp=1.0,bWeightZeroMisTagDown=1.0;
  float bWeight1 = 1.,bWeight1BTagUp= 1., bWeight1BTagDown=1.0, bWeight1MisTagUp=1.0,bWeight1MisTagDown=1.0;
  float bWeight2 = 1.,bWeight2BTagUp= 1., bWeight2BTagDown=1.0, bWeight2MisTagUp=1.0,bWeight2MisTagDown=1.0;
  float bWeight1_subj = 1.,bWeight1BTagUp_subj= 1., bWeight1BTagDown_subj=1.0, bWeight1MisTagUp_subj=1.0,bWeight1MisTagDown_subj=1.0;
  float bWeight2_subj = 1.,bWeight2BTagUp_subj= 1., bWeight2BTagDown_subj=1.0, bWeight2MisTagUp_subj=1.0,bWeight2MisTagDown_subj=1.0;
  float bWeight0_subj = 1.,bWeight0BTagUp_subj= 1., bWeight0BTagDown_subj=1.0, bWeight0MisTagUp_subj=1.0,bWeight0MisTagDown_subj=1.0;
  float w_pdfs[nPDF];
  float w_zero,w_q2up,w_q2down, w_top,eventFlavour=0.,NMCLeptons=-1;
  int vhf=0;
  //int nCSVMJets30 =0.;
  
  chain.SetBranchAddress("jetsAK4CHSTight_E", jete);
  chain.SetBranchAddress("jetsAK4CHSTight_Pt", jetpt);
  chain.SetBranchAddress("jetsAK4CHSTight_CorrPt", jetptcorr);
  chain.SetBranchAddress("jetsAK4CHSTight_Phi", jetphi);
  chain.SetBranchAddress("jetsAK4CHSTight_Eta", jeteta);
  chain.SetBranchAddress("jetsAK4CHSTight_CSVv2", jetcsv);
  chain.SetBranchAddress("jetsAK4CHSTight_IsCSVM", jetiscsvm);
  chain.SetBranchAddress("jetsAK4CHSTight_size", &jetSize);
  
  chain.SetBranchAddress("jetsAK8CHS_E", fatjete);
  chain.SetBranchAddress("jetsAK8CHS_Pt", fatjetpt);
  chain.SetBranchAddress("jetsAK8CHS_CorrPt", fatjetptcorr);
  chain.SetBranchAddress("jetsAK8CHS_Eta", fatjeteta);
  chain.SetBranchAddress("jetsAK8CHS_Phi", fatjetphi);
  chain.SetBranchAddress("jetsAK8CHS_prunedMassCHS", fatjetprunedmass);
  chain.SetBranchAddress("jetsAK8CHS_CorrPrunedMassCHS", fatjetprunedmasscorr);
  if(sys=="jmrDown") chain.SetBranchAddress("jetsAK8CHS_CorrPrunedMassCHSJMRDOWN", fatjetprunedmasscorr);
  else if(sys=="jmrUp") chain.SetBranchAddress("jetsAK8CHS_CorrPrunedMassCHSJMRUP", fatjetprunedmasscorr);
  else if(sys=="jmsDown") chain.SetBranchAddress("jetsAK8CHS_CorrPrunedMassCHSJMSDOWN", fatjetprunedmasscorr);
  else if(sys=="jmsUp") chain.SetBranchAddress("jetsAK8CHS_CorrPrunedMassCHSJMSUP", fatjetprunedmasscorr);
  chain.SetBranchAddress("jetsAK8CHS_nJ", fatjetnj);
  chain.SetBranchAddress("jetsAK8CHS_nCSVsubj_tm", fatjetnCSVsubjtm);
  chain.SetBranchAddress("jetsAK8CHS_nCSVsubj", fatjetnCSVsubj);
  chain.SetBranchAddress("jetsAK8CHS_tau2OVERtau1",fatjettau2OVERtau1);
  chain.SetBranchAddress("jetsAK8CHS_tau2CHS", fatjettau2);
  chain.SetBranchAddress("jetsAK8CHS_tau1CHS", fatjettau1);
  chain.SetBranchAddress("jetsAK8CHS_size", &fatjetSize);
  chain.SetBranchAddress("jetsAK8CHS_isType2", fatjetistype2);
  chain.SetBranchAddress("jetsAK8CHS_isType1", fatjetistype1);
  chain.SetBranchAddress("jetsAK8CHS_tau3OVERtau2", fatjettau3OVERtau2);

  //chain.SetBranchAddress("Event_passesHLT_PFHT900", &passTrigHT900);
  chain.SetBranchAddress("Event_passesHadronPFHT900Triggers", &passTrigHT900);
  chain.SetBranchAddress("Event_passesSingleMuTriggers", &passTrigSingleMu);
  //chain.SetBranchAddress("Event_passesHLT_PFHT800", &passTrigHT800);
  chain.SetBranchAddress("Event_passesHadronPFHT800Triggers", &passTrigHT800);
  //chain.SetBranchAddress("Event_passesHLT_PFJet450", &passTrigPFJet450);
  chain.SetBranchAddress("Event_passesHadronPFJet450Triggers", &passTrigPFJet450);
  
  Int_t HBHENoiseFilter, HBHENoiseIsoFilter, EcalDeadCellTriggerPrimitive, globalTightHalo2016Filter, BadChargedCandidateFilter, BadPFMuonFilter;
  Float_t METFilters, goodVertices;
  chain.SetBranchAddress("Event_passesFlag_HBHENoiseFilter", &HBHENoiseFilter);
  chain.SetBranchAddress("Event_passesFlag_HBHENoiseIsoFilter", &HBHENoiseIsoFilter);
  chain.SetBranchAddress("Event_passesFlag_EcalDeadCellTriggerPrimitive", &EcalDeadCellTriggerPrimitive);
  chain.SetBranchAddress("Event_passesFlag_goodVertices", &goodVertices);
  chain.SetBranchAddress("Event_passesFlag_globalTightHalo2016Filter", &globalTightHalo2016Filter);
  chain.SetBranchAddress("Event_passesMETFilters", &METFilters);
  chain.SetBranchAddress("Event_passesBadChargedCandidateFilter", &BadChargedCandidateFilter);
  chain.SetBranchAddress("Event_passesBadPFMuonFilter", &BadPFMuonFilter);

  chain.SetBranchAddress("Event_Ht", &Ht);
  
  chain.SetBranchAddress("Event_RunNumber", &runNumber);
  chain.SetBranchAddress("Event_LumiBlock", &lumiSec);
  chain.SetBranchAddress("Event_EventNumber", &evtNumber);
  chain.SetBranchAddress("Event_nTruePV",&numTrueInt);
  chain.SetBranchAddress("Event_nPV",&nPV);
  chain.SetBranchAddress("Event_nGoodPV", &nGoodPV);
  //chain.SetBranchAddress("Event_nCSVMJetsCut30", &nCSVMJets30);
  chain.SetBranchAddress("Event_Z_Pt", &ZPt);
  chain.SetBranchAddress("Event_W_Pt", &WPt);
  
  const char* Wlabel = "WJets";
  const char* Zlabel = "ZJets";
  const char* DYlabel = "DY";

  bool iswzjets=false;
  double shiftval = 0.0;
  if( !strncmp(sample.c_str(), Wlabel , strlen(Wlabel))) {chain.SetBranchAddress("Event_W_Weight", &k_fact);iswzjets=true;shiftval=0.2;}
  if( !strncmp(sample.c_str(), Zlabel , strlen(Zlabel))) {chain.SetBranchAddress("Event_Z_Weight", &k_fact);iswzjets=true;shiftval=0.2;}
  if( !strncmp(sample.c_str(), DYlabel , strlen(DYlabel))) {chain.SetBranchAddress("Event_Z_Weight", &k_fact);iswzjets=true;shiftval=0.2;}

  std::cout<<"k-factor "<<k_fact<<std::endl;

  if(isData=="MC") chain.SetBranchAddress("Event_LHEWeight0", &w_zero);

  if(addQ2){
    chain.SetBranchAddress("Event_LHEWeight4", &w_q2up);
    chain.SetBranchAddress("Event_LHEWeight8", &w_q2down);
  }

  if(addPDF){
    for (int p = 1; p <= nPDF;++p){
      stringstream pdfss;
      pdfss<<(p+8);
      string pstr =(pdfss.str());
      chain.SetBranchAddress(("Event_LHEWeight"+pstr).c_str(), &w_pdfs[p-1]);
    }
    chain.SetBranchAddress("Event_T_Weight",&w_top);
  }
  if(iswzjets && addVHF){
    chain.SetBranchAddress("Event_eventFlavour",&eventFlavour);
  }
  if(addTTSplit) chain.SetBranchAddress("Event_NMCLeptons",&NMCLeptons);
  
  chain.SetBranchAddress("Event_bWeight0CSVM", &bWeightZero);

  chain.SetBranchAddress("Event_bWeightMisTagUp0CSVM", &bWeightZeroMisTagUp);
  chain.SetBranchAddress("Event_bWeightMisTagDown0CSVM", &bWeightZeroMisTagDown);
  chain.SetBranchAddress("Event_bWeightBTagUp0CSVM", &bWeightZeroBTagUp);
  chain.SetBranchAddress("Event_bWeightBTagDown0CSVM", &bWeightZeroBTagDown);

  chain.SetBranchAddress("Event_bWeight1CSVM", &bWeight1);

  chain.SetBranchAddress("Event_bWeightMisTagUp1CSVM", &bWeight1MisTagUp);
  chain.SetBranchAddress("Event_bWeightMisTagDown1CSVM", &bWeight1MisTagDown);
  chain.SetBranchAddress("Event_bWeightBTagUp1CSVM", &bWeight1BTagUp);
  chain.SetBranchAddress("Event_bWeightBTagDown1CSVM", &bWeight1BTagDown);

  chain.SetBranchAddress("Event_bWeight2CSVM", &bWeight2);

  chain.SetBranchAddress("Event_bWeightMisTagUp2CSVM", &bWeight2MisTagUp);
  chain.SetBranchAddress("Event_bWeightMisTagDown2CSVM", &bWeight2MisTagDown);
  chain.SetBranchAddress("Event_bWeightBTagUp2CSVM", &bWeight2BTagUp);
  chain.SetBranchAddress("Event_bWeightBTagDown2CSVM", &bWeight2BTagDown);

  chain.SetBranchAddress("Event_bWeight1CSVM_subj", &bWeight1_subj);

  chain.SetBranchAddress("Event_bWeightMisTagUp1CSVM_subj", &bWeight1MisTagUp_subj);
  chain.SetBranchAddress("Event_bWeightMisTagDown1CSVM_subj", &bWeight1MisTagDown_subj);
  chain.SetBranchAddress("Event_bWeightBTagUp1CSVM_subj", &bWeight1BTagUp_subj);
  chain.SetBranchAddress("Event_bWeightBTagDown1CSVM_subj", &bWeight1BTagDown_subj);

  chain.SetBranchAddress("Event_bWeight0CSVM_subj", &bWeight0_subj);

  chain.SetBranchAddress("Event_bWeightMisTagUp0CSVM_subj", &bWeight0MisTagUp_subj);
  chain.SetBranchAddress("Event_bWeightMisTagDown0CSVM_subj", &bWeight0MisTagDown_subj);
  chain.SetBranchAddress("Event_bWeightBTagUp0CSVM_subj", &bWeight0BTagUp_subj);
  chain.SetBranchAddress("Event_bWeightBTagDown0CSVM_subj", &bWeight0BTagDown_subj);

  chain.SetBranchAddress("Event_bWeight2CSVM_subj", &bWeight2_subj);

  chain.SetBranchAddress("Event_bWeightMisTagUp2CSVM_subj", &bWeight2MisTagUp_subj);
  chain.SetBranchAddress("Event_bWeightMisTagDown2CSVM_subj", &bWeight2MisTagDown_subj);
  chain.SetBranchAddress("Event_bWeightBTagUp2CSVM_subj", &bWeight2BTagUp_subj);
  chain.SetBranchAddress("Event_bWeightBTagDown2CSVM_subj", &bWeight2BTagDown_subj);
  
  /********************************************************************************/
  /**************                    Histogram booking              ***************/
  /********************************************************************************/

  TH1F *h_cutFlow  = new TH1F("h_cutFlow","cutFlow",8,-0.5,7.5);
  TH1F *h_nPV   [maxSysts] ;systZero.initHistogramsSysts(h_nPV,"h_nPV","nPV",100,0,100);
  TH1F *h_nPV_w   [maxSysts] ;systZero.initHistogramsSysts(h_nPV_w,"h_nPV_w","nPV",100,0,100);

  TH1F *h_Ht   [maxSysts] ;systZero.initHistogramsSysts(h_Ht,"h_Ht","Ht",300,0,3000);
  TH1F *h_Ht_bef   [maxSysts] ;systZero.initHistogramsSysts(h_Ht_bef,"h_Ht_bef","Ht",300,0,3000);
  TH1F *h_Ht_trigaft   [maxSysts] ;systZero.initHistogramsSysts(h_Ht_trigaft,"h_Ht_trigaft","Ht",300,0,3000);
  
  TH1F *h_AK8jetpt [maxSysts];systZero.initHistogramsSysts(h_AK8jetpt,"h_AK8pt","AK8pt",100,0,1000);
  TH1F *h_AK8jeteta [maxSysts];systZero.initHistogramsSysts(h_AK8jeteta,"h_AK8eta","AK8eta",100,-5,5);
  TH1F *h_AK8jetphi [maxSysts];systZero.initHistogramsSysts(h_AK8jetphi,"h_AK8phi","AK8phi",100,-7,7);
  TH1F *h_AK8jetmult [maxSysts];systZero.initHistogramsSysts(h_AK8jetmult,"h_AK8mult","AK8 mult",20,-0.5,19.5);
  TH1F *h_nsubj [maxSysts];systZero.initHistogramsSysts(h_nsubj,"h_nsubj","nsubj",3,-0.5,2.5);
  TH1F *h_tau2tau1 [maxSysts];systZero.initHistogramsSysts(h_tau2tau1,"h_tau2tau1","tau2tau1",100,0,1);
  TH1F *h_prunedmass [maxSysts];systZero.initHistogramsSysts(h_prunedmass,"h_prunedmass","prunedmass",100,0,500);

  TH1F *h_AK4jetptsublead [maxSysts];systZero.initHistogramsSysts(h_AK4jetptsublead,"h_AK4ptsublead","AK4pt",100,0,1000);
  TH1F *h_AK4jetetasublead [maxSysts];systZero.initHistogramsSysts(h_AK4jetetasublead,"h_AK4etasublead","AK4eta",100,-5,5);
  TH1F *h_AK4jetphisublead [maxSysts];systZero.initHistogramsSysts(h_AK4jetphisublead,"h_AK4phisublead","AK4phi",100,-7,7);
  TH1F *h_AK4jetptlead [maxSysts];systZero.initHistogramsSysts(h_AK4jetptlead,"h_AK4ptlead","AK4pt",100,0,1000);
  TH1F *h_AK4jetetalead [maxSysts];systZero.initHistogramsSysts(h_AK4jetetalead,"h_AK4etalead","AK4eta",100,-5,5);
  TH1F *h_AK4jetphilead [maxSysts];systZero.initHistogramsSysts(h_AK4jetphilead,"h_AK4philead","AK4phi",100,-7,7);

  TH1F *h_AK4bptsublead [maxSysts];systZero.initHistogramsSysts(h_AK4bptsublead,"h_AK4bptsublead","AK4pt",100,0,1000);
  TH1F *h_AK4betasublead [maxSysts];systZero.initHistogramsSysts(h_AK4betasublead,"h_AK4betasublead","AK4eta",100,-5,5);
  TH1F *h_AK4bphisublead [maxSysts];systZero.initHistogramsSysts(h_AK4bphisublead,"h_AK4bphisublead","AK4phi",100,-7,7);
  TH1F *h_AK4bptlead [maxSysts];systZero.initHistogramsSysts(h_AK4bptlead,"h_AK4bptlead","AK4pt",100,0,1000);
  TH1F *h_AK4betalead [maxSysts];systZero.initHistogramsSysts(h_AK4betalead,"h_AK4betalead","AK4eta",100,-5,5);
  TH1F *h_AK4bphilead [maxSysts];systZero.initHistogramsSysts(h_AK4bphilead,"h_AK4bphilead","AK4phi",100,-7,7);

  TH1F *h_AK4fwjetptsublead [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetptsublead,"h_AK4fwptsublead","AK4pt",100,0,1000);
  TH1F *h_AK4fwjetetasublead [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetetasublead,"h_AK4fwetasublead","AK4eta",100,-5,5);
  TH1F *h_AK4fwjetphisublead [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetphisublead,"h_AK4fwphisublead","AK4phi",100,-7,7);
  TH1F *h_AK4fwjetptlead [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetptlead,"h_AK4fwptlead","AK4pt",100,0,1000);
  TH1F *h_AK4fwjetetalead [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetetalead,"h_AK4fwetalead","AK4eta",100,-5,5);
  TH1F *h_AK4fwjetphilead [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetphilead,"h_AK4fwphilead","AK4phi",100,-7,7);
  TH1F *h_AK4fwjetptlead_2p43 [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetptlead_2p43,"h_AK4fwptlead_2p43","AK4pt_2p43",100,0,1000);
  TH1F *h_AK4fwjetetalead_2p43 [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetetalead_2p43,"h_AK4fwetalead_2p43","AK4eta_2p43",100,-5,5);
  TH1F *h_AK4fwjetphilead_2p43 [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetphilead_2p43,"h_AK4fwphilead_2p43","AK4phi_2p43",100,-7,7);
  TH1F *h_AK4fwjetptlead_34p7 [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetptlead_34p7,"h_AK4fwptlead_34p7","AK4pt_34p7",100,0,1000);
  TH1F *h_AK4fwjetetalead_34p7 [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetetalead_34p7,"h_AK4fwetalead_34p7","AK4eta_34p7",100,-5,5);
  TH1F *h_AK4fwjetphilead_34p7 [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetphilead_34p7,"h_AK4fwphilead_34p7","AK4phi_34p7",100,-7,7);
  
  TH1F *h_AK4jetpt [maxSysts];systZero.initHistogramsSysts(h_AK4jetpt,"h_AK4pt","AK4pt",100,0,1000);
  TH1F *h_AK4jeteta [maxSysts];systZero.initHistogramsSysts(h_AK4jeteta,"h_AK4eta","AK4eta",100,-5,5);
  TH1F *h_AK4jetphi [maxSysts];systZero.initHistogramsSysts(h_AK4jetphi,"h_AK4phi","AK4phi",100,-7,7);
  TH1F *h_AK4jetcsv [maxSysts];systZero.initHistogramsSysts(h_AK4jetcsv,"h_AK4csv","AK4csv",100,0,1);
  TH1F *h_AK4jetmult [maxSysts];systZero.initHistogramsSysts(h_AK4jetmult,"h_AK4mult","AK4 mult",20,-0.5,19.5);
  TH1F *h_AK4bjetmult [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmult,"h_AK4bmult","AK4 b-tagged mult",20,-0.5,19.5);
  TH1F *h_AK4bjetmultaft [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmultaft,"h_AK4bmultaft","AK4 b-tagged mult",20,-0.5,19.5);
  TH1F *h_AK4jetmultaft [maxSysts];systZero.initHistogramsSysts(h_AK4jetmultaft,"h_AK4multaft","AK4 jet multiplicity",20,-0.5,19.5);
  TH1F *h_AK4bjetmultaft_nH [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmultaft_nH,"h_AK4bmultaft_nH","AK4 b-tagged jets multiplicity",20,-0.5,19.5);

  TH1F *h_deltaRbH [maxSysts];systZero.initHistogramsSysts(h_deltaRbH ,"h_deltaRbH","deltaRbH",100,0,5);
  
  TH1F *h_AK8jetmultaft_SR [maxSysts];systZero.initHistogramsSysts(h_AK8jetmultaft_SR,"h_AK8mult aft_SR","AK8 mult aft_SR",20,-0.5,19.5);
  TH1F *h_AK4fwjetpt [maxSysts];systZero.initHistogramsSysts(h_AK4fwjetpt,"h_AK4fwjetpt","AK4pt",100,0,1000);
  TH1F *h_AK4fwjeteta [maxSysts];systZero.initHistogramsSysts(h_AK4fwjeteta,"h_AK4fwjeteta","AK4eta",100,-6,6);
  TH1F *h_AK4cjetpt [maxSysts];systZero.initHistogramsSysts(h_AK4cjetpt,"h_AK4cjetpt","AK4pt",100,0,1000);
  TH1F *h_AK4cjeteta [maxSysts];systZero.initHistogramsSysts(h_AK4cjeteta,"h_AK4cjeteta","AK4eta",100,-6,6);
  TH1F *h_AK4cjetcsv [maxSysts];systZero.initHistogramsSysts(h_AK4cjetcsv,"h_AK4cjetcsv","AK4csv",100,0,1);
  TH1F *h_AK4bjetpt [maxSysts];systZero.initHistogramsSysts(h_AK4bjetpt,"h_AK4bjetpt","AK4pt",100,0,1000);
  TH1F *h_AK4bjeteta [maxSysts];systZero.initHistogramsSysts(h_AK4bjeteta,"h_AK4bjeteta","AK4eta",100,-6,6);

  TH1F *h_AK4bjetmultaft_SR [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmultaft_SR,"h_AK4bmultaft_SR","AK4 b-tagged mult",20,-0.5,19.5);
  TH1F *h_AK4jetmultaft_SR [maxSysts];systZero.initHistogramsSysts(h_AK4jetmultaft_SR,"h_AK4mult aft_SR","AK4 mult aft_SR",20,-0.5,19.5);
  TH1F *h_AK4fwjets [maxSysts]; systZero.initHistogramsSysts(h_AK4fwjets, "h_AK4fwjets", "AK4 forward jets multiplicity", 10, -0.5, 9.5);
  TH1F *h_AK4fwjets_SR [maxSysts]; systZero.initHistogramsSysts(h_AK4fwjets_SR, "h_AK4fwjets_SR", "AK4 forward jets multiplicity", 10, -0.5, 9.5);
  TH1F *h_AK4fwjets_CRB [maxSysts]; systZero.initHistogramsSysts(h_AK4fwjets_CRB, "h_AK4fwjets_CRB", "AK4 forward jets multiplicity", 10, -0.5, 9.5);
  TH1F *h_AK4fwjets_CRC [maxSysts]; systZero.initHistogramsSysts(h_AK4fwjets_CRC, "h_AK4fwjets_CRC", "AK4 forward jets multiplicity", 10, -0.5, 9.5);
  TH1F *h_AK4fwjets_CRD [maxSysts]; systZero.initHistogramsSysts(h_AK4fwjets_CRD, "h_AK4fwjets_CRD", "AK4 forward jets multiplicity", 10, -0.5, 9.5);
  TH1F *h_AK4cjets [maxSysts]; systZero.initHistogramsSysts(h_AK4cjets, "h_AK4cjets", "AK4 central jets multiplicity", 20, -0.5, 19.5);
  TH1F *h_AK4bjets [maxSysts]; systZero.initHistogramsSysts(h_AK4bjets, "h_AK4bjets", "AK4 b-tagged jets multiplicity", 10, -0.5, 9.5);

  TH1F *h_bprimept_SR [maxSysts];systZero.initHistogramsSysts(h_bprimept_SR,"h_bprimept_SR","bprimept",100,0,1000);
  TH1F *h_bprimeeta_SR[maxSysts];systZero.initHistogramsSysts(h_bprimeeta_SR,"h_bprimeeta_SR","bprimeeta",100,-5,5);
  TH1F *h_bprimephi_SR [maxSysts];systZero.initHistogramsSysts(h_bprimephi_SR,"h_bprimephi_SR","bprimephi",100,-7,7);
  
  TH1F *h_nsubj_SR [maxSysts];systZero.initHistogramsSysts(h_nsubj_SR,"h_nsubj_SR","nsubj",3,-0.5,2.5);
  TH1F *h_tau2tau1_SR [maxSysts];systZero.initHistogramsSysts(h_tau2tau1_SR,"h_tau2tau1_SR","tau2tau1",100,0,1);
  TH1F *h_prunedmass_SR [maxSysts];systZero.initHistogramsSysts(h_prunedmass_SR,"h_prunedmass_SR","prunedmass",100,0,500);
  
  TH1F *h_AK8jet_selh_pt_SR [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_pt_SR,"h_AK8_selh_pt_SR","AK8pt",100,0,1000);
  TH1F *h_AK8jet_selh_eta_SR [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_eta_SR,"h_AK8_selh_eta_SR","AK8eta",100,-5,5);
  TH1F *h_AK8jet_selh_phi_SR [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_phi_SR,"h_AK8_selh_phi_SR","AK8phi",100,-7,7);

  TH1F *h_AK4jet_selb_pt_SR [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_pt_SR,"h_AK4_selb_pt_SR","AK4pt",100,0,1000);
  TH1F *h_AK4jet_selb_eta_SR [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_eta_SR,"h_AK4_selb_eta_SR","AK4eta",100,-5,5);
  TH1F *h_AK4jet_selb_phi_SR [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_phi_SR,"h_AK4_selb_phi_SR","AK4phi",100,-7,7);

  TH1F *h_bprimemass_SR   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_SR,"h_bprimemass_SR","bprimemass",300,0,3000);
  TH1F *h_weight10 [maxSysts]; systZero.initHistogramsSysts(h_weight10, "h_weight10", "h_weight10", 2000, 0, 2);
  TH1F *h_weight50 [maxSysts]; systZero.initHistogramsSysts(h_weight50, "h_weight50", "h_weight50", 2000, 0, 2);
  TH1F *h_weight10_aft [maxSysts]; systZero.initHistogramsSysts(h_weight10_aft, "h_weight10_aft", "h_weight10_aft", 2000, 0, 2);
  TH1F *h_weight50_aft [maxSysts]; systZero.initHistogramsSysts(h_weight50_aft, "h_weight50_aft", "h_weight50_aft", 2000, 0, 2);
  TH1F *h_bprimemass_SR_1   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_SR_1,"h_bprimemass_SR_1","bprimemass_1",300,0,3000);
  TH1F *h_bprimemass_SR_2   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_SR_2,"h_bprimemass_SR_2","bprimemass_2",300,0,3000);
  TH1F *h_bprimemass_SR_3   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_SR_3,"h_bprimemass_SR_3","bprimemass_3",300,0,3000);
  TH1F *h_bprimemass_SR_4   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_SR_4,"h_bprimemass_SR_4","bprimemass_4",300,0,3000);
  TH1F *h_bprimemass_SR_5   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_SR_5,"h_bprimemass_SR_5","bprimemass_5",300,0,3000);
  TH1F *h_Ht_SR   [maxSysts] ;systZero.initHistogramsSysts(h_Ht_SR,"h_Ht_SR","Ht_SR",300,0,3000);
  
  //CONTROL REGION PLOTS
  TH1F *h_AK8jetmultaft_CRB [maxSysts];systZero.initHistogramsSysts(h_AK8jetmultaft_CRB,"h_AK8mult aft_CRB","AK8 mult aft_CRB",20,-0.5,19.5);
  TH1F *h_AK4bjetmultaft_CRB [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmultaft_CRB,"h_AK4bmultaft_CRB","AK4 b-tagged mult",20,-0.5,19.5);
  TH1F *h_AK4jetmultaft_CRB [maxSysts];systZero.initHistogramsSysts(h_AK4jetmultaft_CRB,"h_AK4mult aft_CRB","AK4 mult aft_CRB",20,-0.5,19.5);

  TH1F *h_AK8jetmultaft_CRC [maxSysts];systZero.initHistogramsSysts(h_AK8jetmultaft_CRC,"h_AK8mult aft_CRC","AK8 mult aft_CRC",20,-0.5,19.5);
  TH1F *h_AK4bjetmultaft_CRC [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmultaft_CRC,"h_AK4bmultaft_CRC","AK4 b-tagged mult",20,-0.5,19.5);
  TH1F *h_AK4jetmultaft_CRC [maxSysts];systZero.initHistogramsSysts(h_AK4jetmultaft_CRC,"h_AK4mult aft_CRC","AK4 mult aft_CRC",20,-0.5,19.5);

  TH1F *h_AK8jetmultaft_CRD [maxSysts];systZero.initHistogramsSysts(h_AK8jetmultaft_CRD,"h_AK8mult aft_CRD","AK8 mult aft_CRD",20,-0.5,19.5);
  TH1F *h_AK4bjetmultaft_CRD [maxSysts];systZero.initHistogramsSysts(h_AK4bjetmultaft_CRD,"h_AK4bmultaft_CRD","AK4 b-tagged mult",20,-0.5,19.5);
  TH1F *h_AK4jetmultaft_CRD [maxSysts];systZero.initHistogramsSysts(h_AK4jetmultaft_CRD,"h_AK4mult aft_CRD","AK4 mult aft_CRD",20,-0.5,19.5);

  TH1F *h_Ht_CRB   [maxSysts] ;systZero.initHistogramsSysts(h_Ht_CRB,"h_Ht_CRB","Ht",300,0,3000);
  TH1F *h_Ht_CRC   [maxSysts] ;systZero.initHistogramsSysts(h_Ht_CRC,"h_Ht_CRC","Ht",300,0,3000);
  TH1F *h_Ht_CRD   [maxSysts] ;systZero.initHistogramsSysts(h_Ht_CRD,"h_Ht_CRD","Ht",300,0,3000);
  
  TH1F *h_bprimemass_CRB   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_CRB,"h_bprimemass_CRB","bprimemass",300,0,3000);
  TH1F *h_bprimemass_CRC   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_CRC,"h_bprimemass_CRC","bprimemass",300,0,3000);
  TH1F *h_bprimemass_CRD   [maxSysts] ;systZero.initHistogramsSysts(h_bprimemass_CRD,"h_bprimemass_CRD","bprimemass",300,0,3000);

  TH1F *h_bprimept_CRB [maxSysts];systZero.initHistogramsSysts(h_bprimept_CRB,"h_bprimept_CRB","bprimept",100,0,1000);
  TH1F *h_bprimeeta_CRB[maxSysts];systZero.initHistogramsSysts(h_bprimeeta_CRB,"h_bprimeeta_CRB","bprimeeta",100,-5,5);
  TH1F *h_bprimephi_CRB [maxSysts];systZero.initHistogramsSysts(h_bprimephi_CRB,"h_bprimephi_CRB","bprimephi",100,-7,7);
  
  TH1F *h_nsubj_CRB [maxSysts];systZero.initHistogramsSysts(h_nsubj_CRB,"h_nsubj_CRB","nsubj",3,-0.5,2.5);
  TH1F *h_tau2tau1_CRB [maxSysts];systZero.initHistogramsSysts(h_tau2tau1_CRB,"h_tau2tau1_CRB","tau2tau1",100,0,1);
  TH1F *h_prunedmass_CRB [maxSysts];systZero.initHistogramsSysts(h_prunedmass_CRB,"h_prunedmass_CRB","prunedmass",100,0,500);
  
  TH1F *h_AK8jet_selh_pt_CRB [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_pt_CRB,"h_AK8_selh_pt_CRB","AK8pt",100,0,1000);
  TH1F *h_AK8jet_selh_eta_CRB [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_eta_CRB,"h_AK8_selh_eta_CRB","AK8eta",100,-5,5);
  TH1F *h_AK8jet_selh_phi_CRB [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_phi_CRB,"h_AK8_selh_phi_CRB","AK8phi",100,-7,7);

  TH1F *h_AK4jet_selb_pt_CRB [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_pt_CRB,"h_AK4_selb_pt_CRB","AK4pt",100,0,1000);
  TH1F *h_AK4jet_selb_eta_CRB [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_eta_CRB,"h_AK4_selb_eta_CRB","AK4eta",100,-5,5);
  TH1F *h_AK4jet_selb_phi_CRB [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_phi_CRB,"h_AK4_selb_phi_CRB","AK4phi",100,-7,7);

  TH1F *h_bprimept_CRC [maxSysts];systZero.initHistogramsSysts(h_bprimept_CRC,"h_bprimept_CRC","bprimept",100,0,1000);
  TH1F *h_bprimeeta_CRC[maxSysts];systZero.initHistogramsSysts(h_bprimeeta_CRC,"h_bprimeeta_CRC","bprimeeta",100,-5,5);
  TH1F *h_bprimephi_CRC [maxSysts];systZero.initHistogramsSysts(h_bprimephi_CRC,"h_bprimephi_CRC","bprimephi",100,-7,7);
  
  TH1F *h_nsubj_CRC [maxSysts];systZero.initHistogramsSysts(h_nsubj_CRC,"h_nsubj_CRC","nsubj",3,-0.5,2.5);
  TH1F *h_tau2tau1_CRC [maxSysts];systZero.initHistogramsSysts(h_tau2tau1_CRC,"h_tau2tau1_CRC","tau2tau1",100,0,1);
  TH1F *h_prunedmass_CRC [maxSysts];systZero.initHistogramsSysts(h_prunedmass_CRC,"h_prunedmass_CRC","prunedmass",100,0,500);
  
  TH1F *h_AK8jet_selh_pt_CRC [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_pt_CRC,"h_AK8_selh_pt_CRC","AK8pt",100,0,1000);
  TH1F *h_AK8jet_selh_eta_CRC [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_eta_CRC,"h_AK8_selh_eta_CRC","AK8eta",100,-5,5);
  TH1F *h_AK8jet_selh_phi_CRC [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_phi_CRC,"h_AK8_selh_phi_CRC","AK8phi",100,-7,7);

  TH1F *h_AK4jet_selb_pt_CRC [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_pt_CRC,"h_AK4_selb_pt_CRC","AK4pt",100,0,1000);
  TH1F *h_AK4jet_selb_eta_CRC [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_eta_CRC,"h_AK4_selb_eta_CRC","AK4eta",100,-5,5);
  TH1F *h_AK4jet_selb_phi_CRC [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_phi_CRC,"h_AK4_selb_phi_CRC","AK4phi",100,-7,7);

  TH1F *h_bprimept_CRD [maxSysts];systZero.initHistogramsSysts(h_bprimept_CRD,"h_bprimept_CRD","bprimept",100,0,1000);
  TH1F *h_bprimeeta_CRD[maxSysts];systZero.initHistogramsSysts(h_bprimeeta_CRD,"h_bprimeeta_CRD","bprimeeta",100,-5,5);
  TH1F *h_bprimephi_CRD [maxSysts];systZero.initHistogramsSysts(h_bprimephi_CRD,"h_bprimephi_CRD","bprimephi",100,-7,7);
  
  TH1F *h_nsubj_CRD [maxSysts];systZero.initHistogramsSysts(h_nsubj_CRD,"h_nsubj_CRD","nsubj",3,-0.5,2.5);
  TH1F *h_tau2tau1_CRD [maxSysts];systZero.initHistogramsSysts(h_tau2tau1_CRD,"h_tau2tau1_CRD","tau2tau1",100,0,1);
  TH1F *h_prunedmass_CRD [maxSysts];systZero.initHistogramsSysts(h_prunedmass_CRD,"h_prunedmass_CRD","prunedmass",100,0,500);
  
  TH1F *h_AK8jet_selh_pt_CRD [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_pt_CRD,"h_AK8_selh_pt_CRD","AK8pt",100,0,1000);
  TH1F *h_AK8jet_selh_eta_CRD [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_eta_CRD,"h_AK8_selh_eta_CRD","AK8eta",100,-5,5);
  TH1F *h_AK8jet_selh_phi_CRD [maxSysts];systZero.initHistogramsSysts(h_AK8jet_selh_phi_CRD,"h_AK8_selh_phi_CRD","AK8phi",100,-7,7);

  TH1F *h_AK4jet_selb_pt_CRD [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_pt_CRD,"h_AK4_selb_pt_CRD","AK4pt",100,0,1000);
  TH1F *h_AK4jet_selb_eta_CRD [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_eta_CRD,"h_AK4_selb_eta_CRD","AK4eta",100,-5,5);
  TH1F *h_AK4jet_selb_phi_CRD [maxSysts];systZero.initHistogramsSysts(h_AK4jet_selb_phi_CRD,"h_AK4_selb_phi_CRD","AK4phi",100,-7,7);

  TH1F *h_nHiggsCand_A [maxSysts]; systZero.initHistogramsSysts(h_nHiggsCand_A,"h_nHiggsCand_A","h_nHiggsCand_A",10,-0.5,9.5);
  TH1F *h_nHiggsCand_B [maxSysts]; systZero.initHistogramsSysts(h_nHiggsCand_B,"h_nHiggsCand_B","h_nHiggsCand_B",10,-0.5,9.5);
  TH1F *h_nHiggsCand_C [maxSysts]; systZero.initHistogramsSysts(h_nHiggsCand_C,"h_nHiggsCand_C","h_nHiggsCand_C",10,-0.5,9.5);
  TH1F *h_nHiggsCand_D [maxSysts]; systZero.initHistogramsSysts(h_nHiggsCand_D,"h_nHiggsCand_D","h_nHiggsCand_D",10,-0.5,9.5);

  TH1F *h_bCandpt_A [maxSysts];systZero.initHistogramsSysts(h_bCandpt_A,"h_bCandpt_A","h_bCandpt_A",100,0,1000);
  TH1F *h_bCandeta_A [maxSysts];systZero.initHistogramsSysts(h_bCandeta_A,"h_bCandeta_A","h_bCandeta_A",100,-5,5);
  TH1F *h_bCandphi_A [maxSysts];systZero.initHistogramsSysts(h_bCandphi_A,"h_bCandphi_A","h_bCandphi_A",100,-7,7);
  TH1F *h_bCandmult_A [maxSysts];systZero.initHistogramsSysts(h_bCandmult_A,"h_bCandmult_A","h_bCandmult_A",10,-0.5,9.5);
  TH1F *h_hCandpt_A [maxSysts];systZero.initHistogramsSysts(h_hCandpt_A,"h_hCandpt_A","h_hCandpt_A",100,0,1000);
  TH1F *h_hCandeta_A [maxSysts];systZero.initHistogramsSysts(h_hCandeta_A,"h_hCandeta_A","h_hCandeta_A",100,-5,5);
  TH1F *h_hCandphi_A [maxSysts];systZero.initHistogramsSysts(h_hCandphi_A,"h_hCandphi_A","h_hCandphi_A",100,-7,7);
  TH1F *h_hCandmult_A [maxSysts];systZero.initHistogramsSysts(h_hCandmult_A,"h_hCandmult_A","h_hCandmult_A",10,-0.5,9.5);
  TH1F *h_bjetpt [maxSysts];systZero.initHistogramsSysts(h_bjetpt,"h_bjetpt","h_bjetpt",100,0,1000);
  TH1F *h_bjeteta [maxSysts];systZero.initHistogramsSysts(h_bjeteta,"h_bjeteta","h_bjeteta",100,-5,5);
  TH1F *h_bjetphi [maxSysts];systZero.initHistogramsSysts(h_bjetphi,"h_bjetphi","h_bjetphi",100,-7,7);
  TH1F *h_bjetmult [maxSysts];systZero.initHistogramsSysts(h_bjetmult,"h_bjetmult","h_bjetmult",10,-0.5,9.5);
  TH1F *h_fwjetmult [maxSysts];systZero.initHistogramsSysts(h_fwjetmult,"h_fwjetmult","h_fwjetmult",10,-0.5,9.5);
  TH1F *h_fwjetmult_2p43 [maxSysts];systZero.initHistogramsSysts(h_fwjetmult_2p43,"h_fwjetmult_2p43","h_fwjetmult_2p43",10,-0.5,9.5);
  TH1F *h_fwjetmult_34p7 [maxSysts];systZero.initHistogramsSysts(h_fwjetmult_34p7,"h_fwjetmult_34p7","h_fwjetmult_34p7",10,-0.5,9.5);

  float systWeights1B2sB[maxSysts], systWeights1B1sB[maxSysts],  systWeights1B0sB[maxSysts], systWeights0B0sB[maxSysts];//, systWeights2B0sB[maxSysts];
  //float systWeightsNoSyst[maxSysts];

  //for pile-up reweighting
  float w_pu;
  float LHEWeightSign[1] = {1.};

  string outFileName =outdir + "/res/"+sample + "_" +cat+ "_" +channel+".root";

  bool onlyNominal=false;
  systZero.setOnlyNominal(onlyNominal);
  syst1B2sB.setOnlyNominal(onlyNominal);
  syst1B1sB.setOnlyNominal(onlyNominal);
  //syst2B0sB.setOnlyNominal(onlyNominal);
  syst1B0sB.setOnlyNominal(onlyNominal);
  syst0B0sB.setOnlyNominal(onlyNominal);
    
  systZero.createFilesSysts(allMyFiles,outdir+"/res/"+sample + "_" + cat +"_" +channel+syststr);

  edm::LumiReWeighting LumiWeights_, LumiWeightsUp_, LumiWeightsDown_;
 
  if(isData=="MC"){
    LumiWeights_ = edm::LumiReWeighting("data_Mo17/puMC.root", "data_Mo17/MyDataPileupHistogram.root","MC_pu","pileup");
    LumiWeightsUp_ = edm::LumiReWeighting("data_Mo17/puMC.root", "data_Mo17/MyDataPileupHistogramUP.root","MC_pu","pileup");
    LumiWeightsDown_ = edm::LumiReWeighting("data_Mo17/puMC.root", "data_Mo17/MyDataPileupHistogramDOWN.root","MC_pu","pileup");
  }
  
  kFactor wQCD("WQCD");
  kFactor wEWK("WEWK");
  kFactor wQCDrenUp("WQCDrenUp");
  kFactor wQCDrenDown("WQCDrenDown");
  kFactor wQCDfacUp("WQCDfacUp");
  kFactor wQCDfacDown("WQCDfacDown");
  
  kFactor zQCD("ZQCD");
  kFactor zEWK("ZEWK");
  kFactor zQCDrenUp("ZQCDrenUp");
  kFactor zQCDrenDown("ZQCDrenDown");
  kFactor zQCDfacUp("ZQCDfacUp");
  kFactor zQCDfacDown("ZQCDfacDown");
  
  float kfact(1.);
  float kfact_qcd(1.),  kfact_ewk(1.);
  float kfact_qcdrenUp(1.), kfact_qcdrenDown(1.), kfact_qcdfacUp(1.), kfact_qcdfacDown(1.), kfact_ewkUp(1.) ,kfact_ewkDown(1.);
  //nEventsPrePres=10000;
 
  for(Int_t i=0; i<nEventsPrePres; i++ )
    {
      if((METFilters && BadChargedCandidateFilter && BadPFMuonFilter)>0){
      if(i%100000==1 ){
	cout<<"Running on event: "<<i<<endl; 
      }
      w = LHEWeightSign[0];
      chain.GetEntry(i);
      
      if( !strncmp(sample.c_str(), Wlabel , strlen(Wlabel))) {
        kfact_qcd = wQCD.getkFact(WPt);
        kfact_ewk = wEWK.getkFact(WPt);
	
	kfact_qcdrenUp = wQCDrenUp.getSyst(WPt); 
	kfact_qcdrenDown = wQCDrenDown.getSyst(WPt); 
	kfact_qcdfacUp = wQCDfacUp.getSyst(WPt); 
	kfact_qcdfacDown = wQCDfacDown.getSyst(WPt); 
	
	kfact_ewkUp=1.;
	kfact_ewkDown=kfact_ewk;
	
	kfact =  kfact_qcd *  kfact_ewk;
	k_fact = kfact;
      }
      
      else if( !strncmp(sample.c_str(), Zlabel , strlen(Zlabel))  or !strncmp(sample.c_str(), Zlabel , strlen(DYlabel)) ) {
        kfact_qcd = zQCD.getkFact(ZPt);
        kfact_ewk = zEWK.getkFact(ZPt);
	
	kfact_qcdrenUp = zQCDrenUp.getSyst(ZPt); 
	kfact_qcdrenDown = zQCDrenDown.getSyst(ZPt); 
	kfact_qcdfacUp = zQCDfacUp.getSyst(ZPt); 
	kfact_qcdfacDown = zQCDfacDown.getSyst(ZPt); 
	
	kfact_ewkUp=1.;
	kfact_ewkDown=kfact_ewk;
	
	kfact =  kfact_qcd *  kfact_ewk;
	k_fact = kfact;
      }
     else{
       
       kfact =  1.;
     }
        
      if(isData=="MC"){
	w = LHEWeightSign[0];
	w_pu = LumiWeights_.weight(numTrueInt);
	w = w * w_pu;
	
	if(sample=="TT"){
	  w*=w_top/topWeight;
	}
	if((samplestr).find("BprimeBToHB") != std::string::npos){
	  if(addQ2) w_zero = w_zero * q2SplittedWeight;
	}
	
	vhf=(int)eventFlavour;
      }
      
      double  wcats[10]={1.,1.,1.,1.,1.,1.,1.,1.,1.,1.};
      
      if(isData=="DATA"){
	
	systZero.setWeight(0,1.);
	systZero.setWeight("btagUp",1.);
	systZero.setWeight("btagDown",1.);
	systZero.setWeight("mistagUp",1.);
	systZero.setWeight("mistagDown",1.);
	systZero.setWeight("puDown",1.);
	systZero.setWeight("puUp",1.);
	systZero.setWeight("mistagHiggsDown",1.);
	systZero.setWeight("mistagHiggsUp",1.);
	
	syst0B0sB.copySysts(systZero);
        syst0B0sB.setWeight("btagUp",1.);
        syst0B0sB.setWeight("btagDown",1.);
	
        systWeights0B0sB[NOSYST]=1.;
        systWeights0B0sB[BTAGUP]=1.;
	systWeights0B0sB[BTAGDOWN]=1.;
        systWeights0B0sB[MISTAGUP]=1.;
        systWeights0B0sB[MISTAGDOWN]=1.;
        systWeights0B0sB[PUUP]=1.;
        systWeights0B0sB[PUDOWN]=1.;
	systWeights0B0sB[MISTAGHIGGSUP]=1.;
	systWeights0B0sB[MISTAGHIGGSDOWN]=1.;
	
	syst1B2sB.setWeight("btagUp",1.);
	syst1B2sB.setWeight("btagDown",1.);
	
	systWeights1B2sB[NOSYST]=1.;
	systWeights1B2sB[BTAGUP]=1.;
	systWeights1B2sB[BTAGDOWN]=1.;
	systWeights1B2sB[MISTAGUP]=1.;
	systWeights1B2sB[MISTAGDOWN]=1.;
	systWeights1B2sB[PUUP]=1.;
	systWeights1B2sB[PUDOWN]=1.;
	systWeights1B2sB[MISTAGHIGGSUP]=1.;
	systWeights1B2sB[MISTAGHIGGSDOWN]=1.;

	syst1B2sB.copySysts(systZero);
	syst1B2sB.setWeight("btagUp",1.);
	syst1B2sB.setWeight("btagDown",1.);
	
	systWeights1B2sB[NOSYST]=1.;
	systWeights1B2sB[BTAGUP]=1.;
	systWeights1B2sB[BTAGDOWN]=1.;
	systWeights1B2sB[MISTAGUP]=1.;
	systWeights1B2sB[MISTAGDOWN]=1.;
	systWeights1B2sB[PUUP]=1.;
	systWeights1B2sB[PUDOWN]=1.;
	systWeights1B2sB[MISTAGHIGGSUP]=1.;
	systWeights1B2sB[MISTAGHIGGSDOWN]=1.;

	systWeights1B1sB[NOSYST]=1.;
	systWeights1B1sB[BTAGUP]=1.;
	systWeights1B1sB[BTAGDOWN]=1.;
	systWeights1B1sB[MISTAGUP]=1.;
	systWeights1B1sB[MISTAGDOWN]=1.;
	systWeights1B1sB[PUUP]=1.;
	systWeights1B1sB[PUDOWN]=1.;
	systWeights1B1sB[MISTAGHIGGSUP]=1.;
	systWeights1B1sB[MISTAGHIGGSDOWN]=1.;

	syst1B1sB.copySysts(systZero);
	syst1B1sB.setWeight("btagUp",1.);
	syst1B1sB.setWeight("btagDown",1.);
	
	systWeights1B1sB[NOSYST]=1.;
	systWeights1B1sB[BTAGUP]=1.;
	systWeights1B1sB[BTAGDOWN]=1.;
	systWeights1B1sB[MISTAGUP]=1.;
	systWeights1B1sB[MISTAGDOWN]=1.;
	systWeights1B1sB[PUUP]=1.;
	systWeights1B1sB[PUDOWN]=1.;
	systWeights1B1sB[MISTAGHIGGSUP]=1.;
	systWeights1B1sB[MISTAGHIGGSDOWN]=1.;

	systWeights1B0sB[NOSYST]=1.;
	systWeights1B0sB[BTAGUP]=1.;
	systWeights1B0sB[BTAGDOWN]=1.;
	systWeights1B0sB[MISTAGUP]=1.;
	systWeights1B0sB[MISTAGDOWN]=1.;
	systWeights1B0sB[PUUP]=1.;
	systWeights1B0sB[PUDOWN]=1.;
	systWeights1B0sB[MISTAGHIGGSUP]=1.;
	systWeights1B0sB[MISTAGHIGGSDOWN]=1.;

	syst1B0sB.copySysts(systZero);
	syst1B0sB.setWeight("btagUp",1.);
	syst1B0sB.setWeight("btagDown",1.);
	
	systWeights1B0sB[NOSYST]=1.;
	systWeights1B0sB[BTAGUP]=1.;
	systWeights1B0sB[BTAGDOWN]=1.;
	systWeights1B0sB[MISTAGUP]=1.;
	systWeights1B0sB[MISTAGDOWN]=1.;
	systWeights1B0sB[PUUP]=1.;
	systWeights1B0sB[PUDOWN]=1.;
	systWeights1B0sB[MISTAGHIGGSUP]=1.;
	systWeights1B0sB[MISTAGHIGGSDOWN]=1.;
	
	wcats[0]=1.0;   
	if(addTTSplit){
	  wcats[0]=1.0;
	  wcats[1]=double(NMCLeptons==0);
	  wcats[2]=double(NMCLeptons==1);
	  wcats[3]=double(NMCLeptons==2);
	  systZero.setWCats(wcats);
	}
      }
      
      if(isData=="MC"){
	
	double puUpFact=(LumiWeightsUp_.weight(numTrueInt))/(LumiWeights_.weight(numTrueInt));
	double puDownFact=(LumiWeightsDown_.weight(numTrueInt))/(LumiWeights_.weight(numTrueInt));
	
	if(numTrueInt>75){
	  cout << " --> numTrueInt very high!!" << endl;
	  puUpFact =0;
	  puDownFact=0;
	}
	
	systZero.setWeight(0,1.);
	systZero.setWeight("btagUp",1.);
	systZero.setWeight("btagDown",1.);
	systZero.setWeight("mistagUp",1.);
	systZero.setWeight("mistagDown",1.);
	systZero.setWeight("puUp",1.);
	systZero.setWeight("puDown",1.);
	systZero.setWeight("mistagHiggsDown",1.);
	systZero.setWeight("mistagHiggsUp",1.);
	wcats[0]=1.0;
	if(addTTSplit){
	  wcats[0]=1.0;
	  wcats[1]=double(NMCLeptons==0);
	  wcats[2]=double(NMCLeptons==1);
	  wcats[3]=double(NMCLeptons==2);
	  systZero.setWCats(wcats);
	}
	
	if(addPDF)systZero.setPDFWeights(w_pdfs, PDFsplittedWeight, nPDF,w_zero, true);
	if(addQ2)systZero.setQ2Weights(w_q2up,w_q2down,w_zero,true);
	if(addTopPt)systZero.setTWeight(w_top,topWeight,true);
	if(addVHF)systZero.setVHFWeight(vhf,true,shiftval);
	if(addWZNLO){
	  systZero.setkFact("QCDRen",kfact_qcd,kfact_qcdrenUp,kfact_qcdrenDown);
	  systZero.setkFact("QCDFac",kfact_qcd,kfact_qcdfacUp,kfact_qcdfacDown);
	  systZero.setkFact("EWK",kfact_ewk,kfact_ewkUp,kfact_ewkDown);
	}
	
	syst1B2sB.copySysts(systZero);
	syst1B2sB.setWeight(0,bWeight1 * bWeight2_subj);
	syst1B2sB.setWeight("btagUp",bWeight1BTagUp * bWeight2BTagUp_subj); 
	syst1B2sB.setWeight("btagDown",bWeight1BTagDown * bWeight2BTagDown_subj);
	syst1B2sB.setWeight("mistagUp",bWeight1MisTagUp * bWeight2_subj);
	syst1B2sB.setWeight("mistagDown",bWeight1MisTagDown* bWeight2_subj);
	syst1B2sB.setWeight("puUp",bWeight1 * bWeight2_subj * puUpFact);
	syst1B2sB.setWeight("puDown",bWeight1 * bWeight2_subj * puDownFact);
	syst1B2sB.setWeight("mistagHiggsUp",bWeight1MisTagUp_subj * bWeight1 );
	syst1B2sB.setWeight("mistagHiggsDown",bWeight1MisTagDown_subj * bWeight1 );
	
	if(addTTSplit){
	  syst1B2sB.setWCats(wcats);
	  //	   syst1B2sB.setWeight("0lep",float(NMCLeptons==0),true);	   syst1B2sB.setWeight("1lep",float(NMCLeptons==1),true);	   syst1B2sB.setWeight("2lep",float(NMCLeptons==2),true);
	}
	if(addPDF)syst1B2sB.setPDFWeights(w_pdfs, PDFsplittedWeight, nPDF,w_zero,true);
	if(addQ2)syst1B2sB.setQ2Weights(w_q2up,w_q2down,w_zero,true);
	if(addTopPt)syst1B2sB.setTWeight(w_top,topWeight,true);
	if(addVHF)syst1B2sB.setVHFWeight(vhf,true,shiftval);
	if(addWZNLO){
	  syst1B2sB.setkFact("QCDRen",kfact_qcd,kfact_qcdrenUp,kfact_qcdrenDown);
	  syst1B2sB.setkFact("QCDFac",kfact_qcd,kfact_qcdfacUp,kfact_qcdfacDown);
	  syst1B2sB.setkFact("EWK",kfact_ewk,kfact_ewkUp,kfact_ewkDown);
	}
	
	systWeights1B2sB[PUUP]= puUpFact * bWeight1 * bWeight2_subj;
	systWeights1B2sB[PUDOWN]= puDownFact * bWeight1 * bWeight2_subj;
	systWeights1B2sB[MISTAGHIGGSUP]= bWeight2MisTagUp_subj * bWeight1 ;
	systWeights1B2sB[MISTAGHIGGSDOWN]= bWeight2MisTagDown_subj * bWeight1 ;
	systWeights1B2sB[NOSYST]=bWeight1*bWeight2_subj;
	systWeights1B2sB[BTAGUP]=bWeight1BTagUp*bWeight2BTagUp_subj;
	systWeights1B2sB[BTAGDOWN]=bWeight1BTagDown*bWeight2BTagDown_subj;
	systWeights1B2sB[MISTAGUP]=bWeight1MisTagUp*bWeight2_subj;
	systWeights1B2sB[MISTAGDOWN]=bWeight1MisTagDown*bWeight2_subj;

	syst1B1sB.copySysts(systZero);
	syst1B1sB.setWeight(0,bWeight1 * bWeight1_subj);
	syst1B1sB.setWeight("btagUp",bWeight1BTagUp * bWeight1BTagUp_subj);
	syst1B1sB.setWeight("btagDown",bWeight1BTagDown * bWeight1BTagDown_subj);
	syst1B1sB.setWeight("mistagUp",bWeight1MisTagUp * bWeight1_subj);
	syst1B1sB.setWeight("mistagDown",bWeight1MisTagDown * bWeight1_subj);
	syst1B1sB.setWeight("puUp",bWeight1 * bWeight1_subj * puUpFact);
	syst1B1sB.setWeight("puDown",bWeight1 * bWeight1_subj * puDownFact);
	syst1B1sB.setWeight("mistagHiggsUp",bWeight1MisTagUp_subj * bWeight1);
	syst1B1sB.setWeight("mistagHiggsDown",bWeight1MisTagDown_subj * bWeight1);
	
	if(addTTSplit){
	  syst1B1sB.setWCats(wcats);
	  //	   syst1B1sB.setWeight("0lep",float(NMCLeptons==0),true);	   syst1B1sB.setWeight("1lep",float(NMCLeptons==1),true);	   syst1B1sB.setWeight("2lep",float(NMCLeptons==2),true);
	}
	if(addPDF)syst1B1sB.setPDFWeights(w_pdfs, PDFsplittedWeight, nPDF,w_zero, true);
	if(addQ2)syst1B1sB.setQ2Weights(w_q2up,w_q2down,w_zero,true);
	if(addTopPt)syst1B1sB.setTWeight(w_top,topWeight,true);
	if(addVHF)syst1B1sB.setVHFWeight(vhf,true,shiftval);
	if(addWZNLO){
	  syst1B1sB.setkFact("QCDRen",kfact_qcd,kfact_qcdrenUp,kfact_qcdrenDown);
	  syst1B1sB.setkFact("QCDFac",kfact_qcd,kfact_qcdfacUp,kfact_qcdfacDown);
	  syst1B1sB.setkFact("EWK",kfact_ewk,kfact_ewkUp,kfact_ewkDown);
	}
	
	systWeights1B1sB[PUUP]= puUpFact * bWeight1 * bWeight1_subj;
	systWeights1B1sB[PUDOWN]= puDownFact * bWeight1 * bWeight1_subj;
	systWeights1B1sB[MISTAGHIGGSUP]= bWeight1MisTagUp_subj * bWeight1;
	systWeights1B1sB[MISTAGHIGGSDOWN]= bWeight1MisTagDown_subj * bWeight1;
	systWeights1B1sB[NOSYST]=bWeight1 * bWeight1_subj;
	systWeights1B1sB[BTAGUP]=bWeight1BTagUp * bWeight1BTagUp_subj;
	systWeights1B1sB[BTAGDOWN]=bWeight1BTagDown * bWeight1BTagDown_subj;
	systWeights1B1sB[MISTAGUP]=bWeight1MisTagUp * bWeight1_subj;
	systWeights1B1sB[MISTAGDOWN]=bWeight1MisTagDown * bWeight1_subj;

	syst1B0sB.copySysts(systZero);
	syst1B0sB.setWeight(0,bWeight1 * 1);
	syst1B0sB.setWeight("btagUp",bWeight1BTagUp * 1);
	syst1B0sB.setWeight("btagDown",bWeight1BTagDown * 1);
	syst1B0sB.setWeight("mistagUp",bWeight1MisTagUp * 1);
	syst1B0sB.setWeight("mistagDown",bWeight1MisTagDown * 1);
	syst1B0sB.setWeight("puUp",bWeight1 * 1 * puUpFact);
	syst1B0sB.setWeight("puDown",bWeight1 * 1 * puDownFact);
	syst1B0sB.setWeight("mistagHiggsUp", 1 * bWeight1);
	syst1B0sB.setWeight("mistagHiggsDown", 1 * bWeight1);
	
	if(addTTSplit){
	  syst1B0sB.setWCats(wcats);
	  //	   syst1B0sB.setWeight("0lep",float(NMCLeptons==0),true);	   syst1B0sB.setWeight("1lep",float(NMCLeptons==1),true);	   syst1B0sB.setWeight("2lep",float(NMCLeptons==2),true);
	}
	if(addPDF)syst1B0sB.setPDFWeights(w_pdfs, PDFsplittedWeight, nPDF,w_zero, true);
	if(addQ2)syst1B0sB.setQ2Weights(w_q2up,w_q2down,w_zero,true);
	if(addTopPt)syst1B0sB.setTWeight(w_top,topWeight,true);
	if(addVHF)syst1B0sB.setVHFWeight(vhf,true,shiftval);
	if(addWZNLO){
	  syst1B0sB.setkFact("QCDRen",kfact_qcd,kfact_qcdrenUp,kfact_qcdrenDown);
	  syst1B0sB.setkFact("QCDFac",kfact_qcd,kfact_qcdfacUp,kfact_qcdfacDown);
	  syst1B0sB.setkFact("EWK",kfact_ewk,kfact_ewkUp,kfact_ewkDown);
	}
	
	systWeights1B0sB[PUUP]= puUpFact * bWeight1 * 1;
	systWeights1B0sB[PUDOWN]= puDownFact * bWeight1 * 1;
	systWeights1B0sB[MISTAGHIGGSUP]= 1 * bWeight1;
	systWeights1B0sB[MISTAGHIGGSDOWN]= 1 * bWeight1;
	systWeights1B0sB[NOSYST]=bWeight1 * 1;
	systWeights1B0sB[BTAGUP]=bWeight1BTagUp * 1;
	systWeights1B0sB[BTAGDOWN]=bWeight1BTagDown * 1;
	systWeights1B0sB[MISTAGUP]=bWeight1MisTagUp * 1;
	systWeights1B0sB[MISTAGDOWN]=bWeight1MisTagDown * 1;
	
	/****
	syst2B0sB.copySysts(systZero);
        syst2B0sB.setWeight(0,bWeight2 * 1);
        syst2B0sB.setWeight("btagUp",bWeight2BTagUp * 1);
        syst2B0sB.setWeight("btagDown",bWeight2BTagDown * 1);
        syst2B0sB.setWeight("mistagUp",bWeight2MisTagUp * 1);
        syst2B0sB.setWeight("mistagDown",bWeight2MisTagDown * 1);
        syst2B0sB.setWeight("puUp",bWeight2 * 1 * puUpFact);
        syst2B0sB.setWeight("puDown",bWeight2 * 1 * puDownFact);
	syst2B0sB.setWeight("btagHiggsUp", 1 * bWeight2);
        syst2B0sB.setWeight("btagHiggsDown", 1 * bWeight2);
        syst2B0sB.setWeight("mistagHiggsUp", 1 * bWeight2);
        syst2B0sB.setWeight("mistagHiggsDown", 1 * bWeight2);

        if(addTTSplit){
          syst2B0sB.setWCats(wcats);
          //       syst2B0sB.setWeight("0lep",float(NMCLeptons==0),true);          syst2B0sB.setWeight("1lep",float(NMCLeptons==1),true);          syst2BsetWeight("2lep",float(NMCLeptons==2),true);                                                                                                                  
        }

        if(addPDF)syst2B0sB.setPDFWeights(w_pdfs,nPDF,w_zero,true);
        if(addQ2)syst2B0sB.setQ2Weights(w_q2up,w_q2down,w_zero,true);
        if(addTopPt)syst2B0sB.setTWeight(w_top,topWeight,true);
        if(addVHF)syst2B0sB.setVHFWeight(vhf,true,shiftval);
        if(addWZNLO){
          syst2B0sB.setkFact("QCDRen",kfact_qcd,kfact_qcdrenUp,kfact_qcdrenDown);
          syst2B0sB.setkFact("QCDFac",kfact_qcd,kfact_qcdfacUp,kfact_qcdfacDown);
          syst2B0sB.setkFact("EWK",kfact_ewk,kfact_ewkUp,kfact_ewkDown);
        }

        systWeights2B0sB[PUUP]= puUpFact * bWeight2 * 1;
        systWeights2B0sB[PUDOWN]= puDownFact * bWeight2 * 1;
        systWeights2B0sB[BTAGHIGGSUP]= 1 * bWeight2;
        systWeights2B0sB[BTAGHIGGSDOWN]= 1 * bWeight2;
        systWeights2B0sB[MISTAGHIGGSUP]= 1 * bWeight2;
        systWeights2B0sB[MISTAGHIGGSDOWN]= 1 * bWeight2;
        systWeights2B0sB[NOSYST]=bWeight2 * 1;
        systWeights2B0sB[BTAGUP]=bWeight2BTagUp * 1;
        systWeights2B0sB[BTAGDOWN]=bWeight2BTagDown * 1;
        systWeights2B0sB[MISTAGUP]=bWeight2MisTagUp * 1;
        systWeights2B0sB[MISTAGDOWN]=bWeight2MisTagDown * 1;
	*/
	
	syst0B0sB.copySysts(systZero);
	syst0B0sB.setWeight(0, 1 * 1);
	syst0B0sB.setWeight("btagUp", 1 * 1);
	syst0B0sB.setWeight("btagDown",  1 * 1);
	syst0B0sB.setWeight("mistagUp",  1 * 1);
	syst0B0sB.setWeight("mistagDown",  1 * 1);
	syst0B0sB.setWeight("puUp",puUpFact *  1 * 1 );
	syst0B0sB.setWeight("puDown",puDownFact  * 1 * 1);
	syst0B0sB.setWeight("mistagHiggsUp",  1 * 1);
	syst0B0sB.setWeight("mistagHiggsDown",  1 * 1);
	
	if(addTTSplit){
	  syst0B0sB.setWCats(wcats);
	  //      syst0B0sB.setWeight("0lep",float(NMCLeptons==0),true);     syst0B0sB.setWeight("1lep",float(NMCLeptons==1),true);     syst0B0sB.setWeight("2lep",float(NMCLeptons==2),true);                                                                                                                              
	}
	if(addPDF)syst0B0sB.setPDFWeights(w_pdfs, PDFsplittedWeight, nPDF,w_zero, true);
	if(addQ2)syst0B0sB.setQ2Weights(w_q2up,w_q2down,w_zero,true);
	if(addTopPt)syst0B0sB.setTWeight(w_top,topWeight,true);
	if(addVHF)syst0B0sB.setVHFWeight(vhf,true,shiftval);
	if(addWZNLO){
	  syst0B0sB.setkFact("QCDRen",kfact_qcd,kfact_qcdrenUp,kfact_qcdrenDown);
	  syst0B0sB.setkFact("QCDFac",kfact_qcd,kfact_qcdfacUp,kfact_qcdfacDown);
	  syst0B0sB.setkFact("EWK",kfact_ewk,kfact_ewkUp,kfact_ewkDown);
	}
	
	systWeights0B0sB[PUUP]= puUpFact * 1 * 1;
	systWeights0B0sB[PUDOWN]=puDownFact * 1 * 1;
	systWeights0B0sB[MISTAGHIGGSUP]=  1 * 1;
	systWeights0B0sB[MISTAGHIGGSDOWN]=  1 * 1;
	systWeights0B0sB[NOSYST]=  1 * 1;
	systWeights0B0sB[BTAGUP]=  1 * 1;
	systWeights0B0sB[BTAGDOWN]=  1 * 1;
	systWeights0B0sB[MISTAGUP]=  1 * 1;
	systWeights0B0sB[MISTAGDOWN]=  1 * 1;
      }
     
      std::vector<TLorentzVector> jets, bjets, fwjets, fatjets;
      struct btag{
	TLorentzVector vect;
	float csv;
	float deltar;
      }; 
      
      std::vector<btag> b_selvects, fwvects;
      
      struct Bosontag{
	TLorentzVector vect;
	float tau2;
	float tau1;
	float prunedmass;
	int nsubjets;
      };
      
      int maxJetLoop = min(15, jetSize);
      int maxFatJetLoop = min(10, fatjetSize);
       
      syst0B0sB.fillHistogramsSysts(h_weight10, w_pdfs[23]/w_zero, 1, systWeights0B0sB);
      syst0B0sB.fillHistogramsSysts(h_weight50, w_pdfs[45]/w_zero, 1, systWeights0B0sB);

      if( (isData=="DATA" && ((samplestr).find("JetHT_runH") != std::string::npos) && (passTrigHT900 >0. || passTrigPFJet450>0.)) || (isData=="DATA" && !((samplestr).find("JetHT_runH") != std::string::npos) && (passTrigHT900>0.)) || (isData=="MC" && passTrigHT900>0.)){ //trigger requirement
	//if(passTrigSingleMu>0.){
	syst0B0sB.fillHistogramsSysts(h_Ht_bef,Ht,w,systWeights0B0sB);
	n_trig += w;
	
	if(Ht>1250){ // HT requirement
	//if(1>0){
	n_ht+=w;
	
	  //forward jet category
	  int countfwjets=0, countcjets=0, countbjets=0;
	  for (int j = 0; j <maxJetLoop;++j){
	    if(fabs(jeteta[j])<4) {
	      
	      if(/*jetptcorr[j]>20 &&*/ fabs(jeteta[j])>2.4 ){
		countfwjets++;
		TLorentzVector fwjet;
		fwjet.SetPtEtaPhiE(jetptcorr[j], jeteta[j], jetphi[j], jete[j]);
		btag fw;
		fw.vect = fwjet;
		fwvects.push_back(fw);
		syst0B0sB.fillHistogramsSysts(h_AK4fwjetpt,jetptcorr[j],w,systWeights0B0sB);
		syst0B0sB.fillHistogramsSysts(h_AK4fwjeteta,jeteta[j],w,systWeights0B0sB);
	      }
	      if(jetptcorr[j]>30 && fabs(jeteta[j])<2.4){
		syst0B0sB.fillHistogramsSysts(h_AK4cjetpt,(jetptcorr[j]),w,systWeights0B0sB);
		syst0B0sB.fillHistogramsSysts(h_AK4cjeteta,(jeteta[j]),w,systWeights0B0sB);
		syst0B0sB.fillHistogramsSysts(h_AK4cjetcsv, jetcsv[j], w, systWeights0B0sB);
		countcjets++;
	      }
	      if(jetcsv[j]>0.8484 && jetptcorr[j]>30){
		syst1B0sB.fillHistogramsSysts(h_AK4bjetpt,(jetptcorr[j]),w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_AK4bjeteta,(jeteta[j]),w,systWeights1B0sB);
		countbjets++;
	      }
	    }                                                                                                                         
	  }
	 
	  syst0B0sB.fillHistogramsSysts(h_AK4fwjets,countfwjets,w,systWeights0B0sB);
	  syst0B0sB.fillHistogramsSysts(h_AK4cjets,countcjets,w,systWeights0B0sB);
	  syst0B0sB.fillHistogramsSysts(h_AK4bjets,countbjets,w,systWeights0B0sB);

	  //preselection on jet multiplicity
	  int countjets=0, countfatjets=0, countb=0, nAK4bjets=0;
	  for (int j = 0; j <maxJetLoop;++j){
	    if(jetptcorr[j]>30. &&  fabs(jeteta[j])<4) {
	      countjets++;
	      if(jetcsv[j]>0.8484 && fabs(jeteta[j])<2.4) countb++;
	    }
	  }
	  
	  for(int j=0; j<maxFatJetLoop; ++j){
	    if(fatjetptcorr[j]>300 && fabs(fatjeteta[j])<2.4){
	      countfatjets++;
	    }
	  }
	  
	  syst0B0sB.fillHistogramsSysts(h_AK8jetmult,countfatjets,w,systWeights0B0sB);
	  syst0B0sB.fillHistogramsSysts(h_AK4jetmult,countjets,w,systWeights0B0sB);
	  syst0B0sB.fillHistogramsSysts(h_AK4bjetmult,countb,w,systWeights0B0sB);

	  syst0B0sB.fillHistogramsSysts(h_Ht,Ht,w,systWeights0B0sB);
	  //if( (isData=="DATA" && ((samplestr).find("JetHTh") != std::string::npos) && (passTrigHT900 >0. || passTrigPFJet450>0.)) || (isData=="DATA" && !((samplestr).find("JetHTh") != std::string::npos) && (passTrigHT900>0.)) || (isData=="MC" && passTrigHT900>0.)){syst0B0sB.fillHistogramsSysts(h_Ht_trigaft,Ht,1.,systWeights0B0sB);}
	  
	  syst0B0sB.fillHistogramsSysts(h_nPV,nGoodPV,1.,systWeights0B0sB);

	  syst0B0sB.fillHistogramsSysts(h_nPV_w,nGoodPV,w,systWeights0B0sB);
	  
	  if(countfatjets>0){
	    n_fatjet+=w;

	    if(countjets>2){
	      n_jet+=w;
	      
	      //syst0B0sB.fillHistogramsSysts(h_Ht_bef,Ht,w,systWeights0B0sB);
	      
	      if(countb>0){
		n_bjet+=w;
		TLorentzVector AK4bjet;
	      
	      if((cat=="cat_inclusive" && countfwjets>-1) || (cat=="cat0" && countfwjets==0) || (cat=="cat1" && countfwjets>0)){ //forward jet based categories
		n_cat += w;

		//if( (isData=="DATA" && ((samplestr).find("JetHT_runH") != std::string::npos) && (passTrigHT900 >0. || passTrigPFJet450>0.)) || (isData=="DATA" && !((samplestr).find("JetHT_runH") != std::string::npos) && (passTrigHT900>0.)) || (isData=="MC" && passTrigHT900>0.)){syst0B0sB.fillHistogramsSysts(h_Ht_trigaft,Ht,w,systWeights0B0sB);}     
		
		//syst1B0sB.fillHistogramsSysts(h_Ht,Ht,w.,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_Ht_trigaft,Ht,1.,systWeights1B0sB);
		
		syst1B0sB.fillHistogramsSysts(h_AK4jetptlead,jetptcorr[0],w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_AK4jetetalead,jeteta[0],w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_AK4jetphilead,jetphi[0],w,systWeights1B0sB);

		syst1B0sB.fillHistogramsSysts(h_AK4jetptsublead,jetptcorr[1],w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_AK4jetetasublead,jeteta[1],w,systWeights1B0sB);
                syst1B0sB.fillHistogramsSysts(h_AK4jetphisublead,jetphi[1],w,systWeights1B0sB);
		
		TLorentzVector fwjet, fwjet_2p43, fwjet_34p7, bjet;
		std::vector<TLorentzVector> bjets, fwjets, fwjets_2p43, fwjets_34p7;
		int b=0, f=0, f_34p7=0, f_2p43=0;
		for(int i=0; i<maxJetLoop; i++){
		  if(jetptcorr[i]>30 && fabs(jeteta[i])<2.4 && jetcsv[i]>0.8484){
		    bjet.SetPtEtaPhiE(jetptcorr[i], jeteta[i], jetphi[i], jete[i]);
		    b++;
		    bjets.push_back(bjet);
		  }
		  if(fabs(jeteta[i])>2.4 /*&& jetptcorr[i]>20*/){
                    fwjet.SetPtEtaPhiE(jetptcorr[i], jeteta[i], jetphi[i], jete[i]);
                    f++;
                    fwjets.push_back(fwjet);
		    if(fabs(jeteta[i])>2.4 && fabs(jeteta[i])<3.){
		      fwjet_2p43.SetPtEtaPhiE(jetptcorr[i], jeteta[i], jetphi[i], jete[i]);
		      f_2p43++;
		      fwjets_2p43.push_back(fwjet);
		    }
		    else if (fabs(jeteta[i])>3.){
                      fwjet_34p7.SetPtEtaPhiE(jetptcorr[i], jeteta[i], jetphi[i], jete[i]);
                      f_34p7++;
                      fwjets_34p7.push_back(fwjet);
                    }
                  }
		}
		if(b>0){
		  syst1B0sB.fillHistogramsSysts(h_AK4bptlead,bjets[0].Pt(),w,systWeights1B0sB);
		  syst1B0sB.fillHistogramsSysts(h_AK4betalead,bjets[0].Eta(),w,systWeights1B0sB);
		  syst1B0sB.fillHistogramsSysts(h_AK4bphilead,bjets[0].Phi(),w,systWeights1B0sB);
		}
		if(b>1){
		  syst1B0sB.fillHistogramsSysts(h_AK4bptsublead,bjets[1].Pt(),w,systWeights1B0sB);
		  syst1B0sB.fillHistogramsSysts(h_AK4betasublead,bjets[1].Eta(),w,systWeights1B0sB);
		  syst1B0sB.fillHistogramsSysts(h_AK4bphisublead,bjets[1].Phi(),w,systWeights1B0sB);
		  }
		if(f_2p43>0){
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetptlead_2p43,fwjets_2p43[0].Pt(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetetalead_2p43,fwjets_2p43[0].Eta(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetphilead_2p43,fwjets_2p43[0].Phi(),w,systWeights1B0sB);
                }
		if(f_34p7>0){
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetptlead_34p7,fwjets_34p7[0].Pt(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetetalead_34p7,fwjets_34p7[0].Eta(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetphilead_34p7,fwjets_34p7[0].Phi(),w,systWeights1B0sB);
                }
		if(f>0){
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetptlead,fwjets[0].Pt(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetetalead,fwjets[0].Eta(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetphilead,fwjets[0].Phi(),w,systWeights1B0sB);
                }
                if(f>1){
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetptsublead,fwjets[1].Pt(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetetasublead,fwjets[1].Eta(),w,systWeights1B0sB);
                  syst1B0sB.fillHistogramsSysts(h_AK4fwjetphisublead,fwjets[1].Phi(),w,systWeights1B0sB);
		}

		syst1B0sB.fillHistogramsSysts(h_fwjetmult_34p7,f_34p7,w,systWeights1B0sB);     
		syst1B0sB.fillHistogramsSysts(h_fwjetmult_2p43,f_2p43,w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_fwjetmult,f,w,systWeights1B0sB);

		for(int i=0; i<maxJetLoop;++i){
		  if(jetptcorr[i]>30.){
		    syst1B0sB.fillHistogramsSysts(h_AK4jetpt,jetptcorr[i],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_AK4jeteta,jeteta[i],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_AK4jetphi,jetphi[i],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_AK4jetcsv,jetcsv[i],w,systWeights1B0sB);
		    if(jetcsv[i]>0.8484 && fabs(jeteta[i])<2.4){
		      AK4bjet.SetPtEtaPhiE(jetptcorr[i], jeteta[i], jetphi[i], jete[i]);
		      nAK4bjets++;
		      bjets.push_back(AK4bjet);
		    }
		  }
		}
		
		//syst1B0sB.fillHistogramsSysts(h_bjetmult,nb,w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_AK4bjetmultaft,countb,w,systWeights1B0sB);  
		syst1B0sB.fillHistogramsSysts(h_AK4jetmultaft, countjets,w,systWeights1B0sB);  

		std::vector<Bosontag> HiggsCand_A, antiHiggsCand_C, antiHiggsCand_B, antiHiggsCand_D;

		int nHiggsCand_A=0, nantiHiggsCand_C=0, nantiHiggsCand_B=0, nantiHiggsCand_D=0, nAK8jets=0;
		
		for(int j=0; j<maxFatJetLoop; ++j){
		  if(fatjetptcorr[j]>300 && fabs(fatjeteta[j])<2.4){
		    nAK8jets+=1;
		    
		    syst1B0sB.fillHistogramsSysts(h_AK8jetpt,fatjetptcorr[j],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_AK8jeteta,fatjeteta[j],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_AK8jetphi,fatjetphi[j],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_nsubj,fatjetnCSVsubj[j],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_tau2tau1,fatjettau2[j]/fatjettau1[j],w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_prunedmass,fatjetprunedmasscorr[j],w,systWeights1B0sB);
		    
		    TLorentzVector AK8jet;      
		    AK8jet.SetPtEtaPhiE(fatjetptcorr[j], fatjeteta[j], fatjetphi[j], fatjete[j]);
		    
		    Bosontag Boson;
		    Boson.vect = AK8jet;
		    Boson.prunedmass = fatjetprunedmasscorr[j];
		    Boson.tau2 = fatjettau2[j];
		    Boson.tau1 = fatjettau1[j];
		    Boson.nsubjets = fatjetnCSVsubj[j];

		    if(/*Boson.tau2/Boson.tau1<1.0 &&*/ (Boson.prunedmass>105 && Boson.prunedmass<135) && Boson.nsubjets==2){
		      HiggsCand_A.push_back(Boson);
		      nHiggsCand_A+=1;
		    }
		    if(/*Boson.tau2/Boson.tau1<1.0 &&*/ (Boson.prunedmass>105 && Boson.prunedmass<135) && Boson.nsubjets==1){
		      antiHiggsCand_C.push_back(Boson);
		      nantiHiggsCand_C+=1;
		    }
		    if(/*Boson.tau2/Boson.tau1<1.0 &&*/ (Boson.prunedmass>135 || Boson.prunedmass<105) && Boson.nsubjets==2){
		      antiHiggsCand_B.push_back(Boson);
		      nantiHiggsCand_B+=1;
		    }
		    if(/*Boson.tau2/Boson.tau1<1.0 &&*/ (Boson.prunedmass>135 || Boson.prunedmass<105) && Boson.nsubjets==1){
		      antiHiggsCand_D.push_back(Boson);
		      nantiHiggsCand_D+=1;
		    }
		  }
		}
		syst1B0sB.fillHistogramsSysts(h_nHiggsCand_A,nHiggsCand_A,w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_nHiggsCand_B,nantiHiggsCand_B,w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_nHiggsCand_C,nantiHiggsCand_C,w,systWeights1B0sB);
		syst1B0sB.fillHistogramsSysts(h_nHiggsCand_D,nantiHiggsCand_D,w,systWeights1B0sB);

		std::vector<btag> bCand;
		Bosontag  Higgs_A,  antiHiggs_C, antiHiggs_B, antiHiggs_D;
			
		btag bSel;
		bool isRegionA=0, isRegionB=0, isRegionC=0, isRegionD=0;
		int nb=0;

		if(nAK8jets>0){
		  for(int i=0; i<maxJetLoop;++i){
		    if(jetptcorr[i]>30. && jetcsv[i]>0.8484 && fabs(jeteta[i])<2.4){
		      syst1B0sB.fillHistogramsSysts(h_bjetpt,jetptcorr[i],w,systWeights1B0sB);
		      syst1B0sB.fillHistogramsSysts(h_bjeteta,jeteta[i],w,systWeights1B0sB);
		      syst1B0sB.fillHistogramsSysts(h_bjetphi,jetphi[i],w,systWeights1B0sB);
		      nb++;
		    }
		  }
		 
		  //syst1B0sB.fillHistogramsSysts(h_bjetmult,nb,w,systWeights1B0sB);

		  //SIGNAL REGION
		  if(nHiggsCand_A>0){
		    int nH_A=0;
		    for(size_t j=0; j<HiggsCand_A.size(); j++){
		      if(nH_A>0) break;
		      Higgs_A.vect = HiggsCand_A[j].vect;
		      Higgs_A.prunedmass = HiggsCand_A[j].prunedmass;
		      Higgs_A.tau2 = HiggsCand_A[j].tau2;
		      Higgs_A.tau1 = HiggsCand_A[j].tau1;
		      Higgs_A.nsubjets = HiggsCand_A[j].nsubjets;
		
		      syst1B2sB.fillHistogramsSysts(h_hCandpt_A, (HiggsCand_A[j].vect).Pt(), w, systWeights1B2sB);
		      syst1B2sB.fillHistogramsSysts(h_hCandeta_A, (HiggsCand_A[j].vect).Eta(), w, systWeights1B2sB);
		      syst1B2sB.fillHistogramsSysts(h_hCandphi_A, (HiggsCand_A[j].vect).Phi(), w, systWeights1B2sB);

		      bCand.clear();
		      for(size_t b=0; b<bjets.size(); b++){ 
			if((Higgs_A.vect).DeltaR(bjets[b])>1.2){ 
			  bSel.vect = bjets[b]; 
			  bSel.deltar = (Higgs_A.vect).DeltaR(bjets[b]);
			  bCand.push_back(bSel);
			  nH_A++;
			  isRegionA=1;
			  syst1B2sB.fillHistogramsSysts(h_bCandpt_A,(bjets[b]).Pt(),w,systWeights1B2sB);
			  syst1B2sB.fillHistogramsSysts(h_bCandeta_A,(bjets[b]).Eta(),w,systWeights1B2sB);
			  syst1B2sB.fillHistogramsSysts(h_bCandphi_A,(bjets[b]).Phi(),w,systWeights1B2sB);
			}
		      }
		      syst1B2sB.fillHistogramsSysts(h_bCandmult_A,bCand.size(),w,systWeights1B2sB);
		    }
		    syst1B2sB.fillHistogramsSysts(h_hCandmult_A,HiggsCand_A.size(),w,systWeights1B2sB);
		    n_Bosonjets+=w;
		    //syst1B0sB.fillHistogramsSysts(h_AK4bjetmultaft,bjets.size(),w,systWeights1B0sB);
		    syst1B0sB.fillHistogramsSysts(h_AK4bjetmultaft_nH,bCand.size(),w,systWeights1B0sB);
		  }//CONTROL REGION C
		  else if(nHiggsCand_A==0 && nantiHiggsCand_C>0){
		    int nH_C=0;
		    for(size_t j=0; j<antiHiggsCand_C.size(); j++){
		      if(nH_C>0) break;
		      antiHiggs_C.vect = antiHiggsCand_C[j].vect;
		      antiHiggs_C.prunedmass = antiHiggsCand_C[j].prunedmass;
		      antiHiggs_C.tau2 = antiHiggsCand_C[j].tau2;
		      antiHiggs_C.tau1 = antiHiggsCand_C[j].tau1;
		      antiHiggs_C.nsubjets = antiHiggsCand_C[j].nsubjets;
		      bCand.clear();
		      for(size_t b=0; b<bjets.size(); b++){
			if((antiHiggs_C.vect).DeltaR(bjets[b])>1.2){
			  bSel.vect = bjets[b];
			  bSel.deltar = (antiHiggs_C.vect).DeltaR(bjets[b]);
			  bCand.push_back(bSel);
			  nH_C++;
			  isRegionC=1;
			}
		      }
		    }
		    
		  }//CONTRO REGION B
		  else if(nHiggsCand_A==0 && nantiHiggsCand_C==0 && nantiHiggsCand_B>0){
		    int nH_B=0;
		    for(size_t j=0; j<antiHiggsCand_B.size(); j++){
		      if(nH_B>0) break;
		      antiHiggs_B.vect = antiHiggsCand_B[j].vect;
		      antiHiggs_B.prunedmass = antiHiggsCand_B[j].prunedmass;
		      antiHiggs_B.tau2 = antiHiggsCand_B[j].tau2;
		      antiHiggs_B.tau1 = antiHiggsCand_B[j].tau1;
		      antiHiggs_B.nsubjets = antiHiggsCand_B[j].nsubjets;
		      bCand.clear();
		      for(size_t b=0; b<bjets.size(); b++){
			if((antiHiggs_B.vect).DeltaR(bjets[b])>1.2){
			  bSel.vect = bjets[b];
			  bSel.deltar = (antiHiggs_B.vect).DeltaR(bjets[b]);
			  bCand.push_back(bSel);
			  nH_B++;
			  isRegionB=1;
			}
		      }
		    }
		  }//CONTROL REGION D
		  else if(nHiggsCand_A==0 && nantiHiggsCand_C==0 && nantiHiggsCand_B==0 && nantiHiggsCand_D>0){
		    int nH_D=0;
		    for(size_t j=0; j<antiHiggsCand_D.size(); j++){
		      if(nH_D>0) break;
		      antiHiggs_D.vect = antiHiggsCand_D[j].vect;
		      antiHiggs_D.prunedmass = antiHiggsCand_D[j].prunedmass;
		      antiHiggs_D.tau2 = antiHiggsCand_D[j].tau2;
		      antiHiggs_D.tau1 = antiHiggsCand_D[j].tau1;
		      antiHiggs_D.nsubjets = antiHiggsCand_D[j].nsubjets;
		      bCand.clear();
		      for(size_t b=0; b<bjets.size(); b++){
			if((antiHiggs_D.vect).DeltaR(bjets[b])>1.2){
			  bSel.vect = bjets[b];
			  bSel.deltar = (antiHiggs_D.vect).DeltaR(bjets[b]);
			  bCand.push_back(bSel);
			  nH_D++;
			  isRegionD=1;
			}
		      }
		    }
		  }
		  
		}
		
		TLorentzVector Bprime;
		if(isRegionA==1){
		  n_bjets+=w;
		  nA+=w;
		  syst0B0sB.fillHistogramsSysts(h_weight10_aft, w_pdfs[10]/w_zero, 1, systWeights0B0sB);
		  syst0B0sB.fillHistogramsSysts(h_weight50_aft, w_pdfs[50]/w_zero, 1, systWeights0B0sB);
		  Bprime = bCand[0].vect + Higgs_A.vect;
		  //cout << Bprime.M()<< endl;
		  syst1B2sB.fillHistogramsSysts(h_Ht_SR,Ht,w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4fwjets_SR,countfwjets,w,systWeights1B2sB);		  
		  syst1B2sB.fillHistogramsSysts(h_bprimemass_SR,Bprime.M(),w,systWeights1B2sB);
		  if(countjets>1) syst1B2sB.fillHistogramsSysts(h_bprimemass_SR_1,Bprime.M(),w,systWeights1B2sB);
		  if(countjets>2) syst1B2sB.fillHistogramsSysts(h_bprimemass_SR_2,Bprime.M(),w,systWeights1B2sB);
		  if(countjets>3) syst1B2sB.fillHistogramsSysts(h_bprimemass_SR_3,Bprime.M(),w,systWeights1B2sB);
		  if(countjets>4) syst1B2sB.fillHistogramsSysts(h_bprimemass_SR_4,Bprime.M(),w,systWeights1B2sB);
		  if(countjets>5) syst1B2sB.fillHistogramsSysts(h_bprimemass_SR_5,Bprime.M(),w,systWeights1B2sB);

		  syst1B2sB.fillHistogramsSysts(h_bprimept_SR,Bprime.Pt(),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_bprimeeta_SR,Bprime.Eta(),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_bprimephi_SR,Bprime.Phi(),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4jet_selb_pt_SR,((bCand[0].vect).Pt()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4jet_selb_eta_SR,((bCand[0].vect).Eta()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4jet_selb_phi_SR,((bCand[0].vect).Phi()),w,systWeights1B2sB);		  
		  syst1B2sB.fillHistogramsSysts(h_AK8jet_selh_pt_SR,((Higgs_A.vect).Pt()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK8jet_selh_eta_SR,((Higgs_A.vect).Eta()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK8jet_selh_phi_SR,((Higgs_A.vect).Phi()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_nsubj_SR,Higgs_A.nsubjets,w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_tau2tau1_SR,Higgs_A.tau2/Higgs_A.tau1,w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_prunedmass_SR,Higgs_A.prunedmass,w,systWeights1B2sB);
		}else if(isRegionC==1){
		  Bprime = bCand[0].vect + antiHiggs_C.vect;
		  nC+=w;
		  syst1B1sB.fillHistogramsSysts(h_Ht_CRC,Ht,w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4fwjets_CRC,countfwjets,w,systWeights1B1sB);	  
		  syst1B1sB.fillHistogramsSysts(h_bprimemass_CRC,Bprime.M(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_bprimept_CRC,Bprime.Pt(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_bprimeeta_CRC,Bprime.Eta(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_bprimephi_CRC,Bprime.Phi(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4jet_selb_pt_CRC,((bCand[0].vect).Pt()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4jet_selb_eta_CRC,((bCand[0].vect).Eta()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4jet_selb_phi_CRC,((bCand[0].vect).Phi()),w,systWeights1B1sB);		  
		  syst1B1sB.fillHistogramsSysts(h_AK8jet_selh_pt_CRC,((antiHiggs_C.vect).Pt()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK8jet_selh_eta_CRC,((antiHiggs_C.vect).Eta()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK8jet_selh_phi_CRC,((antiHiggs_C.vect).Phi()),w,systWeights1B1sB);	  
		  syst1B1sB.fillHistogramsSysts(h_nsubj_CRC,antiHiggs_C.nsubjets,w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_tau2tau1_CRC,antiHiggs_C.tau2/antiHiggs_C.tau1,w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_prunedmass_CRC,antiHiggs_C.prunedmass,w,systWeights1B1sB);

		}else if(isRegionB==1){
		  Bprime = bCand[0].vect + antiHiggs_B.vect;
		  nB+=w;
		  syst1B2sB.fillHistogramsSysts(h_Ht_CRB,Ht,w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4fwjets_CRB,countfwjets,w,systWeights1B2sB);	  
		  syst1B2sB.fillHistogramsSysts(h_bprimemass_CRB,Bprime.M(),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_bprimept_CRB,Bprime.Pt(),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_bprimeeta_CRB,Bprime.Eta(),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_bprimephi_CRB,Bprime.Phi(),w,systWeights1B2sB);	  
		  syst1B2sB.fillHistogramsSysts(h_AK4jet_selb_pt_CRB,((bCand[0].vect).Pt()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4jet_selb_eta_CRB,((bCand[0].vect).Eta()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK4jet_selb_phi_CRB,((bCand[0].vect).Phi()),w,systWeights1B2sB);	  
		  syst1B2sB.fillHistogramsSysts(h_AK8jet_selh_pt_CRB,((antiHiggs_B.vect).Pt()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK8jet_selh_eta_CRB,((antiHiggs_B.vect).Eta()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_AK8jet_selh_phi_CRB,((antiHiggs_B.vect).Phi()),w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_nsubj_CRB,antiHiggs_B.nsubjets,w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_tau2tau1_CRB,antiHiggs_B.tau2/antiHiggs_B.tau1,w,systWeights1B2sB);
		  syst1B2sB.fillHistogramsSysts(h_prunedmass_CRB,antiHiggs_B.prunedmass,w,systWeights1B2sB);
		}else if(isRegionD==1){
		  Bprime = bCand[0].vect + antiHiggs_D.vect;
		  nD+=w;
		  syst1B1sB.fillHistogramsSysts(h_Ht_CRD,Ht,w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4fwjets_CRD,countfwjets,w,systWeights1B1sB);	  
		  syst1B1sB.fillHistogramsSysts(h_bprimemass_CRD,Bprime.M(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_bprimept_CRD,Bprime.Pt(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_bprimeeta_CRD,Bprime.Eta(),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_bprimephi_CRD,Bprime.Phi(),w,systWeights1B1sB);		  
		  syst1B1sB.fillHistogramsSysts(h_AK4jet_selb_pt_CRD,((bCand[0].vect).Pt()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4jet_selb_eta_CRD,((bCand[0].vect).Eta()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK4jet_selb_phi_CRD,((bCand[0].vect).Phi()),w,systWeights1B1sB);		  
		  syst1B1sB.fillHistogramsSysts(h_AK8jet_selh_pt_CRD,((antiHiggs_D.vect).Pt()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_AK8jet_selh_eta_CRD,((antiHiggs_D.vect).Eta()),w,systWeights1B1sB);	  
		  syst1B1sB.fillHistogramsSysts(h_AK8jet_selh_phi_CRD,((antiHiggs_D.vect).Phi()),w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_nsubj_CRD,antiHiggs_D.nsubjets,w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_tau2tau1_CRD,antiHiggs_D.tau2/antiHiggs_D.tau1,w,systWeights1B1sB);
		  syst1B1sB.fillHistogramsSysts(h_prunedmass_CRD,antiHiggs_D.prunedmass,w,systWeights1B1sB);
		}
	      }
	      }//end of categories
	    }//end of AK4 jet
	  }//end of AK8 jets
	}//end of ht
	
      }//end of trigger
    
       fileout
	<<std::fixed<<std::setprecision(0)
	<<runNumber<<"   "
	<<evtNumber<<"   "
	<<lumiSec<<"   "
	<<(double) n_closure/nEventsPrePres<< "   "
       	<<std::endl;
      }
    }//end of loop over events
  
  h_cutFlow->SetBinContent(1,nEvents);
  h_cutFlow->GetXaxis()->SetBinLabel(1,"no selection");
  h_cutFlow->SetBinContent(2, n_trig);
  h_cutFlow->GetXaxis()->SetBinLabel(2, "trigger");
  h_cutFlow->SetBinContent(4, n_fatjet);
  h_cutFlow->GetXaxis()->SetBinLabel(4, "#AK8 jet>0");
  h_cutFlow->SetBinContent(5, n_jet);
  h_cutFlow->GetXaxis()->SetBinLabel(5, "#AK4 jet>3");
  h_cutFlow->SetBinContent(6, n_bjet);
  h_cutFlow->GetXaxis()->SetBinLabel(6, "#AK4 CSVMv2 jet>0");
  h_cutFlow->SetBinContent(7, n_Bosonjets);
  h_cutFlow->GetXaxis()->SetBinLabel(7, "#Higgs jet>1");
  h_cutFlow->SetBinContent(8, n_bjets);
  h_cutFlow->GetXaxis()->SetBinLabel(8, "#Delta R(bjet,H)>1.2");
  h_cutFlow->SetBinContent(3, n_ht);
  h_cutFlow->GetXaxis()->SetBinLabel(3, "Ht>1250 GeV");
  
  systZero.writeSingleHistogramSysts(h_cutFlow, allMyFiles);
  
  syst0B0sB.writeHistogramsSysts(h_weight10,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_weight50,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_weight10_aft,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_weight50_aft,allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_AK4cjetcsv, allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_AK4bptsublead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4betasublead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bphisublead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bptlead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4betalead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bphilead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetptsublead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetetasublead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetphisublead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetptlead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetetalead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetphilead, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetptlead_2p43, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetetalead_2p43, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetphilead_2p43, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetptlead_34p7, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetetalead_34p7, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4fwjetphilead_34p7, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_bCandpt_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bCandeta_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bCandphi_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bCandmult_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_hCandpt_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_hCandeta_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_hCandphi_A,allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_hCandmult_A,allMyFiles);
  
  syst1B0sB.writeHistogramsSysts(h_bjetpt,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_bjeteta,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_bjetphi,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_bjetmult,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_fwjetmult,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_fwjetmult_2p43,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_fwjetmult_34p7,allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_nHiggsCand_A,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_nHiggsCand_B,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_nHiggsCand_C,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_nHiggsCand_D,allMyFiles);
  
  syst1B0sB.writeHistogramsSysts(h_AK4jetptsublead,allMyFiles);  
  syst1B0sB.writeHistogramsSysts(h_AK4jetetasublead,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetphisublead,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetptlead,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetetalead,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetphilead,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4fwjetpt,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4fwjeteta,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4cjetpt,allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4cjeteta,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bjetpt,allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bjeteta,allMyFiles);

  syst0B0sB.writeHistogramsSysts(h_nPV_w, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_nPV, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4fwjets, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4cjets, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4bjets, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_AK4jetmult, allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_AK8jetmult, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bjetmult, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bjetmultaft, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4bjetmultaft_nH, allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_AK4jetmultaft, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4bjetmultaft_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4jetmultaft_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK8jetmultaft_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4fwjets_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4fwjets_CRB, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4fwjets_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4fwjets_CRD, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_AK4bjetmultaft_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4jetmultaft_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK8jetmultaft_CRB, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_AK4bjetmultaft_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4jetmultaft_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK8jetmultaft_CRC, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_AK4bjetmultaft_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4jetmultaft_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK8jetmultaft_CRD, allMyFiles);

  syst0B0sB.writeHistogramsSysts(h_Ht, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_Ht_bef, allMyFiles);
  syst0B0sB.writeHistogramsSysts(h_Ht_trigaft, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_Ht_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_Ht_CRB, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_Ht_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_Ht_CRD, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_SR_1, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_SR_2, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_SR_3, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_SR_4, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_SR_5, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimemass_CRB, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimemass_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimemass_CRD, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_bprimept_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimept_CRB, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimept_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimept_CRD, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_bprimeeta_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimeeta_CRB, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimeeta_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimeeta_CRD, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_bprimephi_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimephi_CRB, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimephi_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimephi_CRD, allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_nsubj, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_tau2tau1, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_prunedmass, allMyFiles);

  syst1B0sB.writeHistogramsSysts(h_AK8jetpt, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK8jeteta, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK8jetphi, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetpt, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetphi, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jeteta, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_AK4jetcsv, allMyFiles);
  syst1B0sB.writeHistogramsSysts(h_deltaRbH, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_AK4jet_selb_pt_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4jet_selb_eta_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4jet_selb_phi_SR, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_AK8jet_selh_pt_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK8jet_selh_eta_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK8jet_selh_phi_SR, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_nsubj_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_tau2tau1_SR, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_prunedmass_SR, allMyFiles);
  
  syst1B2sB.writeHistogramsSysts(h_bprimemass_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimept_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimeeta_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_bprimephi_CRB, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_AK4jet_selb_pt_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4jet_selb_eta_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK4jet_selb_phi_CRB, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_AK8jet_selh_pt_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK8jet_selh_eta_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_AK8jet_selh_phi_CRB, allMyFiles);

  syst1B2sB.writeHistogramsSysts(h_nsubj_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_tau2tau1_CRB, allMyFiles);
  syst1B2sB.writeHistogramsSysts(h_prunedmass_CRB, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_bprimemass_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimept_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimeeta_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimephi_CRC, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_AK4jet_selb_pt_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4jet_selb_eta_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4jet_selb_phi_CRC, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_AK8jet_selh_pt_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK8jet_selh_eta_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK8jet_selh_phi_CRC, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_nsubj_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_tau2tau1_CRC, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_prunedmass_CRC, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_bprimemass_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimept_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimeeta_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_bprimephi_CRD, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_AK4jet_selb_pt_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4jet_selb_eta_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK4jet_selb_phi_CRD, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_AK8jet_selh_pt_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK8jet_selh_eta_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_AK8jet_selh_phi_CRD, allMyFiles);

  syst1B1sB.writeHistogramsSysts(h_nsubj_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_tau2tau1_CRD, allMyFiles);
  syst1B1sB.writeHistogramsSysts(h_prunedmass_CRD, allMyFiles);

  fileout.close();
  
  std::cout<< "---> "<<sample<<std::endl;
  
  std::cout<< "**************************** "<<std::endl;
  std::cout<< "* Cutflow in Signal Region *    "<<std::endl;
  std::cout<< "**************************** "<<std::endl;
  
  std::cout<< "Number of Events           : "<<nEvents<<std::endl;
  std::cout<< "Events after trigger cut   : "<<n_trig<<std::endl;
  std::cout<< "Events after Ht cut        : "<<n_ht<<std::endl; 
  std::cout<< "Events after 1 ak8 jet     : "<<n_fatjet<<std::endl;
  std::cout<< "Events after 3 ak4 jets    : "<<n_jet<<std::endl;
  std::cout<< "Events after 1 higgs jet   : "<<n_Bosonjets<<std::endl;
  std::cout<< "Events after 1 b jet       : "<<n_bjets<<std::endl;
  //  std::cout<< "Events after Ht cut        : "<<n_ht<<std::endl;

  std::cout<< "****************************** "<<std::endl;
  std::cout<< "* Final yields in SR and CRs * "<<std::endl;
  std::cout<< "****************************** "<<std::endl;
  
  std::cout<< "Events in region A        : "<<nA<<std::endl;
  std::cout<< "Events in region B        : "<<nB<<std::endl;
  std::cout<< "Events in region C        : "<<nC<<std::endl;
  std::cout<< "Events in region D        : "<<nD<<std::endl;
  
  //  std::cout<< "Contamination in Closure Region: " << (float)n_closure/nA << std::endl;
  
}//end of main

TH1F * initproduct(TH1F * hA,TH1F* hB, int rebinA = 1, int rebinB=1,double integral = -1.){
  int nbinsA = hA->GetNbinsX();
  int nbinsB = hA->GetNbinsX();
  double min = hA->GetBinLowEdge(1)*hB->GetBinLowEdge(1);
  double max = hA->GetBinLowEdge(nbinsA+1)*hB->GetBinLowEdge(nbinsB+1);
  //Get the actual name from the original histograms 
  string name =(string)(hA->GetName()) +"_vs_"+ (string)(hB->GetName());
  
  //Initialize histogram 
  TH1F * result = new TH1F(name.c_str(),name.c_str(),nbinsA*nbinsB,min,max);
  return result;
}

TH1F * makeproduct(TH1F * hA,TH1F* hB, int rebinA = 1, int rebinB=1,double integral = -1.){

  //Make temporary histos to rebin
  //  TH1F *hA = (TH1F*)h_A->Clone("hA");
  // TH1F *hB = (TH1F*)h_B->Clone("hB");

  //  hA->Rebin(rebinA);
  // hB->Rebin(rebinB);
  
  //get nbins from new histos
  int nbinsA = hA->GetNbinsX();
  int nbinsB = hA->GetNbinsX();
  double min = hA->GetBinLowEdge(1)*hB->GetBinLowEdge(1);
  double max = hA->GetBinLowEdge(nbinsA+1)*hB->GetBinLowEdge(nbinsB+1);
  //Get the actual name from the original histograms 
  string name =(string)(hA->GetName()) +"_vs_"+ (string)(hB->GetName());
  
  //Initialize histogram 
  TH1F * result = new TH1F(name.c_str(),name.c_str(),nbinsA*nbinsB,min,max);
  //Fill histogram
  for(int i =1; i<= nbinsA;++i){
    for(int j =1; j<= nbinsB;++j){
      double value = hA->GetBinContent(i)*hB->GetBinContent(j);
      int k = ((i-1)*nbinsB)+j;
      result->SetBinContent(k,value);
    }
  }
  if( integral <= 0.)integral = hB->Integral()/result->Integral();
  else integral = integral / result->Integral();
  result->Scale(integral);
  return result;

}

//void initHistogramsSysts(TH1F* histo, TString name, TString, int, float, float , bool useOnlyNominal=false);

void systWeights::copySysts(systWeights sys){
  for(int i =0; i < sys.maxSysts;++i){
    this->weightedNames[i]=sys.weightedNames[i];
    this->weightedSysts[i]=sys.weightedSysts[i];

  }
  this->setMax(sys.maxSysts);
  this->setMaxNonPDF(sys.maxSystsNonPDF);
  this->nPDF=sys.nPDF;
  this->nCategories=sys.nCategories;  
  this->addQ2=sys.addQ2;
  this->addPDF=sys.addPDF;
  this->addTopPt=sys.addTopPt;
  this->addVHF=sys.addVHF;
  this->addTTSplit=sys.addTTSplit;
}


void systWeights::prepareDefault(bool addDefault, bool addQ2, bool addPDF, bool addTopPt,bool addVHF, bool addTTSplit, int numPDF){
  this->addPDF=addPDF;
  this->addQ2=addQ2;
  this->addTopPt=addTopPt;
  this->addVHF=addVHF;
  this->addTTSplit=addTTSplit;
  this->nPDF=numPDF;
  this->nCategories=1;
  categoriesNames[0]="";
  this->wCats[0]=1.0;
  if(addDefault){
    //    int MAX = this->maxSysts;
    this->weightedNames[0]="";
    this->weightedNames[1]="btagUp";
    this->weightedNames[2]="btagDown";
    this->weightedNames[3]="mistagUp";
    this->weightedNames[4]="mistagDown";
    this->weightedNames[5]="puUp";
    this->weightedNames[6]="puDown";
    this->weightedNames[9]="mistagHiggsUp";
    this->weightedNames[10]="mistagHiggsDown";
    //this->weightedNames[11]="trigUp";
    //this->weightedNames[12]="trigDown";
    this->setMax(11);
    this->setMaxNonPDF(11);
    this->weightedNames[this->maxSysts]="";
  }
  if(addQ2){
    this->weightedNames[this->maxSysts]= "q2Up";
    this->weightedNames[this->maxSysts+1]= "q2Down";
    this->setMax(this->maxSysts+2);
    this->setMaxNonPDF(this->maxSystsNonPDF+2);
    this->weightedNames[this->maxSysts]= "";
  }

  if(addTopPt){
    this->weightedNames[this->maxSysts]="topPtWeightUp";
    this->weightedNames[this->maxSysts+1]="topPtWeightDown";
    this->setMax(this->maxSysts+2);
    this->setMaxNonPDF(this->maxSystsNonPDF+2);
    this->weightedNames[this->maxSysts]= "";
  }
  

  if(addVHF){
    this->weightedNames[this->maxSysts]="VHFWeightUp";
    this->weightedNames[this->maxSysts+1]="VHFWeightDown";
    this->setMax(this->maxSysts+2);
    this->setMaxNonPDF(this->maxSystsNonPDF+2);
    this->weightedNames[this->maxSysts]= "";
  }

  if(addTTSplit){
    //    this->weightedNames[this->maxSysts]="2lep";
    //    this->weightedNames[this->maxSysts+1]="1lep";
    //    this->weightedNames[this->maxSysts+2]="0lep";
    //    this->setMax(this->maxSysts+3);
    //    this->setMaxNonPDF(this->maxSystsNonPDF+3);
    //    this->weightedNames[this->maxSysts]= "";
    this->nCategories=4;
    categoriesNames[1]="TT0lep";
    categoriesNames[2]="TT1lep";
    categoriesNames[3]="TT2lep";
    this->wCats[1]=1.0;
    this->wCats[2]=1.0;
    this->wCats[3]=1.0;

  }


  /*  if(addkFact){
    this->weightedNames[this->maxSysts]="VHFWeightUp";
    this->weightedNames[this->maxSysts+1]="VHFWeightDown";
    this->setMax(this->maxSysts+2);
    this->setMaxNonPDF(this->maxSystsNonPDF+2);
    this->weightedNames[this->maxSysts]= "";
    }*/

  if(addPDF){
    this->weightedNames[this->maxSysts]= "pdf_totalUp";
    this->weightedNames[this->maxSysts+1]= "pdf_totalDown";
    this->weightedNames[this->maxSysts+2]= "pdf_asUp";
    this->weightedNames[this->maxSysts+3]= "pdf_asDown";
    this->weightedNames[this->maxSysts+4]= "pdf_zmUp";
    this->weightedNames[this->maxSysts+5]= "pdf_zmDown";
    this->setMax(this->maxSysts+6);
    this->setMaxNonPDF(this->maxSystsNonPDF+6);
    int nPDF=this->nPDF;
    for(int i =0; i < nPDF;++i){
      stringstream ss;
      ss<< i+1;
      this->weightedNames[i+this->maxSysts]= "pdf"+ss.str();
    }
    this->setMax(maxSysts+nPDF);
    this->weightedNames[this->maxSysts]= "";
  }
  
}
void systWeights::addSyst(string name){
  this->weightedNames[this->maxSysts]= name;
  this->setMax(maxSysts+1);
  if(name.find("pdf")!=std::string::npos)this->setMaxNonPDF(maxSysts+1);
  this->weightedNames[this->maxSysts]= "";
}

void systWeights::addSystNonPDF(string name){
  this->weightedNames[this->maxSystsNonPDF]= name;
  this->setMaxNonPDF(maxSystsNonPDF+1);
  int nPDF=this->nPDF;
  for(int i =0; i < nPDF;++i){
    stringstream ss;
    ss<< i+1;
    this->weightedNames[i+this->maxSystsNonPDF]= "pdf"+ss.str();
  }
  this->setMax(maxSystsNonPDF+nPDF);
  this->weightedNames[this->maxSysts]= "";
}

void systWeights::addkFact(string name){
  string up=name+"Up";
  string down=name+"Down";
  cout << " adding syst "<< up<<endl;
  this->addSystNonPDF(up);
  this->addSystNonPDF(down);
}

void systWeights::setkFact(string name, float kfact_nom, float kfact_up,float kfact_down, bool mult){
  //  void setkFact(string name,float kfact_nom, float kfact_up,float kfact_down, float w_zero=1.0, mult=true);
  float zerofact=1.0;
  if(mult)zerofact=this->weightedSysts[0];
  string up = name+"Up";
  string down = name+"Down";
  float valueup=kfact_up/kfact_nom;
  float valuedown=kfact_down/kfact_nom;
  //  cout << "setting syst "<< up<<endl;
  //  cout << "values nom "<<kfact_nom<< " up "<< kfact_up << " down "<< kfact_down << " valup "<< valueup<< " valdown "<< valuedown <<" zerofact "<< zerofact<<endl;
  this->setSystValue(up, valueup*zerofact);
  this->setSystValue(down, valuedown*zerofact);
}

void systWeights::setPDFWeights(float * wpdfs, double * xsections, int numPDFs, float wzero, bool mult){
  float zerofact=1.0;
  if(mult)zerofact=this->weightedSysts[0];
  for (int i = 1; i <= numPDFs; ++i){
    this->setPDFValue(i,zerofact*wpdfs[i]/(wzero*xsections[i]));
  }
  this->setSystValue("pdf_asUp", this->getPDFValue(this->nPDF-2)/wzero);
  this->setSystValue("pdf_asDown", zerofact);
  this->setSystValue("pdf_zmUp", this->getPDFValue(this->nPDF-1)/wzero);
  this->setSystValue("pdf_zmDown", zerofact);
  this->setSystValue("pdf_totalUp", zerofact);
  this->setSystValue("pdf_totalDown", zerofact);
}

//void systWeights::setTWeight(float tweight, float totalweight){
void systWeights::setTWeight(float tweight, float wtotsample,bool mult){
  float zerofact=1.0;
  //  cout << " weighted syst 0 is "<< weightedSysts[0]<<endl;
  if(mult)zerofact=this->weightedSysts[0];
  this->setSystValue("topPtWeightUp", zerofact*tweight/wtotsample);
  this->setSystValue("topPtWeightDown", zerofact/tweight*wtotsample);
}

void systWeights::setVHFWeight(int vhf,bool mult,double shiftval){
  float zerofact=1.0;
  double w_shift=0.0;
  //  cout << "vhf is "<<vhf<<endl;
  if (vhf>1)w_shift=shiftval;
  //  cout << " weighted syst 0 is "<< weightedSysts[0]<<endl;
  if(mult)zerofact=this->weightedSysts[0];
  this->setSystValue("VHFWeightUp", zerofact*(1+w_shift));
  this->setSystValue("VHFWeightDown", zerofact*(1-w_shift));
}


void systWeights::setQ2Weights(float q2up, float q2down, float wzero, bool mult){
  float zerofact=1.0;
  if(mult){
    zerofact=this->weightedSysts[0];
    //    cout <<  "zerofact "<< zerofact << endl;
  }
  //cout <<  "zerofact "<< zerofact << " q2up weight "<< q2up/wzero << " tot to fill "<< zerofact*q2up/wzero<<endl;
  //cout <<  "zerofact "<< zerofact << " q2down weight "<< q2down/wzero << " tot to fill "<< zerofact*q2down/wzero<<endl;
  this->setSystValue("q2Up", zerofact*q2up/wzero);
  this->setSystValue("q2Down", zerofact*q2down/wzero);
}

double systWeights::getPDFValue(int numPDF){
  if(!addPDF){ cout << "error! No PDF used, this will do nothing."<<endl;return 0.;}
  int MIN = this->maxSystsNonPDF;
  return (double)this->weightedSysts[numPDF+MIN];

}
void systWeights::setPDFValue(int numPDF, double w){
  if(!addPDF){ cout << "error! No PDF used, this will do nothing."<<endl;return;}
  int MIN = this->maxSystsNonPDF;
  this->weightedSysts[numPDF+MIN]=w;

}

void systWeights::calcPDFHisto(TH1F** histo, TH1F* singleHisto, double scalefactor, int c){//EXPERIMENTAL
  if(!addPDF){ cout << "error! No PDF used, this will do nothing."<<endl;return;}
  int MAX = this->maxSysts;
  //  for (int c = 0; c < this->nCategories; c++){
    int MIN = this->maxSystsNonPDF+(MAX+1)*c;
    for(int b = 0; b< singleHisto->GetNbinsX();++b){
      float val = singleHisto->GetBinContent(b);
      //      cout << "bin # "<<b << " val "<<val<<endl;
      float mean = 0, devst=0;
      //      cout << "name is "<< singleHisto->GetName()<<endl;
      for(int i = 0; i<this->nPDF;++i ){
	//cout<< " now looking at pdf # "<<i<< " coordinate is "<< MIN+i<<endl;
	//	cout << "is histo there? "<< histo[i+MIN]<<endl;
	//	cout << " histo should be "<< (histo[i+MIN])->GetName()<<endl;
	mean = mean+ histo[i+MIN]->GetBinContent(b);
      }
      mean = mean/this->nPDF;
      //mean = val;//mean/this->nPDF;
      for(int i = 0; i<this->nPDF;++i ){
	devst+=(mean-histo[i+MIN]->GetBinContent(b))*(mean-histo[i+MIN]->GetBinContent(b));
      }
      devst= sqrt(devst/this->nPDF);
      singleHisto->SetBinContent(b,val+devst*scalefactor);
      //      singleHisto->SetBinContent(b,mean+devst*scalefactor);
    }
    //}
}

void systWeights::initHistogramsSysts(TH1F** histo,TString name, TString title, int nbins, float min, float max){
  for (int c = 0; c < this->nCategories; c++){
    int MAX = this->maxSysts;
    bool useOnlyNominal = this->onlyNominal;
    TString cname= (this->categoriesNames[c]).c_str();
    for(int sy=0;sy<(int)MAX;++sy){
      TString ns= (this->weightedNames[sy]).c_str();
      if(sy==0){
	if(c==0) histo[sy+((MAX+1)*(c))]=new TH1F(name,title,nbins,min,max);
	else histo[sy+((MAX+1)*(c))]=new TH1F(name+"_"+cname,title,nbins,min,max);
      }
      if(sy!=0 && !useOnlyNominal) {
	if(c==0)histo[sy+(MAX+1)*c]=new TH1F(name+"_"+ns,title,nbins,min,max);
	else histo[sy+(MAX+1)*c]=new TH1F(name+"_"+ns+"_"+cname,title,nbins,min,max);
      }
      //cout << " initialized histogram "<< histo[sy+(MAX+1)*c]->GetName() <<" sy " << sy << " c  "<< c <<" location " << sy+(MAX+1)*c << endl;

    }
  }
}

void systWeights::setOnlyNominal(bool useOnlyNominal){
  this->onlyNominal=useOnlyNominal;
}

void systWeights::setWCats(double * wcats){
  for(int i =0;i<this->nCategories;++i){
    //    cout << "setting wcat #"<< i << " to be "<<wcats[i]<<endl;
    this->wCats[i]=wcats[i];
  }
 
}

void systWeights::fillHistogramsSysts(TH1F** histo, float v, float w,  float *systWeights, int nFirstSysts, double * wcats, bool verbose){
  if(wcats== NULL){
    wcats = this->wCats;
  }
  //cout << *wcats << endl;
  for (int c = 0; c < this->nCategories; c++){
    int MAX = this->maxSysts;
    bool useOnlyNominal = this->onlyNominal;
    //cout << " filling histo " << histo[0+(MAX+1)*(c)]->GetName()<< endl;
    //cout << "MAX " << MAX <<endl;
    //cout << " filling histo " << histo[0+(MAX+1)*(c)]->GetName()<< " MAX "<<MAX*(1+c)<<" nFirstSysts"<< nFirstSysts<< endl;
    //    cout << "weight 0 "<< systWeights[0]<< " weighted syst 0 "<< this->weightedSysts[0]<<endl;
    for(int sy=0;sy<(int)MAX;++sy){
      //cout << wcats[c] << endl;
      //cout << "sy" << sy << endl;
      //cout << "filling histo " << histo[(int)sy]->GetName()<<endl;
      if(sy!=0 && useOnlyNominal)continue;
      float ws=1.0;
      if(sy<nFirstSysts){
	//cout << "wcats" << "\t" << wcats[c] << endl;
	wcats[c] =1.0;
	//ws=systWeights[sy];
	ws=systWeights[sy]*wcats[c];
	//cout << "wc" << wcats[c] << endl;
	//cout << sy<<"\t"<<systWeights[sy] << endl; 
	//cout << "ws" << ws << endl;
	//cout << sy<<"\t"<<systWeights[sy] << endl;
      }
      else {
	//cout << "wcats" << "\t" << wcats[c] << endl;
	wcats[c] =1.0;
	ws = (this->weightedSysts[(int)sy]*wcats[c]);
	//ws = (this->weightedSysts[(int)sy]);
	//cout << "ws" << ws << endl;
	//cout << this->weightedSysts[(int)sy] << endl;
      }
      //cout << ws << endl;
      //cout << "filling histo " << histo[sy+1]->GetName()<<" value "<< v << " wevt "<< w << " syst number "<< sy<< " name "<< weightedNames[sy]<<" ws value " <<ws<< " wcats" << wcats[c] << endl;    
      //cout <</* "filling histo "<< histo[sy+((MAX+1)*(c))]->GetName()<<*/" value "<< v << " wevt "<< w << " syst number "<< sy<< " name "<< weightedNames[sy]<<" ws value " <<ws<<endl;
      //cout << "c\t" << c << endl;
      //cout << MAX << endl;
      //cout << sy << endl;
      //cout <<sy+((MAX+1)*(c)) << endl;
      //cout << "filling histo " << histo[sy]->GetName()<<endl;
      //histo[1]->Fill(v);
      histo[sy+(MAX+1)*(c)]->Fill(v, w * ws);
      //cout << histo[sy+(MAX+1)*(c)]->Integral() << " " << v << " " << w << " " << ws << endl;
    }
  }
}

void systWeights::fillHistogramsSysts(TH1F** histo, float v, float w, double * wcats, bool verbose ){
  if(wcats==NULL){
    wcats=this->wCats;
  }
  for (int c = 0; c < this->nCategories; c++){
    int MAX = this->maxSysts;
    bool useOnlyNominal = this->onlyNominal;
    for(int sy=0;sy<(int)MAX;++sy){
      if(sy!=0 && useOnlyNominal)continue;
      float ws = (this->weightedSysts[(int)sy])*wcats[c];
      // cout << " filling histogram "<< histo[(int)sy]->GetName() << " with value "<< v <<" and weight "<< w <<" ws "<< ws<<endl;
      histo[sy+(MAX+1)*(c)]->Fill(v, w*ws);
    }
  }
}


void systWeights::createFilesSysts(  TFile ** allFiles, TString basename, TString opt){
  for (int c = 0; c < this->nCategories; c++){
    int MAX = this->maxSystsNonPDF;
    int MAXTOT = this->maxSystsNonPDF;
    bool useOnlyNominal = this->onlyNominal;
    TString cname= (this->categoriesNames[c]).c_str();
    if (c!=0) cname= "_"+cname;
    for(int sy=0;sy<(int)MAX;++sy){
      TString ns= (this->weightedNames[(int)sy]);
      cout << " creating file for syst "<< ns<<endl;
      if (c!=0)     cout << " category is "<< c<<endl;
      cout << "onlynominal is "<<useOnlyNominal<<endl;

      //    "/afs/cern.ch/user/o/oiorio/public/xAnnapaola/Nov10/res/"+sample + "_" +channel+".root";
      if(sy==0){
	//cout<<" filename is "<< basename+ns+cname+".root"<<endl;
	allFiles[sy+(MAX+1)*c]= TFile::Open((basename+ns+cname+".root"), opt);
      }
      else{
	if(!useOnlyNominal){
	  //if((ns!="1lep") && (ns!="2lep")&& (ns!="0lep")){
	  //	  cout<<" filename is "<< basename+ns+cname+".root"<<endl;
	  allFiles[sy+(MAX+1)*c]= TFile::Open((basename+"_"+ns+cname+".root"), opt);
	}
      }
      //TFile *outTree = TFile::Open(("trees/tree_"+outFileName).c_str(), "RECREATE");
      //cout << " created file at c "<< c << " s "<< sy << " location "<< sy+(MAXTOT+1)*c<< " fname "<<allFiles[sy+(MAXTOT+1)*c]->GetName()<<endl;   
    }
    if(this->addPDF){
      if(!useOnlyNominal)allFiles[MAX+((MAX+1)*c)]= TFile::Open((basename+"_pdf"+cname+".root"), opt);
      //cout << " created file at c "<< c << " s "<< MAX+(MAX+1)*c << " location "<< MAX+(MAX+1)*c<<endl;
      cout<< " fname "<<allFiles[MAX+(MAXTOT+1)*c]->GetName()<<endl;   
    }
  }
  //return allFiles;
}

void systWeights::writeHistogramsSysts(TH1F** histo, TFile **filesout){  
  int MAX= this->maxSystsNonPDF;
  int MAXTOT= this->maxSysts;
  bool useOnlyNominal = this->onlyNominal;
  for (int c = 0; c < this->nCategories; c++){
    TString cname= (this->categoriesNames[c]).c_str();
    if (c!=0) cname= "_"+cname;
    for(int sy=0;sy<(int)MAX;++sy){
      //      cout << "c is now "<< c << " sy "<< sy << " location "<< sy+(MAXTOT+1)*c <<" is histo there? " << histo[sy+(MAXTOT+1)*c] << " file location "<<sy+(MAX+1)*c << " is file there "<< filesout[sy+(MAX+1)*c]<< endl;
      //      cout << " writing histo "<< histo[sy+(MAXTOT+1)*c]->GetName()<< " in file "<< filesout[sy+(MAX+1)*c]->GetName()<<endl;;
      //TString ns= weightedSystsNames((weightedSysts)sy);
      if(!(!useOnlyNominal || sy==0)) continue;
      
      filesout[(int)sy+(MAX+1)*(c)]->cd();
      if(this->addPDF){
	if(this->weightedNames[sy]=="pdf_totalUp")calcPDFHisto(histo, histo[sy+(MAXTOT+1)*(c)],1.0,c);
	if(this->weightedNames[sy]=="pdf_totalDown")calcPDFHisto(histo, histo[sy+(MAXTOT+1)*(c)],-1.0,c);
	;      //this->
      }
      
      histo[sy+(MAXTOT+1)*c]->Write(histo[0]->GetName());
      //    histo[sy]=new TH1F(name+ns,name+ns,nbins,min,max);
      //    filesout[(int)sy]->Close();
    }
    if(this->addPDF){
      if(!useOnlyNominal){
	filesout[MAX+(MAX+1)*(c)]->cd();
	//	cout << " file max is "<< filesout[MAX+(MAX+1)*c]->GetName()<<endl;
	//	int npdf=this->maxSysts-this->maxSystsNonPdf;
	int MAXPDF=this->maxSysts;
	for(int sy=MAX;sy<MAXPDF;++sy){
	  //	  cout << " writing sy "<<sy+(MAXTOT+1)*c<<endl;
	  //	  cout << " histo is there? "<< histo[sy+(MAXTOT+1)*c]<<endl;
	  histo[sy+(MAXTOT+1)*(c)]->Write();
	  //	  cout << " written sy "<< histo[sy+(MAXTOT+1)*c]->GetName()<<endl;
	}
      }
    }
  }
}

void systWeights::writeSingleHistogramSysts(TH1F* histo, TFile **filesout){  
  int MAX= this->maxSystsNonPDF;
  bool useOnlyNominal = this->onlyNominal;
  for (int c = 0; c < this->nCategories; c++){
    TString cname= (this->categoriesNames[c]).c_str();
    if (c!=0) cname= "_"+cname;
    for(int sy=0;sy<(int)MAX;++sy){
      if(!(!useOnlyNominal || sy==0)) continue;
      //cout << " writing histo "<< histo->GetName()<< " in file "<< filesout[(int)sy]->GetName()<<endl;;
      filesout[(int)sy+(MAX+1)*c]->cd();
      histo->Write();
      //    histo[sy]=new TH1F(name+ns,name+ns,nbins,min,max);
    }
    if(this->addPDF){
      if(!useOnlyNominal){
	filesout[MAX+(MAX+1)*c]->cd();
	int MAXPDF=this->maxSysts;
	for(int sy=MAX;sy<MAXPDF;++sy){
	  //      cout << " writing sy "<< histo[sy]->GetName()<<endl;
	  histo->Write();
	  //      cout << " written sy "<< histo[sy]->GetName()<<endl;
	}
      }
    }
  }
}


void systWeights::setMax(int max){
  this->maxSysts =  max;
}
void systWeights::setMaxNonPDF(int max){
  this->maxSystsNonPDF =  max;
}
void systWeights::setSystValue(string name, double value, bool mult){
  float zerofact=1.0;
  if(mult)zerofact=this->weightedSysts[0];
  int MAX = this->maxSysts;
  for(int sy=0;sy<(int)MAX;++sy){
    if(this->weightedNames[(int)sy] ==name){
      this->weightedSysts[(int)sy] =value*zerofact;
    }
  }
}

void systWeights::setSystValue(int place, double value, bool mult){
  float zerofact=1.0;
  if(mult)zerofact=this->weightedSysts[0];
  this->weightedSysts[place] =value*zerofact;
}

void systWeights::setWeight(string name, double value, bool mult){
  this->setSystValue(name, value, mult);
}

void systWeights::setWeight(int place, double value, bool mult){
  this->setSystValue(place, value, mult);
}

TString  weightedSystsNames (weightedSysts sy){
  switch(sy){
  case NOSYST : return "";
  case BTAGUP : return "btagUp";
  case BTAGDOWN : return "btagDown";
  case MISTAGUP : return "mistagUp";
  case MISTAGDOWN : return "mistagDown";
  case PUUP : return "puUp";
  case PUDOWN : return "puDown";
  case MISTAGHIGGSUP : return "mistagtagHiggsUp";
  case MISTAGHIGGSDOWN : return "mistagHiggsDown";
  case MAXSYSTS : return "";
  }
  return "noSyst";
}

void  initHistogramsSysts (TH1F* histo[(int)MAXSYSTS],TString name, TString title, int nbins, float min, float max, bool useOnlyNominal=false){
  for(int sy=0;sy<(int)MAXSYSTS;++sy){
    TString ns= weightedSystsNames((weightedSysts)sy);
    histo[sy]=new TH1F(name+ns,title,nbins,min,max);
  }
}

void fillHistogramsSysts(TH1F* histo[(int)MAXSYSTS], float v, float w, float systWeight[(int)MAXSYSTS] , bool useOnlyNominal=false){
  for(int sy=0;sy<(int)MAXSYSTS;++sy){
    float ws = systWeight[(int)sy];
    histo[sy]->Fill(v, w*ws);
  }
}

void createFilesSysts(  TFile * allFiles[(int)MAXSYSTS], TString basename, bool useOnlyNominal=false,TString opt = "RECREATE"){
  for(int sy=0;sy<(int)MAXSYSTS;++sy){
    TString ns= weightedSystsNames((weightedSysts)sy);
    //    "/afs/cern.ch/user/o/oiorio/public/xAnnapaola/Nov10/res/"+sample + "_" +channel+".root";
    if(sy==0){
	allFiles[sy]= TFile::Open((basename+ns+".root"), opt);}
    else{
      if(!useOnlyNominal) allFiles[sy]= TFile::Open((basename+"_"+ns+".root"), opt);}
    //TFile *outTree = TFile::Open(("trees/tree_"+outFileName).c_str(), "RECREATE");
    
  }
  //return allFiles;
}

void writeHistogramsSysts(TH1F* histo[(int)MAXSYSTS], TFile *filesout[(int)MAXSYSTS], bool useOnlyNominal=false){  
  for(int sy=0;sy<(int)MAXSYSTS;++sy){
    //cout << " writing histo "<< histo[(int)sy]->GetName()<< " in file "<< filesout[(int)sy]->GetName()<<endl;;
    //TString ns= weightedSystsNames((weightedSysts)sy);
    filesout[(int)sy]->cd();
    histo[sy]->Write(histo[0]->GetName());
    //    histo[sy]=new TH1F(name+ns,name+ns,nbins,min,max);
  }
}

void writeSingleHistogramSysts(TH1F* histo, TFile *filesout[(int)MAXSYSTS], bool useOnlyNominal=false){  
  for(int sy=0;sy<(int)MAXSYSTS;++sy){
    cout << " writing histo "<< histo->GetName()<< " in file "<< filesout[(int)sy]->GetName()<<endl;;
    //TString ns= weightedSystsNames((weightedSysts)sy);
    filesout[(int)sy]->cd();
    histo->Write();
    //    histo[sy]=new TH1F(name+ns,name+ns,nbins,min,max);
  }
}

TH1F * makeproduct(TH2F * h){

  //Make temporary histos to rebin
  //  TH1F *hA = (TH1F*)h_A->Clone("hA");
  // TH1F *hB = (TH1F*)h_B->Clone("hB");

  //  hA->Rebin(rebinA);
  // hB->Rebin(rebinB);
  
  //get nbins from new histos
  int nbinsA = h->GetNbinsX();
  int nbinsB = h->GetNbinsY();
  double min = h->GetXaxis()->GetBinLowEdge(1)*h->GetYaxis()->GetBinLowEdge(1);
  double max = h->GetXaxis()->GetBinLowEdge(nbinsA+1)*h->GetYaxis()->GetBinLowEdge(nbinsB+1);
  //Get the actual name from the original histograms 
  string name = (string)(h->GetName()) + "_1D";
  
  //Initialize histogram 
  TH1F * result = new TH1F(name.c_str(),name.c_str(),nbinsA*nbinsB,min,max);
  //Fill histogram
  for(int i =1; i<= nbinsA;++i){
    for(int j =1; j<= nbinsB;++j){
      double value = h->GetBinContent(i,j);
      int k = ((i-1)*nbinsB)+j;
      result->SetBinContent(k,value);
    }
  }
  //  if( integral <= 0.)integral = hA->Integral()/result->Integral();
  //else integral = integral / result->Integral();
  //result->Scale(integral);
  return result;

}
