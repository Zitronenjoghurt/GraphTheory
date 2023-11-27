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

def test_add_node():
    graph = Graph()

    assert graph.get_node('A') is None
    assert graph.get_node('B') is None
    assert graph.get_node('C') is None

    assert graph.add_node('A') is True
    assert graph.add_node('B') is True
    assert graph.add_node('C') is True

    assert graph.get_node('A') is not None
    assert graph.get_node('B') is not None
    assert graph.get_node('C') is not None

    assert graph.add_node('A') is False
    assert graph.add_node('B') is False
    assert graph.add_node('C') is False

def test_remove_node():
    graph = Graph.load_from_file('3_circle')

    assert graph.get_node('A') is not None
    assert graph.get_node('B') is not None
    assert graph.get_node('C') is not None

    assert graph.remove_node('A') is True
    assert graph.get_node('B').get_neighbor('A') is None
    assert graph.get_node('C').get_neighbor('A') is None

    assert graph.remove_node('B') is True
    assert graph.get_node('C').get_neighbor('A') is None

    assert graph.remove_node('C') is True

    assert graph.get_node('A') is None
    assert graph.get_node('B') is None
    assert graph.get_node('C') is None

    assert graph.remove_node('A') is False
    assert graph.remove_node('B') is False
    assert graph.remove_node('C') is False

def test_add_edge():
    # unweighted undirected
    graph1 = Graph(['A', 'B', 'C'])
    assert graph1.add_edge('A', 'B') is True
    assert graph1.add_edge('A', 'B') is False
    assert graph1.add_edge('B', 'A') is False
    assert graph1.add_edge('B', 'C') is True
    assert graph1.add_edge('B', 'C') is False
    assert graph1.add_edge('C', 'B') is False
    assert graph1.add_edge('C', 'A') is True
    assert graph1.add_edge('C', 'A') is False
    assert graph1.add_edge('A', 'C') is False

    assert graph1.get_node('A').get_neighbor_names() == ['B', 'C']
    assert graph1.get_node('B').get_neighbor_names() == ['A', 'C']
    assert graph1.get_node('C').get_neighbor_names() == ['B', 'A']

    # unweighted directed
    graph2 = Graph(['A', 'B', 'C'], directed=True)
    assert graph2.add_edge('A', 'B') is True
    assert graph2.add_edge('A', 'B') is False
    assert graph2.add_edge('B', 'C') is True
    assert graph2.add_edge('B', 'C') is False
    assert graph2.add_edge('C', 'A') is True
    assert graph2.add_edge('C', 'A') is False

    assert graph2.get_node('A').get_neighbor('B') is not None
    assert graph2.get_node('A').get_neighbor('C') is None
    assert graph2.get_node('B').get_neighbor('A') is None
    assert graph2.get_node('B').get_neighbor('C') is not None
    assert graph2.get_node('C').get_neighbor('A') is not None
    assert graph2.get_node('C').get_neighbor('B') is None

    assert graph2.add_edge('B', 'A') is True
    assert graph2.add_edge('C', 'B') is True
    assert graph2.add_edge('A', 'C') is True

    # weighted undirected
    graph3 = Graph(['A', 'B', 'C'])
    assert graph3.add_edge('A', 'B', 1337) is True
    assert graph3.add_edge('B', 'C', 27) is True
    assert graph3.add_edge('C', 'A', 42) is True

    assert graph3.get_node('A').get_weights() == {'B': 1337, 'C': 42}
    assert graph3.get_node('A').get_weight('B') == 1337
    assert graph3.get_node('A').get_weight('C') == 42
    assert graph3.get_node('B').get_weights() == {'A': 1337, 'C': 27}
    assert graph3.get_node('B').get_weight('A') == 1337
    assert graph3.get_node('B').get_weight('C') == 27
    assert graph3.get_node('C').get_weights() == {'B': 27, 'A': 42}
    assert graph3.get_node('C').get_weight('A') == 42
    assert graph3.get_node('C').get_weight('B') == 27

    # weighted directed
    graph4 = Graph(['A', 'B', 'C'], directed=True)
    assert graph4.add_edge('A', 'B', 1337) is True
    assert graph4.add_edge('B', 'C', 27) is True
    assert graph4.add_edge('C', 'A', 42) is True

    assert graph4.get_node('A').get_weights() == {'B': 1337}
    assert graph4.get_node('A').get_weight('B') == 1337
    assert graph4.get_node('A').get_weight('C') is None
    assert graph4.get_node('B').get_weights() == {'C': 27}
    assert graph4.get_node('B').get_weight('A') is None
    assert graph4.get_node('B').get_weight('C') == 27
    assert graph4.get_node('C').get_weights() == {'A': 42}
    assert graph4.get_node('C').get_weight('A') == 42
    assert graph4.get_node('C').get_weight('B') is None

def test_remove_edge():
    graph = Graph.load_from_file('3_circle')

    assert graph.remove_edge('A', 'B') is True
    assert graph.get_node('A').get_neighbor('B') is None
    assert graph.get_node('B').get_neighbor('A') is None
    assert graph.get_node('B').get_neighbor('C') is not None
    assert graph.get_node('C').get_neighbor('B') is not None
    assert graph.get_node('C').get_neighbor('A') is not None
    assert graph.get_node('A').get_neighbor('C') is not None

    assert graph.remove_edge('B', 'C') is True
    assert graph.get_node('B').get_neighbor('C') is None
    assert graph.get_node('C').get_neighbor('B') is None
    assert graph.get_node('C').get_neighbor('A') is not None
    assert graph.get_node('A').get_neighbor('C') is not None

    assert graph.remove_edge('C', 'A') is True
    assert graph.get_node('C').get_neighbor('A') is None
    assert graph.get_node('A').get_neighbor('C') is None

    assert graph.remove_edge('A', 'B') is False
    assert graph.remove_edge('B', 'C') is False
    assert graph.remove_edge('C', 'A') is False

    graph2 = Graph.load_from_file('3_circle', directed=True)

    assert graph2.remove_edge('A', 'B') is True
    assert graph2.get_node('A').get_neighbor('B') is None
    assert graph2.get_node('B').get_neighbor('C') is not None
    assert graph2.get_node('C').get_neighbor('A') is not None

    assert graph2.remove_edge('B', 'C') is True
    assert graph2.get_node('B').get_neighbor('C') is None
    assert graph2.get_node('C').get_neighbor('A') is not None

    assert graph2.remove_edge('C', 'A') is True
    assert graph2.get_node('C').get_neighbor('A') is None

def test_invert_graph():
    graph = Graph.load_from_file('3_circle', True)
    inverted_graph = graph.get_inverted_graph()

    assert inverted_graph.get_node('A').get_neighbor_names() == ['C']
    assert inverted_graph.get_node('B').get_neighbor_names() == ['A']
    assert inverted_graph.get_node('C').get_neighbor_names() == ['B']