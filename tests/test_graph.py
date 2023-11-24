from src.classes.graph import Graph

def test_init():
    graph = Graph.load_from_file('3_circle')
    A = graph.get_node('A')
    B = graph.get_node('B')
    C = graph.get_node('C')

    assert A is not None
    assert B is not None
    assert C is not None

    assert A.get_neighbor('B') is not None
    assert A.get_neighbor('C') is not None
    assert B.get_neighbor('A') is not None
    assert B.get_neighbor('C') is not None
    assert C.get_neighbor('A') is not None
    assert C.get_neighbor('B') is not None

    assert A.get_neighbor('A') is None
    assert B.get_neighbor('B') is None
    assert C.get_neighbor('C') is None