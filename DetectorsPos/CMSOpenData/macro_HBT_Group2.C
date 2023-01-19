

//to reject a range in the fit -- here was not needed to remove any range...so, just used a dummy range... :-)
Double_t reject_range_min = 0.0;
Double_t reject_range_max = 0.00001;


Double_t func1_exp(Double_t* x, Double_t* par){
Double_t v = 0;
if(reject_range_min<x[0] && x[0]<reject_range_max){TF1::RejectPoint();}
else{v= par[0]*(1 + par[1]*exp(-par[2]*x[0]/0.1973))*(1+par[3]*x[0]);}
return v;
}

Double_t func2_gauss(Double_t* x, Double_t* par){
Double_t v = 0;
if(reject_range_min<x[0] && x[0]<reject_range_max){TF1::RejectPoint();}
else{v= par[0]*(1 + par[1]*exp(-pow(par[2]*x[0]/0.1973,2.)))*(1+par[3]*x[0]);}
return v;
}

//Main function
void macro_HBT_Group2(){

auto fileName = "HBT_histos_Group2.root";
TFile *f = TFile::Open(fileName);

TH1D * h_qinv_sig_SS_Ccorr = (TH1D*) f->Get("hqinvSigSS_Ccorr");
TH1D * h_qinv_sig_OS_Ccorr = (TH1D*) f->Get("hqinvSigOS_Ccorr");

auto c = new TCanvas("c", "", 500, 500);
c->cd();

TH1D * h_qinv_sig_SS_Ccorr_clone = (TH1D *)h_qinv_sig_SS_Ccorr->Clone("h_qinv_sig_SS_Ccorr_clone");
TH1D * h_qinv_sig_OS_Ccorr_clone = (TH1D *)h_qinv_sig_OS_Ccorr->Clone("h_qinv_sig_OS_Ccorr_clone");
Int_t bin_for_normInt_min = h_qinv_sig_SS_Ccorr_clone->GetXaxis()->FindBin(0.6001);
Int_t bin_for_normInt_max = h_qinv_sig_SS_Ccorr_clone->GetXaxis()->FindBin(0.9999);
Double_t int_num_controlRegion = h_qinv_sig_SS_Ccorr_clone->Integral(bin_for_normInt_min,bin_for_normInt_max);
Double_t int_den_controlRegion = h_qinv_sig_OS_Ccorr_clone->Integral(bin_for_normInt_min,bin_for_normInt_max);
h_qinv_sig_OS_Ccorr_clone->Scale(int_num_controlRegion/int_den_controlRegion);
h_qinv_sig_SS_Ccorr_clone->Divide(h_qinv_sig_OS_Ccorr_clone);
h_qinv_sig_SS_Ccorr_clone->SetLineColor(1);
h_qinv_sig_SS_Ccorr_clone->SetMarkerColor(1);
h_qinv_sig_SS_Ccorr_clone->SetTitle("");

//Setting function for double ratio
TF1 *f_exp = new TF1("f_exp",func1_exp,0.02, 0.5, 4); 
f_exp->SetParameters(1.0,1.0,4.0,0.0);
f_exp->SetParName(0,"Const");
f_exp->SetParLimits(0,0.0,2.0);//The specified limits will be used in a fit operation when the option "B" is specified (Bounds). To fix a parameter, use TF1::FixParameter.
f_exp->SetParName(1,"#lambda");
f_exp->SetParLimits(1,0.0,2.0);
f_exp->SetParName(2,"R (fm)");
f_exp->SetParName(3,"#delta");
f_exp->SetLineColor(kRed); 
f_exp->SetLineWidth(2);  
h_qinv_sig_SS_Ccorr_clone->Draw("pError");
h_qinv_sig_SS_Ccorr_clone->GetYaxis()->SetTitle("Single Ratio (SR)");
h_qinv_sig_SS_Ccorr_clone->GetXaxis()->SetTitle("q_{inv} [GeV]");
TFitResultPtr res_exp;
ROOT::Math::MinimizerOptions::SetDefaultMinimizer("Minuit2");
res_exp = h_qinv_sig_SS_Ccorr_clone->Fit(f_exp, "S R"); 
f_exp->Draw("SameL");

TF1 *f_gauss = new TF1("f_gauss",func2_gauss,0.02, 0.5, 4);
f_gauss->SetParameters(1.0,1.0,4.0,0.0);
f_gauss->SetParName(0,"Const");
f_gauss->SetParLimits(0,0.0,2.0);
f_gauss->SetParName(1,"#lambda");
f_gauss->SetParLimits(1,0.0,2.0);
f_gauss->SetParName(2,"R (fm)");
f_gauss->SetParName(3,"#delta");
f_gauss->SetLineColor(kBlue); 
f_gauss->SetLineWidth(2);
TFitResultPtr res_gauss;
res_gauss = h_qinv_sig_SS_Ccorr_clone->Fit(f_gauss, "S R");
f_gauss->Draw("SameL");
gPad->SetLogy(0);
gStyle->SetOptStat(0);
c->Print("plot_SR_plusFits_Group2.pdf");
c->Update();

}	
