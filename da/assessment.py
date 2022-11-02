import nltk
from nltk import CFG, ChartParser
from tqdm import tqdm

from typing import List
from dbca.datasets.relational import RelationalSample
from dbca.dbca_splitter import DBCASplitter, DBCASplitterConfig
from dbca.sample import Sample

from da.graph import generate_DAG_from_parse_tree


class AssessConfig:
    max_compounds: int = 10000
    max_compound_nodes: int = 3
    max_compound_branch: int = 2


class GrammarDBCAssessor:
    def __init__(self,
                 grammar: nltk.CFG or str,
                 train_text: List[str],
                 test_text: List[str],
                 assess_config: AssessConfig = None):

        # configuration
        self.assess_config = assess_config if assess_config else AssessConfig()
        # Disregard the rest of splitter configuration since they do not affect assessment
        self.DBCAConfig = DBCASplitterConfig(max_compounds=self.assess_config.max_compounds)

        print('------initializing------')

        if type(grammar) == str:
            grammar = CFG.fromstring(grammar)
        self.grammar = grammar
        self.rule_id = self.__gen_rule_id()
        self.parser = ChartParser(grammar=self.grammar)
        self.train_samples = self.__parse_and_gen_samples(train_text, 'train')
        self.test_samples = self.__parse_and_gen_samples(test_text, 'test')

        self.atom_diver, self.comp_diver, self.splitter = DBCASplitter.measure_sample_sets(self.train_samples,
                                                                                           self.test_samples,
                                                                                           self.DBCAConfig)

    def __parse_and_gen_samples(self, text, spl=None):
        print(f'Generating {spl} Samples...')
        samples = []
        for line in tqdm(text):
            trees = self.parser.parse(line.split())
            trees = [tree for tree in trees]
            # choose the first parse tree
            parse_tree = trees[0]
            DAG = generate_DAG_from_parse_tree(parse_tree, rule_id=self.rule_id)
            sample = RelationalSample(graph=DAG,
                                      c_max_n_nodes=self.assess_config.max_compound_nodes,
                                      c_max_n_branch=self.assess_config.max_compound_branch)
            samples.append(sample)
        return samples

    def __gen_rule_id(self):
        rule_id = dict()
        for id, r in enumerate(self.grammar.productions()):
            rule_id[r] = f'r{id}'
        return rule_id
