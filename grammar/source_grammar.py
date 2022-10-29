"""
Grammar for CFQ.

EN_source_transduction_grammar: 
The extended version to be coupled with the (Japanese) tranduction rules.

EN_source_original_grammar: 
The grammar provided by the paper "Compositional Generalization in Dependency Parsing" url:https://arxiv.org/pdf/2110.06843.pdf.
"""






EN_source_transduction_grammar =  """S -> NPQ VP 
S -> NPQ was NominalSub 
S -> NPQ did NPVMod 
S -> was NominalSub Vobl 
S -> NPQ Vobl 
S -> was NominalSub Adj 
S -> was NominalSub Nominal 
S -> did NominalSub VP 

NPVMod -> Nominal VMod
NPVMod -> Nominal VPrepOrgMod
NPVT -> Nominal VT
NPVT -> Nominal VPrepOrgT

VP -> V Nominal
VP -> was Vobl
VPT -> VT Nominal
VPT -> was VoblT 
VPMod -> VMod Nominal
VPMod -> was VoblMod

VPrep -> was VPrep
VPrep -> Vsr by
VPrepT -> was VPrepT
VPrepT -> VsrT by
VPrepMod -> was VPrepMod
VPrepMod -> VsrMod by

VPrepOrgMod -> was VPrepOrgMod
VPrepOrgMod -> VPassOrgMod by
VPrepOrgT -> was VPrepOrgT
VPrepOrgT -> VPassOrgT by

Vobl -> VPrep Nominal
VoblT -> VPrepT Nominal 
VoblMod -> VPrepMod Nominal

NPQ -> WhWNominal 
NPQ -> WhW role caseO

commonNoun -> commonNoun RC
WhWcommonNoun -> WhWcommonNoun RC
detSubcommonNoun -> detSubcommonNoun RC

WhWcommonNoun -> WhW commonNounModHead

RC -> VoblMod
RC -> R VPMod
RC -> R NPVMod
RC -> whose role VPMod

VP -> VPT andVP
VP -> VPx andVP
VPx -> VPT punctVPT 
VPx -> VPx punctVPT 
andVP -> conj VP 
andVP -> punct conj VP
punctVPT -> punct VPT

VPMod -> VPT andVPMod
VPMod -> VPx andVPMod
VPx -> VPT punctVPT 
VPx -> VPx punctVPT 
andVPMod -> conj VPMod
andVPMod -> punct conj VPMod
punctVPT -> punct VPT

Vobl -> VoblT andVobl
Vobl -> Voblx andVobl 
Voblx -> VoblT punctVoblT 
Voblx -> Voblx punctVoblT 
andVobl -> conj Vobl 
andVobl -> punct conj Vobl
punctVoblT -> punct VoblT

VoblMod -> VoblT andVoblMod
VoblMod -> Voblx andVoblMod 
Voblx -> VoblT punctVoblT 
Voblx -> Voblx punctVoblT 
andVoblMod -> conj VoblMod 
andVoblMod -> punct conj VoblMod
punctVoblT -> punct VoblT

VPrep -> VPrepT andVPrep 
VPrep -> VPrepX andVPrep 
VPrepX -> VPrepT punctVPrepT 
VPrepX -> VPrepX punctVPrepT 
andVPrep -> conj VPrep 
andVPrep -> punct conj VPrep 
punctVPrepT -> punct VPrepT

VPrepMod -> VPrepT andVPrepMod 
VPrepMod -> VPrepX andVPrepMod 
VPrepX -> VPrepT punctVPrepT 
VPrepX -> VPrepX punctVPrepT 
andVPrepMod -> conj VPrepMod 
andVPrepMod -> punct conj VPrepMod 
punctVPrepT -> punct VPrepT

VPrepOrgMod -> VPrepOrgT andVPrepOrgMod 
VPrepOrgMod -> VPrepOrgX andVPrepOrgMod 
VPrepOrgX -> VPrepOrgT punctVPrepOrgT 
VPrepOrgX -> VPrepOrgX punctVPrepOrgT 
andVPrepOrgMod -> conj VPrepOrgMod 
andVPrepOrgMod -> punct conj VPrepOrgMod 
punctVPrepOrgT -> punct VPrepOrgT

V -> VT andV
V -> Vx andV
Vx -> VT punctVT
Vx -> Vx punctVT 
andV -> conj V
andV -> punct conj V 
punctVT -> punct VT

VT -> VT andVT
VT -> Vx andVT
Vx -> VT punctVT
Vx -> Vx punctVT 
andVT -> conj VT
andVT -> punct conj VT 
punctVT -> punct VT

VMod -> VT andVMod
VMod -> Vx andVMod
andVMod -> conj VMod
andVMod -> punct conj VMod

Vsr -> VsrT andVsr
Vsr -> Vsrx andVsr
Vsrx -> VsrT punctVsrT
Vsrx -> Vsrx punctVsrT 
andVsr -> conj Vsr
andVsr -> punct conj Vsr 
punctVsrT -> punct VsrT

VsrT -> VsrT andVsrT
VsrT -> Vsrx andVsrT
andVsrT -> conj VsrT
andVsrT -> punct conj VsrT 
punctVsrT -> punct VsrT

VsrMod -> VsrT andVsrMod
VsrMod -> Vsrx andVsrMod
andVsrMod -> conj VsrMod
andVsrMod -> punct conj VsrMod

Vx -> Vx punctVPrepT
Vx -> VT punctVPrepT
V -> Vx andVPrep
V -> VT andVPrep
VPrep -> VPrepT andV
VPrep -> VPrepX andV 
VPrepX -> VPrepT punctVT 
VPrepX -> VPrepX punctVT


VPrepOrgMod -> VPrepOrgT andVOrgPassMod
VPrepOrgMod -> VPrepOrgX andVOrgPassMod
VPrepOrgX -> VPrepOrgT punctVOrgPassT
VPrepOrgX -> VPrepOrgX punctVOrgPassT

punctVOrgPassT -> punct VOrgPassT
andVOrgPassMod -> conj VOrgPassMod
andVOrgPassMod -> punct conj VOrgPassMod


VPassOrgMod -> VPassOrgT andVPassOrgMod
VPassOrgMod -> VPassOrgx andVPassOrgMod
VPassOrgx -> VPassOrgT punctVPassOrgT
VPassOrgx -> VPassOrgx punctVPassOrgT 
andVPassOrgMod -> conj VPassOrgMod
andVPassOrgMod -> punct conj VPassOrgMod 
punctVPassOrgT -> punct VPassOrgT


VMod -> Vx andVPrepMod
VMod -> VT andVPrepMod
VPrepMod -> VPrepT andVMod
VPrepMod -> VPrepX andVMod

NPVMod -> NPVT andNPVMod
NPVMod -> NPVx andNPVMod 
NPVx -> NPVT punctNPVT
NPVx -> NPVx punctNPVT 
andNPVMod -> conj NPVMod 
andNPVMod -> punct conj NPVMod 
punctNPVT -> punct NPVT

V -> F V
VT -> F VT
VMod -> F VMod
Vsr -> F Vsr
VsrT -> F VsrT
VsrMod -> F VsrMod
VPassOrgMod -> F VPassOrgMod
VPassOrgT -> F VPassOrgT
VOrgPassT -> F VOrgPassT
VOrgPassMod -> F VOrgPassMod


Nominal -> Name 
Nominal -> DP
Nominal -> commonNoun
WhWNominal -> WhWcommonNoun

NominalSub -> Name
NominalSub -> DPSub
NominalSub -> commonNoun

DP -> caseS role
DPs -> caseS role
DPSub -> caseSSub role
DPSubs -> caseSSub role

caseS -> DPs pS 
caseS -> Name pS 
caseSSub -> DPSubs pS
caseSSub -> Name pS

DP -> det role caseO 
DPSub -> detSub role caseO

caseO -> of DP 
caseO -> of Name

DP -> det commonNoun
DPs -> det commonNounMod
DPs -> det commonNounHead
DPSub -> detSubcommonNoun
DPSubs -> detSubcommonNounModHead

detSubcommonNoun -> detSub commonNounMod
detSubcommonNoun -> detSub commonNounHead
detSubcommonNounModHead -> detSub commonNounModHead

commonNounModHead -> commonNounMod
commonNounModHead -> commonNounHead

Name -> Name andName 
Name -> Namex andName 
Namex -> Name punctName 
Namex -> Namex punctName 
andName -> conjN Name 
andName -> punctN conjN Name 
punctName -> punctN Name

commonNoun -> commonNoun andCommonNoun
commonNoun -> commonNounx andCommonNoun
commonNounx -> commonNoun punctCommonNoun
commonNounx -> commonNounx punctCommonNoun
andCommonNoun -> conjN commonNoun 
andCommonNoun -> punctN conjN commonNoun 
punctCommonNoun -> punctN commonNoun

role -> role androle
role -> rolex androle 
rolex -> role punctrole 
rolex -> rolex punctrole 
androle -> conjN role 
androle -> punctN conjN role
punctrole -> punctN role


commonNoun -> F commonNounHead 
commonNounHead -> F commonNounHead 
role -> F roleHead
role -> Cnt of nat
commonNoun -> P commonNounHead
commonNounHead -> P commonNounHead

commonNoun -> AdjNa commonNounHead
commonNoun -> AdjNa commonNounMod
commonNounMod -> AdjNa commonNounHead
commonNounMod -> AdjNa commonNounMod
role -> AdjNa roleHead
role -> AdjNa role







punct -> ","
punctN -> ","

Cnt -> 'country'
nat -> 'nationality'
P -> 'production'
F -> 'film' | 'art' | 'executive' | 'costume'

V -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VT -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
Vsr -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VsrT -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VMod -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VsrMod -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VPassOrgT -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VPassOrgMod -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VOrgPassT -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
VOrgPassMod -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'




Name -> 'M0' | 'M1' | 'M2' | 'M3' | 'M4' | 'M5' | 'M6' | 'M7' | 'M8' | 'M9'

commonNoun -> 'character' | 'person' | 'composer' | 'prequel' | 'director' | 'writer' | 'company' | 'actor' | 'designer' | 'founder' | 'sequel' | 'producer' | 'spouse' | 'child' | 'editor' | 'employer' | 'employee' | 'distributor' | 'sibling' | 'star' | 'parent' | 'cinematographer' | 'screenwriter' | 'film'
commonNounHead -> 'character' | 'person' | 'composer' | 'prequel' | 'director' | 'writer' | 'company' | 'actor' | 'designer' | 'founder' | 'sequel' | 'producer' | 'spouse' | 'child' | 'editor' | 'employer' | 'employee' | 'distributor' | 'sibling' | 'star' | 'parent' | 'cinematographer' | 'screenwriter' | 'film'

role -> 'character' | 'person' | 'composer' | 'prequel' | 'director' | 'writer' | 'company' | 'actor' | 'designer' | 'founder' | 'sequel' | 'producer' | 'spouse' | 'child' | 'editor' | 'employer' | 'employee' | 'distributor' | 'sibling' | 'star' | 'parent' | 'cinematographer' | 'screenwriter' | 'film'
roleHead -> 'character' | 'person' | 'composer' | 'prequel' | 'director' | 'writer' | 'company' | 'actor' | 'designer' | 'founder' | 'sequel' | 'producer' | 'spouse' | 'child' | 'editor' | 'employer' | 'employee' | 'distributor' | 'sibling' | 'star' | 'parent' | 'cinematographer' | 'screenwriter' | 'film'


NPQ -> 'who' | 'what' | 'Who' | 'What'
WhW -> 'What' | 'Which' | 'what' | 'which'
did -> 'did' | 'Did'

conj -> 'and'
conjN -> 'and'

pS -> "'s"
of -> 'of'

det -> 'a' | 'an'
detSub -> 'a' | 'an'

by -> 'by'
Adj -> 'female' | 'American' | 'French' | 'Italian' | 'male' | 'Swedish' | 'Canadian' | 'British' | 'Spanish' | 'Mexican' | 'Chinese' | 'German' | 'American' | 'Dutch' | 'Japanese'
AdjNa -> 'female' | 'American' | 'French' | 'Italian' | 'male' | 'Swedish' | 'Canadian' | 'British' | 'Spanish' | 'Mexican' | 'Chinese' | 'German' | 'American' | 'Dutch' | 'Japanese'
was -> 'was' | 'were' | 'Was' | 'Were'
R -> 'that'
whose -> 'whose'
"""



