"""
Transduction rules.

src_to_target_grammar: 
The (English to Japanese) tranduction rules to be coupled with the extended English source grammar.
"""


src_to_target_grammar = {
    "S -> NPQ VP":"S -> NPQ が VP か", 
    "S -> NPQ was NominalSub":"S -> NominalSub は NPQ でしたか", # Q
    "S -> NPQ did NPVMod":"S -> NPVMod のは NPQ ですか", # what did A write and B edit? -> A ga kaite, B ga hennshushita no ha nann deshitaka
    "S -> was NominalSub Vobl":"S -> NominalSub は Vobl か",
    "S -> NPQ Vobl":"S -> NPQ が Vobl か", # same Q
    "S -> was NominalSub Adj":"S -> NominalSub は Adj でしたか",
    "S -> was NominalSub Nominal":"S -> NominalSub は Nominal でしたか",
    "S -> did NominalSub VP":"S -> NominalSub は VP か",

    # TODO: Chain rules to add for VMod and VPrepOrgMod
    "NPVMod -> Nominal VMod":"NPVMod -> Nominal が VMod",
    # todo: this rule basically follows VP, VPrepOrg finally derives as V
    "NPVMod -> Nominal VPrepOrgMod":"NPVMod -> Nominal を VPrepOrgMod", # VPrepOrg: passive in EN, active in JP 
    "NPVT -> Nominal VT":"NPVT -> Nominal が VT",
    "NPVT -> Nominal VPrepOrgT":"NPVT -> Nominal を VPrepOrgT",

    "VP -> V Nominal":"VP -> Nominal を V", # have lunch -> hirugohan wo taberu
    "VP -> was Vobl":"VP -> Vobl", # was done by him -> kare ni sareta
    "VPT -> VT Nominal":"VPT -> Nominal を VT",
    "VPT -> was VoblT":"VPT -> VoblT",
    "VPMod -> VMod Nominal":"VPMod -> Nominal を VMod",
    "VPMod -> was VoblMod":"VPMod -> VoblMod",

    "VPrep -> was VPrep":"VPrep -> VPrep",
    "VPrep -> Vsr by":"VPrep -> Vsr",
    "VPrepT -> was VPrepT":"VPrepT -> VPrepT",
    "VPrepT -> VsrT by":"VPrepT -> VsrT",
    "VPrepMod -> was VPrepMod":"VPrepMod -> VPrepMod",
    "VPrepMod -> VsrMod by":"VPrepMod -> VsrMod",
 
    "VPrepOrgMod -> was VPrepOrgMod":"VPrepOrgMod -> VPrepOrgMod",
    "VPrepOrgMod -> VPassOrgMod by":"VPrepOrgMod -> VPassOrgMod",
    "VPrepOrgT -> was VPrepOrgT":"VPrepOrgT -> VPrepOrgT",
    "VPrepOrgT -> VPassOrgT by":"VPrepOrgT -> VPassOrgT",

    "Vobl -> VPrep Nominal":"Vobl -> Nominal に VPrep", # done by nominal -> nominal ni sareta
    "VoblT -> VPrepT Nominal":"VoblT -> Nominal に VPrepT",
    "VoblMod -> VPrepMod Nominal":"VoblMod -> Nominal に VPrepMod",
    
    # "NPQ -> WhW Nominal":"NPQ -> WhW Nominal", # which city -> dono machi
    # TODO: caseO -> of ... : caseO ... no
    "NPQ -> WhW role caseO":"NPQ -> caseO WhW role", # which character of Alice -> alisu no dono kyarakuta

    "commonNoun -> commonNoun RC":"commonNoun -> RC commonNoun", # people whose role was... -> yaku ga... hito
    "WhWcommonNoun -> WhWcommonNoun RC":"WhWcommonNoun -> RC WhWcommonNoun",
    "detSubcommonNoun -> detSubcommonNoun RC":"detSubcommonNoun -> RC detSubcommonNoun",

    # "RC -> VoblMod":"RC -> VoblMod", # people attacked by... -> ...ni kougekisareta hito 
    "RC -> R VPMod":"RC -> VPMod", # people that eat... -> ...wo taberu hito
    "RC -> R NPVMod":"RC -> NPVMod", # people that you like -> anata ga sukina hito
    "RC -> whose role VPMod":"RC -> role が VPMod", # todo: role GA -> ...

    # "VP -> VPT andVP":"VP -> VPT andVP",
    # "VP -> VPx andVP":"VP -> VPx andVP",
    # "VPx -> VPT punctVPT":"VPx -> VPT punctVPT",
    # "VPx -> VPx punctVPT":"VPx -> VPx punctVPT",
    # "andVP -> conj VP":"andVP -> conj VP",
    "andVP -> punct conj VP":"andVP -> conj VP",
    # "punctVPT -> punct VPT":"punctVPT -> punct VPT",

    # VPMod -> VPT andVPMod
    # VPMod -> VPx andVPMod
    # VPx -> VPT punctVPT 
    # VPx -> VPx punctVPT 
    # andVPMod -> conj VPMod
    "andVPMod -> punct conj VPMod":"andVPMod -> conj VPMod",
    # punctVPT -> punct VPT

    # Vobl -> VoblT andVobl
    # Vobl -> Voblx andVobl 
    # Voblx -> VoblT punctVoblT 
    # Voblx -> Voblx punctVoblT 
    # andVobl -> conj Vobl 
    "andVobl -> punct conj Vobl":"andVobl -> conj Vobl",
    # punctVoblT -> punct VoblT

    # VoblMod -> VoblT andVoblMod
    # VoblMod -> Voblx andVoblMod 
    # Voblx -> VoblT punctVoblT 
    # Voblx -> Voblx punctVoblT 
    # andVoblMod -> conj VoblMod 
    "andVoblMod -> punct conj VoblMod":"andVoblMod -> conj VoblMod",
    # punctVoblT -> punct VoblT

    # VPrep -> VPrepT andVPrep 
    # VPrep -> VPrepX andVPrep 
    # VPrepX -> VPrepT punctVPrepT 
    # VPrepX -> VPrepX punctVPrepT 
    # andVPrep -> conj VPrep 
    "andVPrep -> punct conj VPrep":"andVPrep -> conj VPrep",
    # punctVPrepT -> punct VPrepT

    # VPrepMod -> VPrepT andVPrepMod 
    # VPrepMod -> VPrepX andVPrepMod 
    # VPrepX -> VPrepT punctVPrepT 
    # VPrepX -> VPrepX punctVPrepT 
    # andVPrepMod -> conj VPrepMod 
    "andVPrepMod -> punct conj VPrepMod":"andVPrepMod -> conj VPrepMod",
    # punctVPrepT -> punct VPrepT

    # VPrepOrgMod -> VPrepOrgT andVPrepOrgMod 
    # VPrepOrgMod -> VPrepOrgX andVPrepOrgMod 
    # VPrepOrgX -> VPrepOrgT punctVPrepOrgT 
    # VPrepOrgX -> VPrepOrgX punctVPrepOrgT 
    # andVPrepOrgMod -> conj VPrepOrgMod 
    "andVPrepOrgMod -> punct conj VPrepOrgMod":"andVPrepOrgMod -> conj VPrepOrgMod", 
    # punctVPrepOrgT -> punct VPrepOrgT

    # V -> VT andV
    # V -> Vx andV
    # Vx -> VT punctVT
    # Vx -> Vx punctVT 
    # andV -> conj V
    "andV -> punct conj V":"andV -> conj V", 
    # punctVT -> punct VT

    # VT -> VT andVT
    # VT -> Vx andVT
    # Vx -> VT punctVT
    # Vx -> Vx punctVT 
    # andVT -> conj VT
    "andVT -> punct conj VT":"andVT -> conj VT", 
    # punctVT -> punct VT

    # VMod -> VT andVMod
    # VMod -> Vx andVMod
    # andVMod -> conj VMod
    "andVMod -> punct conj VMod":"andVMod -> conj VMod",

    # Vsr -> VsrT andVsr
    # Vsr -> Vsrx andVsr
    # Vsrx -> VsrT punctVsrT
    # Vsrx -> Vsrx punctVsrT 
    # andVsr -> conj Vsr
    "andVsr -> punct conj Vsr":"andVsr -> conj Vsr",
    # punctVsrT -> punct VsrT

    # VsrT -> VsrT andVsrT
    # VsrT -> Vsrx andVsrT
    # andVsrT -> conj VsrT
    "andVsrT -> punct conj VsrT":"andVsrT -> conj VsrT", 
    # punctVsrT -> punct VsrT

    # VsrMod -> VsrT andVsrMod
    # VsrMod -> Vsrx andVsrMod
    # andVsrMod -> conj VsrMod
    "andVsrMod -> punct conj VsrMod":"andVsrMod -> conj VsrMod",

    # Vx -> Vx punctVPrepT
    # Vx -> VT punctVPrepT
    # V -> Vx andVPrep
    # V -> VT andVPrep
    # VPrep -> VPrepT andV
    # VPrep -> VPrepX andV 
    # VPrepX -> VPrepT punctVT 
    # VPrepX -> VPrepX punctVT


    # VPrepOrgMod -> VPrepOrgT andVOrgPassMod
    # VPrepOrgMod -> VPrepOrgX andVOrgPassMod
    # VPrepOrgX -> VPrepOrgT punctVOrgPassT
    # VPrepOrgX -> VPrepOrgX punctVOrgPassT

    # punctVOrgPassT -> punct VOrgPassT
    # andVOrgPassMod -> conj VOrgPassMod
    "andVOrgPassMod -> punct conj VOrgPassMod":"andVOrgPassMod -> conj VOrgPassMod",


    # VPassOrgMod -> VPassOrgT andVPassOrgMod
    # VPassOrgMod -> VPassOrgx andVPassOrgMod
    # VPassOrgx -> VPassOrgT punctVPassOrgT
    # VPassOrgx -> VPassOrgx punctVPassOrgT 
    # andVPassOrgMod -> conj VPassOrgMod
    "andVPassOrgMod -> punct conj VPassOrgMod":"andVPassOrgMod -> conj VPassOrgMod", 
    # punctVPassOrgT -> punct VPassOrgT


    # VMod -> Vx andVPrepMod
    # VMod -> VT andVPrepMod
    # VPrepMod -> VPrepT andVMod
    # VPrepMod -> VPrepX andVMod

    # NPVMod -> NPVT andNPVMod
    # NPVMod -> NPVx andNPVMod 
    # NPVx -> NPVT punctNPVT
    # NPVx -> NPVx punctNPVT 
    # andNPVMod -> conj NPVMod 
    "andNPVMod -> punct conj NPVMod":"andNPVMod -> conj NPVMod", 
    # punctNPVT -> punct NPVT

    # V -> F V
    # VT -> F VT
    # VMod -> F VMod
    # Vsr -> F Vsr
    # VsrT -> F VsrT
    # VsrMod -> F VsrMod
    # VPassOrgMod -> F VPassOrgMod
    # VPassOrgT -> F VPassOrgT
    # VOrgPassT -> F VOrgPassT
    # VOrgPassMod -> F VOrgPassMod


    # Nominal -> Name 
    # Nominal -> DP
    # Nominal -> commonNoun

    # NominalSub -> Name
    # NominalSub -> DPSub
    # NominalSub -> commonNoun


    "DP -> det role caseO":"DP -> caseO role",
    "DPSub -> detSub role caseO":"DPSub -> caseO detSub role",
# of -> no
    "caseO -> of DP":"caseO -> DP of",
    "caseO -> of Name":"caseO -> Name of",

    # DP -> det commonNoun
    # DPSub -> detSub commonNoun

    # Name -> Name andName 
    # Name -> Namex andName 
    # Namex -> Name punctName 
    # Namex -> Namex punctName 
    # andName -> conjN Name 
    "andName -> punctN conjN Name":"andName -> conjN Name",
    # punctName -> punctN Name

    # commonNoun -> commonNoun andCommonNoun
    # commonNoun -> commonNounx andCommonNoun
    # commonNounx -> commonNoun punctCommonNoun
    # commonNounx -> commonNounx punctCommonNoun
    # andCommonNoun -> conjN commonNoun 
    "andCommonNoun -> punctN conjN commonNoun":"andCommonNoun -> conjN commonNoun",
    # punctCommonNoun -> punctN commonNoun

    # role -> role androle
    # role -> rolex androle 
    # rolex -> role punctrole 
    # rolex -> rolex punctrole 
    # androle -> conjN role 
    "androle -> punctN conjN role":"androle -> conjN role",
    # punctrole -> punctN role

    # commonNoun -> F commonNoun 
    # role -> F role
    # role -> Cnt of nat
    # commonNoun -> P commonNoun

    "role -> Cnt of nat":"role -> nat Cnt" # country of nationality -> 国籍国
    
    # commonNoun -> AdjNa commonNoun 
    # role -> AdjNa role
}