met_range = (0,2000, True)


# title,    scale,  rebin, usrrng
settings = {
    'h_htcheck':('', 1,1, (0,2000)),
#    'h_htbprimemass':('', None, None, None),
    'h_ht_presel'           : ('H_{T} (GeV)', 10, 5, (1200,2000)),
    'h_ht'                  : ('H_{T} (GeV)', 10, 5, (1200,2000)),
    'h_ht_antib'            : ('H_{T} (GeV)', 10, 5, (1200,2000)),
    'h_ht_santib'           : ('H_{T} (GeV)', 10, 5, (1200,2000)),
    'h_ht_sb'               : ('H_{T} (GeV)', 10, 5, (1200,2000)),

#    'h_bprimemass_b'        : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemass_c'        : ('Mass (GeV)', 10, 2, None),
#    'h_bprimemass_d'        : ('Mass (GeV)', 10, 2, None),

#    'h_ht_closure'          : ('H_{T} (GeV)', 10, 10, None),
#    'h_ht_antib_closure'    : ('H_{T} (GeV)', 10, 10, None),
#    'h_ht_santib_closure'   : ('H_{T} (GeV)', 10, 10, None),
#    'h_ht_sb_closure'       : ('H_{T} (GeV)', 10, 10, None),

    'h_bprimemassbbreg1'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemassbbreg2'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemassbbregm1'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemassnobbreg1'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemassnobbreg2'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemassnobbregm1'          : ('Mass (GeV)', 10, 2, None),

    'h_bprimemass'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemass_b'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemass_c'          : ('Mass (GeV)', 10, 2, None),
    'h_bprimemass_d'          : ('Mass (GeV)', 10, 2, None),

    'h_genfwqpt'            : ('p_{T} (GeV)', 10, 4, None),
    'h_genfwqeta'           : ('#eta', 10, 5, None),
    'h_genfwqphi'            : ('#phi', 10, 7, None),

    'h_jetpt'               : ('p_{T} (GeV)', 10, 4, None),
    'h_jeteta'              : ('#eta', 10, 5, None),
    'h_jetphi'              : ('#phi', 10, 7, None),
    'h_njet'                : ('AK4 jets multiplicity', 10, None, None),
    
    'h_bjetpt'              : ('p_{T} (GeV)', 10, 4, None),
    'h_bjeteta'             : ('#eta', 10, 5, None),
    'h_bjetphi'             : ('#phi', 10, 7, None),
    'h_nbjet'               : ('CVSM AK4 jets multiplicity', 10, None, None),

    'h_nqcjet'              : ('forward jets multiplicity', 10, None, None),
    'h_qcjetpt'            : ('p_{T} (GeV)', 10, 4, None),
    'h_qcjeteta'           : ('#eta', 10, 5, None),

#    'h_deltaRb1'            : ("#DeltaR(reco b, gen b)", 10, 10, None),
#    'h_deltaRb2'            : ("#DeltaR(reco b, gen b)", 10, 10, None),
#    'h_matching'            : ("", 10, None, None),
    'h_fatjetdoubleB'       : ('Double b-tag', 10, 1, None),
    'h_fatjetpt'            : ('p_{T} (GeV)', 10, 4, None),
    'h_fatjeteta'           : ('#eta', 10, 5, None),
    'h_fatjetphi'           : ('#phi', 10, 7, None),
    'h_nfatjet'             : ('AK8 jets multiplicity', 10, None, None),
    'h_fatjetncsvmsubjets'  : ('CSVM subjets multiplicity', 10, None, None),
    'h_fatjetprunedmass'    : ('pruned mass (GeV)', 10, None, None),
    'h_fatjetnsubjetiness'  : ('#tau_{2}/#tau_{1}', 10, None, None),
    'h_fatjetleadpt'        : ('Leading AK8 jet p_{T} (GeV)', 10, 4, None),
    'h_fatjetsubleadpt'     : ('Sub-leading AK8 jet p_{T} (GeV)', 10, 4, None),

    'h_higgspt'             : ('p_{T} (GeV)', 10, 4, None),
    'h_higgseta'            : ('#eta', 10, 5, None),
    'h_higgsphi'            : ('#phi', 10, 7, None),
    'h_nhiggsjet'           : ('Higgs-tagged jets multiplicity', 10, None, None),

    'h_cutFlow'             : ('', 10, None, None),
}


store = [
    'h_htcheck',
 #   'h_htbprimemass',
    'h_cutFlow',
    'h_ht_presel',
    'h_ht',
    'h_ht_antib',
    'h_ht_santib',
    'h_ht_sb',
    'h_ht_closure',
    'h_ht_antib_closure',
    'h_ht_santib_closure',
    'h_ht_sb_closure',
    'h_bprimemass',
    'h_bprimemass_b',
    'h_bprimemass_c',
    'h_bprimemass_d',
#    'met_preS',
#    'metFinal',
#    'metFinal_tag',
#    'metFinal_untag',
#    "metFinal_Angular",
#    "metFinal_Angular_tag",
#    "metFinal_Angular_untag",
]
