from src.classes.graph import Graph
from src.modules.dfs import Dfs
from src.modules.dfs_graph import construct_dfs_trees, construct_dfs_graph

def test_dfs():
    graph = Graph.load_from_file('pvl_6', True)
    dfs = Dfs(graph)

    assert dfs.get_colors() == {'A': 'black', 'B': 'black', 'C': 'black', 'D': 'black', 'E': 'black', 'F': 'black', 'G': 'black', 'H': 'black', 'I': 'black', 'J': 'black'}
    assert dfs.get_pi() == {'A': 'nil', 'B': 'A', 'C': 'B', 'D': 'A', 'E': 'D', 'F': 'E', 'G': 'nil', 'H': 'G', 'I': 'H', 'J': 'nil'}
    assert dfs.get_discovery_sequence() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    assert dfs.get_finishing_sequence() == ['C', 'B', 'F', 'E', 'D', 'A', 'I', 'H', 'G', 'J']
    assert dfs.get_discovery_times() == {'A': 1, 'B': 2, 'C': 3, 'D': 6, 'E': 7, 'F': 8, 'G': 13, 'H': 14, 'I': 15, 'J': 19}
    assert dfs.get_finishing_times() == {'C': 4, 'B': 5, 'F': 9, 'E': 10, 'D': 11, 'A': 12, 'I': 16, 'H': 17, 'G': 18, 'J': 20}
    assert dfs.get_low_values() == {'A': 1, 'B': 1, 'C': 1, 'D': 6, 'E': 6, 'F': 6, 'G': 13, 'H': 13, 'I': 13, 'J': 19}
    assert dfs.get_log_string() == '1: discovered A\n2: discovered B\n3: discovered C\n4: update low value of C (3 to 1) by 2nd condition\n4: finished C\n5: update low value of B (2 to 1) by 1st condition\n5: finished B\n6: update low value of A (1 to 1) by 1st condition\n6: discovered D\n7: discovered E\n8: discovered F\n9: update low value of F (8 to 6) by 2nd condition\n9: finished F\n10: update low value of E (7 to 6) by 1st condition\n10: finished E\n11: update low value of D (6 to 6) by 1st condition\n11: finished D\n12: update low value of A (1 to 1) by 1st condition\n12: finished A\n13: discovered G\n14: discovered H\n15: discovered I\n16: update low value of I (15 to 13) by 2nd condition\n16: finished I\n17: update low value of H (14 to 13) by 1st condition\n17: finished H\n18: update low value of G (13 to 13) by 1st condition\n18: finished G\n19: discovered J\n20: finished J'

def test_dfs_tree():
    graph = Graph.load_from_file('pvl_6', True)
    dfs = Dfs(graph)
    trees = construct_dfs_trees(dfs)

    assert trees[0].get_root().get_name() == 'A'
    assert trees[0].get_node_names() == ['A', 'B', 'C', 'D', 'E', 'F']
    assert trees[0].get_edges() == [('A', 'B'), ('B', 'C'), ('A', 'D'), ('D', 'E'), ('E', 'F')]

    assert trees[1].get_root().get_name() == 'G'
    assert trees[1].get_node_names() == ['G', 'H', 'I']
    assert trees[1].get_edges() == [('G', 'H'), ('H', 'I')]

    assert trees[2].get_root().get_name() == 'J'
    assert trees[2].get_node_names() == ['J']
    assert trees[2].get_edges() == []

def test_dfs_graph():
    graph = Graph.load_from_file('pvl_6', True)
    dfs = Dfs(graph)
    dfs_graph = construct_dfs_graph(dfs)

    assert dfs_graph.get_edges() == [('A', 'B'), ('B', 'C'), ('A', 'D'), ('D', 'E'), ('E', 'F'), ('G', 'H'), ('H', 'I')]