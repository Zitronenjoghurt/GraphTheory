from src.classes.graph import Graph

def test_init_unweighted():
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

def test_init_weighted():
    graph = Graph.load_from_file("first_weighted", True)
    A = graph.get_node('A')
    B = graph.get_node('B')
    C = graph.get_node('C')
    D = graph.get_node('D')
    E = graph.get_node('E')
    F = graph.get_node('F')
    
    assert A.get_neighbor_names() == ["B", "C"]
    assert A.get_weight('B') == 4
    assert A.get_weight('C') == 3
    assert B.get_neighbor_names() == ["C", "D"]
    assert B.get_weight('C') == 5
    assert B.get_weight('D') == 2
    assert C.get_neighbor_names() == ["D"]
    assert C.get_weight('D') == 7
    assert D.get_neighbor_names() == ["E"]
    assert D.get_weight('E') == 2
    assert E.get_neighbor_names() == ["A", "B", "F"]
    assert E.get_weight('A') == 4
    assert E.get_weight('B') == 4
    assert E.get_weight('F') == 6
    assert F.get_neighbor_names() == []
    assert F.get_weights() == {}

def test_init_grid_based():
    graph = Graph.load_from_file("first_grid_based")
    A = graph.get_node('A')
    B = graph.get_node('B')
    C = graph.get_node('C')
    D = graph.get_node('D')
    E = graph.get_node('E')
    F = graph.get_node('F')
    G = graph.get_node('G')
    H = graph.get_node('H')
    I = graph.get_node('I')

    assert A.get_coordinates() == [0, 0, 0]
    assert B.get_coordinates() == [10, 0, 0]
    assert C.get_coordinates() == [20, 0, 0]
    assert D.get_coordinates() == [0, 10, 0]
    assert E.get_coordinates() == [10, 10, 0]
    assert F.get_coordinates() == [20, 10, 0]
    assert G.get_coordinates() == [0, 20, 0]
    assert H.get_coordinates() == [10, 20, 0]
    assert I.get_coordinates() == [20, 20, 0]

    assert graph.get_node_distance('A', 'B') == 10
    assert graph.get_node_distance('A', 'C') == 20
    assert graph.get_node_distance('A', 'D') == 10
    assert graph.get_node_distance('A', 'E', 2) == 14.14
    assert graph.get_node_distance('A', 'F', 2) == 22.36
    assert graph.get_node_distance('A', 'G') == 20
    assert graph.get_node_distance('A', 'H', 2) == 22.36
    assert graph.get_node_distance('A', 'I', 2) == 28.28
    assert graph.get_node_distance('B', 'C') == 10

    assert A.get_weight('B') == 10
    assert A.get_weight('D') == 10
    assert A.get_weight('I') == 28.28
    assert B.get_weight('C') == 10

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
    graph1 = Graph(nodes=['A', 'B', 'C'])
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
    graph2 = Graph(nodes=['A', 'B', 'C'], directed=True)
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
    graph3 = Graph(nodes=['A', 'B', 'C'])
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

def test_set_edge_weight():
    graph = Graph.load_from_file('first_weighted', True)
    assert graph.set_edge_weight("A", "B", 1) == True
    assert graph.set_edge_weight("A", "C", 2) == True
    assert graph.set_edge_weight("B", "C", 3) == True
    assert graph.set_edge_weight("B", "D", 4) == True
    assert graph.set_edge_weight("C", "D", 5) == True
    assert graph.set_edge_weight("D", "E", 6) == True
    assert graph.set_edge_weight("E", "A", 7) == True
    assert graph.set_edge_weight("E", "B", 8) == True
    assert graph.set_edge_weight("E", "F", 9) == True

    assert graph.set_edge_weight("B", "A", 1) == False
    assert graph.set_edge_weight("C", "A", 2) == False
    assert graph.set_edge_weight("C", "B", 3) == False
    assert graph.set_edge_weight("D", "B", 4) == False
    assert graph.set_edge_weight("D", "C", 5) == False
    assert graph.set_edge_weight("E", "D", 6) == False
    assert graph.set_edge_weight("A", "E", 7) == False
    assert graph.set_edge_weight("B", "E", 8) == False
    assert graph.set_edge_weight("F", "E", 9) == False

    assert graph.get_node('A').get_weights() == {'B': 1, 'C': 2}
    assert graph.get_node('B').get_weights() == {'C': 3, 'D': 4}
    assert graph.get_node('C').get_weights() == {'D': 5}
    assert graph.get_node('D').get_weights() == {'E': 6}
    assert graph.get_node('E').get_weights() == {'A': 7, 'B': 8, 'F': 9}

def test_invert_graph():
    graph = Graph.load_from_file('3_circle', True)
    inverted_graph = graph.get_inverted_graph()

    assert inverted_graph.get_node('A').get_neighbor_names() == ['C']
    assert inverted_graph.get_node('B').get_neighbor_names() == ['A']
    assert inverted_graph.get_node('C').get_neighbor_names() == ['B']