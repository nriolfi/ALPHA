
variable = {}

var_template = {
    # Event
    "EventNumber": {
      "title" : "event number",
      "nbins" : 10000000,
      "min" : 0,
      "max" : 1.e7,
      "log" : False,
    },
    "LumiNumber": {
      "title" : "lumisection number",
      "nbins" : 2000,
      "min" : 0,
      "max" : 2000,
      "log" : False,
    },
    "RunNumber": {
      "title" : "run number",
      "nbins" : 7000,
      "min" : 254000,
      "max" : 261000,
      "log" : False,
    },
    "Rho": {
      "title" : "rho",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    "EventWeight": {
      "title" : "event weight",
      "nbins" : 50,
      "min" : 0.,
      "max" : 5.,
      "log" : False,
    },
    "TriggerWeight": {
      "title" : "trigger weight",
      "nbins" : 50,
      "min" : 0.,
      "max" : 2.,
      "log" : False,
    },
    "PUWeight": {
      "title" : "pilu-up weight",
      "nbins" : 50,
      "min" : 0.,
      "max" : 5.,
      "log" : False,
    },
    "LeptonWeight": {
      "title" : "lepton weight",
      "nbins" : 50,
      "min" : 0.,
      "max" : 5.,
      "log" : False,
    },
    "nPV": {
      "title" : "number of reconstructed Primary Vertices",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : False,
    },
    "nElectrons": {
      "title" : "number of electrons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nMuons": {
      "title" : "number of muons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nTaus": {
      "title" : "number of taus",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nPhotons": {
      "title" : "number of photons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nJets": {
      "title" : "number of jets",
      "nbins" : 10,
      "min" : -0.5,
      "max" : 9.5,
      "log" : True,
    },
    "nFatJets": {
      "title" : "number of AK8 jets",
      "nbins" : 5,
      "min" : 0.5,
      "max" : 5.5,
      "log" : True,
    },
    "nBJets": {
      "title" : "number of b-jets",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nBtagJets": {
      "title" : "number of b-jets",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "genNl": {
      "title" : "number of leptons at generation level",
      "nbins" : 4,
      "min" : -0.5,
      "max" : 3.5,
      "log" : True,
    },
    
    
    # MET
#    "MEt.pt": {
#      "title" : "#slash{E}_{T} (GeV)",
#      "nbins" : -1,
#      "bins" : [200, 300, 400, 500, 700, 1000],
#      "min" : 0,
#      "max" : 0,
#      "log" : True,
#    },
#    "MEt.pt": {
#      "title" : "#slash{E}_{T} (GeV)",
#      "nbins" : 10,
#      "min" : 200,
#      "max" : 1200,
#      "log" : True,
#    },
    "MEt.pt": {
      "title" : "#slash{E}_{T} (GeV)",
      "nbins" : 100,
      "min" : 0,
      "max" : 400,
      "log" : True,
    },
    "MEt.phi": {
      "title" : "#slash{E}_{T} #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "MEt.ptRaw": {
      "title" : "raw #slash{E}_{T} (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "corMEt.pt": {
      "title" : "#slash{E}_{T} (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "corMEt.ptScaleUp": {
      "title" : "#slash{E}_{T} (scale up) (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "corMEt.ptScaleDown": {
      "title" : "#slash{E}_{T} (scale down) (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "corMEt.ptResUp": {
      "title" : "#slash{E}_{T} (resolution up) (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "corMEt.ptResDown": {
      "title" : "#slash{E}_{T} (resolution Down) (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "fakeMEt.pt": {
      "title" : "hadronic recoil (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "fakeMEt.phi": {
      "title" : "hadronic recoil #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "fakecorMEt.pt": {
      "title" : "hadronic recoil (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "fakecorMEt.phi": {
      "title" : "hadronic recoil #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "HT": {
      "title" : "HT (GeV)",
      "nbins" : 100,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "nJetsNoFatJet150": {
      "title" : "number of jets with p_{T}>150 GeV",
      "nbins" : 10,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },
    "nJetsNoFatJet100": {
      "title" : "number of jets with p_{T}>100 GeV",
      "nbins" : 10,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },
    "nJetsNoFatJet50": {
      "title" : "number of jets with p_{T}>50 GeV",
      "nbins" : 10,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },
    "nJetsNoFatJet30": {
      "title" : "number of jets with p_{T}>30 GeV",
      "nbins" : 10,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },
    "maxCSVNoFatJet": {
      "title" : "max CSV, fat jet excluded",
      "nbins" : 25,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "minDeltaPhi": {
      "title" : "min #Delta #varphi (jet-#slash{E}_{T})",
      "nbins" : 28,
      "min" : 0,
      "max" : 3.15,
      "log" : True,
    },
    "minDeltaPhiNoFatJet": {
      "title" : "min #Delta #varphi (jet-#slash{E}_{T})",
      "nbins" : 28,
      "min" : 0,
      "max" : 3.15,
      "log" : True,
    },
    
    # Jets
    "Jet[N].pt": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },
    "Jet[N].eta": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : False,
    },
    "Jet[N].phi": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "Jet[N].mass": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "Jet[N].dPhi_met": {
      "title" : "#Delta #varphi  jet[N]-#slash{E}_{T}",
      "nbins" : 14,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "Jet[N].dPhi_jet1": {
      "title" : "#Delta #varphi  jet[N]-jet1",
      "nbins" : 14,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "Jet[N].CSV": {
      "title" : "jet [N] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].CSVR": {
      "title" : "jet [N] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].CSVRUp": {
      "title" : "jet [N] CSV (+1 #sigma)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].CSVRDown": {
      "title" : "jet [N] CSV (-1 #sigma)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].flavour": {
      "title" : "jet [N] flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "Jet[N].chf": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].nhf": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].phf": {
      "title" : "jet [N] photon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].elf": {
      "title" : "jet [N] electron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].muf": {
      "title" : "jet [N] muon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "Jet[N].chm": {
      "title" : "jet [N] charged multiplicity",
      "nbins" : 20,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    "Jet[N].npr": {
      "title" : "jet [N] constituents multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    
    # Fatjets
    "FatJet[N].pt": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 18,
      "min" : 200,
      "max" : 2000,
      "log" : True,
    },
    "FatJet[N].eta": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : False,
    },
    "FatJet[N].phi": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "FatJet[N].mass": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "FatJet[N].prunedMass": {
      "title" : "jet pruned mass (GeV)",
      "nbins" : 60,
      "min" : 0,
      "max" : 300,
      "log" : False,
    },
    "FatJet[N].prunedMassCorr": {
      "title" : "jet pruned mass (GeV)",
      "nbins" : 60,
      "min" : 0,
      "max" : 300,
      "log" : False,
    },
    "FatJet[N].softdropMass": {
      "title" : "jet soft drop mass (GeV)",
      "nbins" : 20,
      "min" : 0.,
      "max" : 200.,
      "log" : False,
    },
    "FatJet[N].softdropMassCorr": {
      "title" : "jet soft drop mass (GeV)",
      "nbins" : 20,
      "min" : 0.,
      "max" : 200.,
      "log" : False,
    },
    "FatJet[N].softdropPuppiMass": {
      "title" : "jet PUPPI soft drop mass (GeV)",
      "nbins" : 20,
      "min" : 0.,
      "max" : 200.,
      "log" : False,
    },
    "FatJet[N].softdropPuppiMassCorr": {
      "title" : "jet PUPPI soft drop mass (GeV)",
      "nbins" : 20,
      "min" : 0.,
      "max" : 200.,
      "log" : False,
    },
    "FatJet[N].dR": {
      "title" : "subjets #Delta R",
      "nbins" : 20,
      "min" : 0,
      "max" : 1.,
      "log" : False,
    },
    "FatJet[N].dPhi_met": {
      "title" : "#Delta #varphi (jet-#slash{E}_{T})",
      "nbins" : 50,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "FatJet[N].tau21": {
      "title" : "#tau_{2} / #tau_{1}",
      "nbins" : 25,
      "min" : 0,
      "max" : 1.,
      "log" : False,
    },
    "FatJet[N].CSV": {
      "title" : "fatjet CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].CSV1": {
      "title" : "subjet 1 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].CSV2": {
      "title" : "subjet 2 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].CSVR1": {
      "title" : "subjet 1 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].CSVR2": {
      "title" : "subjet 2 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].nBtag": {
      "title" : "number of b-tagged subjets",
      "nbins" : 3,
      "min" : -0.5,
      "max" : 2.5,
      "log" : True,
    },
    "FatJet[N].flavour": {
      "title" : "fatjet flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "FatJet[N].flavour1": {
      "title" : "subjet 1 flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "FatJet[N].flavour2": {
      "title" : "subjet 2 flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "FatJet[N].chf": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].nhf": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].phf": {
      "title" : "jet [N] photon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].elf": {
      "title" : "jet [N] electron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].muf": {
      "title" : "jet [N] muon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "FatJet[N].chm": {
      "title" : "jet [N] charged multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    "FatJet[N].npr": {
      "title" : "jet [N] constituents multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 100,
      "log" : False,
    },
    
    
    # Leptons
    "Lepton[N].pt": {
      "title" : "lepton [N] p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 500,
      "log" : True,
    },
    "Lepton[N].eta": {
      "title" : "lepton [N] #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "Lepton[N].phi": {
      "title" : "lepton [N] #varphi",
      "nbins" : 30,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "Lepton[N].mass": {
      "title" : "lepton [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "Lepton[N].dPhi_met": {
      "title" : "lepton [N] #varphi (l-#slash{E}_{T})",
      "nbins" : 30,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "Lepton[N].isElectron": {
      "title" : "isElectron",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "Lepton[N].isMuon": {
      "title" : "isMuon",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "Lepton[N].charge": {
      "title" : "lepton [N] charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "Lepton[N].dxy": {
      "title" : "lepton [N] d_{xy}",
      "nbins" : 50,
      "min" : -0.02,
      "max" : 0.02,
      "log" : True,
    },
    "Lepton[N].dz": {
      "title" : "lepton [N] d_{z}",
      "nbins" : 50,
      "min" : -0.05,
      "max" : 0.05,
      "log" : True,
    },
    "Lepton[N].relIso03": {
      "title" : "lepton [N] PFIso_{03}",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.25,
      "log" : True,
    },
    "Lepton[N].relIso04": {
      "title" : "lepton [N] PFIso_{04}",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.25,
      "log" : True,
    },
    "Lepton[N].trkIso": {
      "title" : "lepton [N] tracker Iso",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "Lepton[N].miniIso": {
      "title" : "lepton [N] miniIso",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "Lepton[N].looseId": {
      "title" : "loose Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "Lepton[N].mediumId": {
      "title" : "medium Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "Lepton[N].tightId": {
      "title" : "tight Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "Lepton[N].highptId": {
      "title" : "high pT Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    
    # Candidates
    "V.pt": {
      "title" : "Z candidate p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "V.eta": {
      "title" : "Z candidate #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "V.phi": {
      "title" : "Z candidate #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "V.mass": {
      "title" : "m_{Z} (GeV)",
      "nbins" : 75,
      "min" : 50,
      "max" : 125,
      "log" : False,
    },
    "V.charge": {
      "title" : "Z candidate charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "V.dR": {
      "title" : "#Delta R (ll)",
      "nbins" : 40,
      "min" : 0,
      "max" : 2,
      "log" : False,
    },
    "V.dEta": {
      "title" : "#Delta #eta (ll)",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "V.dPhi": {
      "title" : "#Delta #varphi (ll)",
      "nbins" : 50,
      "min" : 0,
      "max" : 3.14,
      "log" : False,
    },
    
    #
    "H.pt": {
      "title" : "Z candidate p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "H.eta": {
      "title" : "Z candidate #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "H.phi": {
      "title" : "Z candidate #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "H.mass": {
      "title" : "m_{Z} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 250,
      "log" : False,
    },
    "H.charge": {
      "title" : "Z candidate charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "H.dR": {
      "title" : "#Delta R (jj)",
      "nbins" : 40,
      "min" : 0,
      "max" : 2,
      "log" : False,
    },
    "H.dEta": {
      "title" : "#Delta #eta (jj)",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "H.dPhi": {
      "title" : "#Delta #varphi (jj)",
      "nbins" : 50,
      "min" : 0,
      "max" : 3.14,
      "log" : False,
    },
    
    # X
    "X.pt": {
      "title" : "p_{T} (ZZ) (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 500,
      "log" : True,
    },
    "X.eta": {
      "title" : "#eta(ZZ)",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "X.phi": {
      "title" : "#varphi(ZZ)",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "X.mass": {
      "title" : "m (ZZ) (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : False,
    },
    "X.charge": {
      "title" : "X candidate charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "X.dR": {
      "title" : "#Delta R (ZZ)",
      "nbins" : 40,
      "min" : 0,
      "max" : 2,
      "log" : False,
    },
    "X.dEta": {
      "title" : "#Delta #eta (ZZ)",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "X.dPhi": {
      "title" : "#Delta #varphi (ZZ)",
      "nbins" : 50,
      "min" : 0,
      "max" : 3.14,
      "log" : False,
    },
    
#    # W
#    "W_pt": {
#      "title" : "W candidate p_{T} (GeV)",
#      "nbins" : 25,
#      "min" : 0,
#      "max" : 500,
#      "log" : True,
#    },
#    "W_eta": {
#      "title" : "W candidate #eta",
#      "nbins" : 30,
#      "min" : -3.,
#      "max" : 3.,
#      "log" : False,
#    },
#    "W_phi": {
#      "title" : "W candidate #varphi",
#      "nbins" : 60,
#      "min" : -3.15,
#      "max" : 3.15,
#      "log" : False,
#    },
#    "W_tmass": {
#      "title" : "W candidate m_{T} (GeV)",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 200,
#      "log" : False,
#    },
#    "W_charge": {
#      "title" : "W candidate charge",
#      "nbins" : 3,
#      "min" : -1.5,
#      "max" : 1.5,
#      "log" : False,
#    },
#    "W_dR": {
#      "title" : "#Delta R_{l-#slash{E}_{T}}",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 5,
#      "log" : False,
#    },
#    "W_dEta": {
#      "title" : "#Delta #eta_{l-#slash{E}_{T}}",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 5,
#      "log" : False,
#    },
#    "W_dPhi": {
#      "title" : "#Delta #varphi_{l-#slash{E}_{T}}",
#      "nbins" : 30,
#      "min" : 0,
#      "max" : 3.14,
#      "log" : False,
#    },
#    "kW_pt": {
#      "title" : "W candidate p_{T} (GeV)",
#      "nbins" : 25,
#      "min" : 200,
#      "max" : 1200,
#      "log" : True,
#    },
#    "kW_eta": {
#      "title" : "W candidate #eta",
#      "nbins" : 30,
#      "min" : -3.,
#      "max" : 3.,
#      "log" : False,
#    },
#    "kW_phi": {
#      "title" : "W candidate #varphi",
#      "nbins" : 30,
#      "min" : -3.15,
#      "max" : 3.15,
#      "log" : False,
#    },
#    "kW_dPhi": {
#      "title" : "#Delta #varphi (l-#slash{E}_{T})",
#      "nbins" : 30,
#      "min" : 0,
#      "max" : 3.14,
#      "log" : False,
#    },
#    "kW_mass": {
#      "title" : "W candidate mass (GeV)",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 200,
#      "log" : False,
#    },
#    "T_mass": {
#      "title" : "Top candidate mass (GeV)",
#      "nbins" : 80,
#      "min" : 0,
#      "max" : 800,
#      "log" : False,
#    },
#    
#    # X
#    "X_pt": {
#      "title" : "X candidate p_{T} (GeV)",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 1000,
#      "log" : True,
#    },
#    "X_eta": {
#      "title" : "X candidate #eta",
#      "nbins" : 30,
#      "min" : -3.,
#      "max" : 3.,
#      "log" : False,
#    },
#    "X_phi": {
#      "title" : "X candidate #varphi",
#      "nbins" : 60,
#      "min" : -3.15,
#      "max" : 3.15,
#      "log" : False,
#    },
#    "X_mass": {
#      "title" : "m_{Vh} (GeV)",
#      "nbins" : 70,
#      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
#      #"bins" : [500, 583, 678, 785, 904, 1035, 1178, 1333, 1500, 1679, 1870, 2073, 2288, 2515, 2754, 3005, 3268, 3543, 3830, 4129, 4600],
#      "bins" : [x*(1+0.1*x)*40+800 for x in range(28)],#[x*(1+0.1*x)*20+500 for x in range(40)], #[x*(1+0.16*x)*50+500 for x in range(20)],
#      "min" : 750.,
#      "max" : 4250.,
#      "log" : True,
#    },
#    "X_tmass": {
#      "title" : "m_{Vh}^{T} (GeV)",
#      "nbins" : 35,
#      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
#      #"bins" : [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 2500, 3000, 3500, 4500],
#      "bins" : [x*(1+0.30*x)*50+800 for x in range(16)],
#      "min" : 750.,
#      "max" : 4250.,
#      "log" : True,
#    },
#    "X_cmass": {
#      "title" : "m_{Vh}^{T} (GeV)",
#      "nbins" : 35,
#      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
#      #"bins" : [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 2500, 3000, 3500, 4500],
#      "bins" : [x*(1+0.30*x)*50+800 for x in range(16)],
#      "min" : 750.,
#      "max" : 4250.,
#      "log" : True,
#    },
#    "X_kmass": {
#      "title" : "m_{Vh} with kinematic fit (GeV)",
#      "nbins" : 90,
#      "min" : 500.,
#      "max" : 5000.,
#      "log" : True,
#    },
#    "X_charge": {
#      "title" : "X candidate charge",
#      "nbins" : 20,
#      "min" : -10,
#      "max" : 10,
#      "log" : False,
#    },
#    "X_dR": {
#      "title" : "#Delta R (V-jet)",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 5,
#      "log" : False,
#    },
#    "X_dEta": {
#      "title" : "#Delta #eta (V-jet)",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 5,
#      "log" : False,
#    },
#    "X_dPhi": {
#      "title" : "#Delta #varphi (V-jet)",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 3.14,
#      "log" : False,
#    },
#    
#    "transverseMass(fatjet1_pt,fatjet1_phi,MEt.pt,MEt.phi)": {
#      "title" : "m_{Vh}^{T} (GeV)",
#      "nbins" : -1,
#      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
#      #"bins" : [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 2500, 3000, 3500, 4500],
#      "bins" : [x*(1+0.5*x)*50+500 for x in range(13)],#[x*(1+0.30*x)*50+500 for x in range(15)],
#      "min" : 500.,
#      "max" : 4500.,
#      "log" : True,
#    },
#    "invariantMass(jet1_pt,jet1_eta,jet1_phi,jet1_mass,jet2_pt,jet2_eta,jet2_phi,jet2_mass)": {
#      "title" : "m_{Vh} (GeV)",
#      "nbins" : 100,
#      "min" : 0.,
#      "max" : 250.,
#      "log" : True,
#    },
#    "invariantDoubleMass(Z_pt,Z_eta,Z_phi,jet1_pt,jet1_eta,jet1_phi,jet2_pt,jet2_eta,jet2_phi)": {
#      "title" : "m_{Vh} (GeV)",
#      "nbins" : 45,
#      "min" : 200.,
#      "max" : 2000.,
#      "log" : True,
#    },
#    "W(lepton1_pt,lepton1_eta,lepton1_phi,lepton1_mass,MEt.pt,MEt.phi)": {
#      "title" : "m_{Vh} (GeV)",
#      "nbins" : 500,
#      "min" : 0.,
#      "max" : 500.,
#      "log" : True,
#    },
#    "XWh(lepton1_pt,lepton1_eta,lepton1_phi,MEt.pt,MEt.phi,fatjet1_pt,fatjet1_eta,fatjet1_phi,fatjet1_mass)": {
#      "title" : "m_{Vh} (GeV)",
#      "nbins" : 21,
#      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
#      #"bins" : [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 2500, 3000, 3500, 4500],
#      "bins" : [x*(1+0.5*x)*50+700 for x in range(13)],#[x*(1+0.30*x)*50+500 for x in range(15)],
#      "min" : 800.,
#      "max" : 5000.,
#      "log" : True,
#    },
#    "deltaPhi(lepton1_phi,MEt.phi)": {
#      "title" : "#Delta #varphi (l-#slash{E}_{T})",
#      "nbins" : 50,
#      "min" : -3.14,
#      "max" : 3.14,
#      "log" : False,
#    },
#    "sqrt((lepton1_eta-fatjet1_eta)**2+deltaPhi(lepton1_phi,fatjet1_phi)**2)": {
#      "title" : "#Delta #varphi (l-#slash{E}_{T})",
#      "nbins" : 50,
#      "min" : 0,
#      "max" : 5,
#      "log" : False,
#    },
#    
#    # Dummy
#    "0*run": {
#      "title" : "",
#      "nbins" : 1,
#      "bins" : [],
#      "min" : -0.5,
#      "max" : 0.5,
#      "log" : False,
#    },
#    "0*run+0": {
#      "title" : "",
#      "nbins" : 4,
#      "bins" : [],
#      "min" : -0.5,
#      "max" : 3.5,
#      "log" : False,
#    },
#    "0*run+1": {
#      "title" : "",
#      "nbins" : 4,
#      "bins" : [],
#      "min" : -0.5,
#      "max" : 3.5,
#      "log" : False,
#    },
#    "0*run+2": {
#      "title" : "",
#      "nbins" : 4,
#      "bins" : [],
#      "min" : -0.5,
#      "max" : 3.5,
#      "log" : False,
#    },
#    "0*run+3": {
#      "title" : "",
#      "nbins" : 4,
#      "bins" : [],
#      "min" : -0.5,
#      "max" : 3.5,
#      "log" : False,
#    },
#    "0==0": {
#      "title" : "",
#      "nbins" : 5,
#      "min" : 0,
#      "max" : 5,
#      "log" : True,
#    },
}


for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(1, 5):
            ni = n.replace('[N]', "%d" % i)
            variable[ni] = v.copy()
            variable[ni]['title'] = variable[ni]['title'].replace('[N]', "%d" % i)
    elif n.startswith('H.'):
        variable[n] = v
        variable[n.replace('H.', 'HMerged.')] = v.copy()
        variable[n.replace('H.', 'HResolved.')] = v.copy()
        variable[n.replace('H.', 'HResolvedHpt.')] = v.copy()
    elif n.startswith('X.'):
        variable[n] = v
        variable[n.replace('X.', 'XMerged.')] = v.copy()
        variable[n.replace('X.', 'XResolved.')] = v.copy()
        variable[n.replace('X.', 'XResolvedHpt.')] = v.copy()
    else:
        variable[n] = v

# Custom settings
#variable['jet2_pt']['max'] = 400
#variable['jet3_pt']['max'] = 200
#variable['jet4_pt']['max'] = 200
#variable['lepton2_pt']['max'] = 250
