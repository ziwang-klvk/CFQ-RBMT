import networkx as nx

def generate_DAG_from_grammar(grammar: str):
    """
    Generate a DAG given a set of grammar in str
    The grammar should be in the form of
    \"""
    A -> xxx
    B -> yyy
    \"""
    where rules are divided by '\n'
    """
    gm = set(grammar.split('\n'))
    gm.remove('')

    G = nx.DiGraph()
    G.add_nodes_from(gm)

    edges = [(rule_b, rule_a) for rule_a in gm for rule_b in gm if a_generate_b(rule_a, rule_b)]
    G.add_edges_from(edges)

    return G


def a_generate_b(a: str, b: str):
    """
    check whether a could generate b.
    """
    a_productions = a.split()[2:]
    b_head = b.split()[0]
    return (b_head in a_productions)