EN_source_original_grammar = """
S -> NPQ VP Qmark
S -> NPQ was Nominal Qmark
S -> NPQ did NPV Qmark
S -> was Nominal Vobl Qmark
S -> NPQ Vobl Qmark
S -> was Nominal Adj Qmark
S -> was Nominal Nominal Qmark 
S -> did Nominal VP Qmark
NPV -> Nominal V 
NPV -> Nominal VPrep
VP -> V Nominal 
VP -> was Vobl 
VPrep -> was VPrep 
VPrep -> V by


Vobl -> VPrep Nominal 
NPQ -> WhW Nominal 
NPQ -> WhW role caseO
commonNoun -> commonNoun RC
RC -> Vobl
RC -> R VP
RC -> R NPV
RC -> whose role VP
VP -> VP andVP
VP -> VPx andVP
VPx -> VP punctVP 
VPx -> VPx punctVP 
andVP -> conj VP 
andVP -> punct conj VP 
punctVP -> punct VP
Vobl -> Vobl andVobl
Vobl -> Voblx andVobl 
Voblx -> Vobl punctVobl 
Voblx -> Voblx punctVobl 
andVobl -> conj Vobl 
andVobl -> punct conj Vobl 
punctVobl -> punct Vobl
VPrep -> VPrep andVPrep 
VPrep -> VPrepX andVPrep 
VPrepX -> VPrep punctVPrep 
VPrepX -> VPrepX punctVPrep 
andVPrep -> conj VPrep 
andVPrep -> punct conj VPrep 
punctVPrep -> punct VPrep
V -> V andV
V -> Vx andV
Vx -> V punctV
Vx -> Vx punctV 
andV -> conj V
andV -> punct conj 
V punctV -> punct V
Vx -> Vx punctVPrep
Vx -> V punctVPrep
V -> Vx andVPrep
V -> V andVPrep
VPrep -> VPrep andV 
VPrep -> VPrepX andV 
VPrepX -> VPrep punctV 
VPrepX -> VPrepX punctV



NPV -> NPV andNPV 
NPV -> NPVx andNPV 
NPVx -> NPV punctNPV 
NPVx -> NPVx punctNPV 
andNPV -> conj NPV 
andNPV -> punct conj NPV 
punctNPV -> punct NPV
V->FV
Nominal -> Name 
Nominal -> DP
Nominal -> commonNoun
DP -> caseS role 
caseS -> DP pS 
caseS -> Name pS 
DP -> det role caseO 
caseO -> of DP 
caseO -> of Name
DP -> det commonNoun
Name -> Name andName 
Name -> Namex andName 
Namex -> Name punctName 
Namex -> Namex punctName 
andName -> conj Name 
andName -> punct conj Name 
punctName -> punct Name
commonNoun -> commonNoun andCommonNoun
commonNoun -> commonNounx andCommonNoun
commonNounx -> commonNoun punctCommonNoun
commonNounx -> commonNounx punctCom- monNoun
andCommonNoun -> conj commonNoun 
andCommonNoun -> punct conj commonNoun 
punctCommonNoun -> punct commonNoun
role -> role androle
role -> rolex androle 
rolex -> role punctrole 
rolex -> rolex punctrole 
androle -> conj role 
androle -> punct conj role

punctrole -> punct role
commonNoun -> F commonNoun 
role -> F role
role -> Cnt of nat
commonNoun -> P commonNoun
commonNoun -> Adj commonNoun 
role -> Adj role

punct -> ","
Cnt -> 'country'
nat -> 'nationality'
P -> 'production'
F -> 'film' | 'art' | 'executive' | 'costume'
V -> 'direct' | 'produce' | 'edit' | 'married' | 'produced' | 'starred' | 'employ' | 'written' | 'edited' | 'marry' | 'distribute' | 'played' | 'influenced' | 'employed' | 'acquire' | 'acquired' | 'produce' | 'directed' | 'wrote' | 'influence' | 'found' | 'play' | 'star' | 'founded' | 'write' | 'direct' | 'distributed'
Name -> 'M0' | 'M1' | 'M2' | 'M3' | 'M4' | 'M5' | 'M6' | 'M7' | 'M8' | 'M9'
commonNoun -> 'character' | 'person' | 'composer' | 'prequel' | 'director' | 'writer' | 'company' | 'actor' | 'designer' | 'founder' | 'sequel' | 'producer' | 'spouse' | 'child' | 'editor' | 'employer' | 'employee' | 'distributor' | 'sibling' | 'star' | 'parent' | 'cinematographer' | 'screenwriter' | 'film'
role -> 'character' | 'person' | 'composer' | 'prequel' | 'director' | 'writer' | 'company' | 'actor' | 'designer' | 'founder' | 'sequel' | 'producer' | 'spouse' | 'child' | 'editor' | 'employer' | 'employee' | 'distributor' | 'sibling' | 'star' | 'parent' | 'cinematographer' | 'screenwriter' | 'film'
NPQ -> 'who' | 'what' | 'Who' | 'What'
WhW -> 'What' | 'Which' | 'what' | 'which'
did -> 'did' | 'Did'
conj -> 'and'
pS -> "'s"
of -> 'of'
det -> 'a' | 'an'
by -> 'by'
Adj -> 'female' | 'American' | 'French' | 'Italian' | 'male' | 'Swedish' | 'Canadian' | 'British' | 'Spanish' | 'Mexican' | 'Chinese' | 'German' | 'American' | 'Dutch' | 'Japanese'
was -> 'was' | 'were' | 'Was' | 'Were'
R -> 'that'
whose -> 'whose'
"""