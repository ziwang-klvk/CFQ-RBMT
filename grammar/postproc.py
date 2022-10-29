"""
Methods and variables for textual post processing.
"""



# The post processing based on pattern replacement
pattern_pairs = {'を結婚し':'と結婚し','を影響し':'に影響し'}



# The preferred patterns to assign priority during post processing
pref_pattern = [{"S -> was NominalSub Vobl","commonNoun -> F commonNounHead"},
                {"S -> was NominalSub Vobl","commonNounHead -> F commonNounHead"},
                {"caseS -> Name pS"},
                {"NPQ -> WhWNominal"}
                ]


class post_processing:

    def __init__(self, pattern_pairs = pattern_pairs) -> None:
        self.pattern_pairs = pattern_pairs

    def replace(self, sens):
        new_sens = []
        for sen in sens:
            for org, tar in self.pattern_pairs.items():
                sen = sen.replace(org, tar)
            new_sens.append(sen)
        return new_sens


