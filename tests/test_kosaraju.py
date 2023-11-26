from src.classes.graph import Graph
from src.modules.kosaraju import find_sccs

def test_find_sccs():
    graph = Graph.load_from_file("pvl_6", True)
    sccs = find_sccs(graph)

    assert sccs == [['A', 'C', 'B'], ['D', 'F', 'E'], ['G', 'I', 'H'], ['J']]