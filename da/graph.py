import networkx as nx
import nltk

from measure.utils import stack



# TODO: define grammar
rule_id = dict()
for id, r in enumerate(gm.productions()):
    rule_id[r] = f'r{id}'


# def generate_DAG_from_grammar(grammar: str):
#     """
#     Generate a DAG given a set of grammar in str
#     The grammar should be in the form of
#     \"""
#     A -> xxx
#     B -> yyy
#     \"""
#     where rules are divided by '\n'
#     """
#     gm = set(grammar.split('\n'))
#     gm.remove('')
#
#     G = nx.DiGraph()
#     G.add_nodes_from(gm)
#
#     edges = [(rule_b, rule_a) for rule_a in gm for rule_b in gm if a_generate_b(rule_a, rule_b)]
#     G.add_edges_from(edges)
#
#     return G
#
#
# def a_generate_b(a: str, b: str):
#     """
#     check whether a could generate b.
#     """
#     a_productions = a.split()[2:]
#     b_head = b.split()[0]
#     return (b_head in a_productions)


def generate_DAG_from_parse_tree(t: nltk.Tree) -> nx.DiGraph:
    """
    The function convert a parse tree into a graph comprising the concerned grammar rules
    :param t: nltk parse Tree
    :return: a DAG converted from the given parse tree
    """
    G = nx.DiGraph()
    rules = t.productions()
    node_to_add_edge = stack()
    for id, r in enumerate(rules):
        G.add_node(id, rule = rule_id[r])
        if r.is_nonlexical():
            if id != 0:
                G.add_edge(id, node_to_add_edge.pop())
            n_edges_to_add = len(r.rhs())
            for _ in range(n_edges_to_add):
                node_to_add_edge.push(id)
        if r.is_lexical():
            # find the id to connect with
            G.add_edge(id, node_to_add_edge.pop())
    # check all the necessary edges are added
    assert node_to_add_edge.is_empty()
    # check the DAG is correctly generated
    assert nx.is_directed_acyclic_graph(G)
    assert nx.is_connected(G)

    return G