# Matthew Henderson, 2010.12.30 (Chandler's Ford)

from networkx import graph_clique_number, complement

from test_functions import has_colour

def to_colouring(assignment):
    """Change a mapping of vertices to colours into a mapping of colours
    to vertices."""
    def f(y):
        return [x for x in assignment.keys() if assignment[x]==y]
    P = list(set(assignment.values()))
    Q = dict(zip(assignment.keys(), map(f, assignment)))
    R = {}
    for q in Q:
        if len(Q[q])>0:
            R[q] = Q[q]
    return R

def support(graph, colour, list_assignment):
    """
    A list of those vertices in 'graph' which have 'colour' in the list 
    associated with that vertex by 'list_assignment'.
    """
    return filter(lambda vertex: has_colour(colour, vertex, list_assignment), graph.nodes())

def support_subgraph(graph, colour, list_assignment):
    """
    The subgraph induced by those vertices of 'graph' which have 'colour' 
    in the list associated by 'list_assignment'.
    """
    return graph.subgraph(support(graph, colour, list_assignment))

def independence_number(graph):
    """
    Compute the independence number of 'graph'.
    """
    if graph.number_of_nodes() == 0:
        return 0
    else:
        return graph_clique_number(complement(graph))

