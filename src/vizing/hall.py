import itertools
from networkx import graph_clique_number, complement
from test_functions import has_colour

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

def hall_number(graph, list_assignment, colour):
    """
    Compute the independence number of the subgraph induced by those 
    vertices in 'graph' having 'colour' in their list.
    """
    return independence_number(support_subgraph(graph, colour, list_assignment))

def halls_sum(graph, list_assignment, colours):
    """
    Sum Hall numbers over all monochromatic subgraphs.
    """
    return sum([hall_number(graph, list_assignment, colour) for colour in colours])

def halls_condition(graph, list_assignment, colours):
    """
    Decide whether Hall's condition is satisfied.
    """
    return halls_sum(graph, list_assignment, colours) >= len(graph.nodes())

def halls_condition_induced_by(graph, size, list_assignment, colours, vertices):
    """
    Check Hall's condition for a subgraph of 'graph' induced by 'vertices'.
    """
    H = graph.subgraph(vertices)
    return halls_condition(H, list_assignment, colours)
