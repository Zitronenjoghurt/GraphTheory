from src.classes.graph import Graph
from src.modules.dfs import Dfs
from src.modules.dfs_tree import construct_dfs_trees

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