from src.classes.graph import Graph
from src.modules.dfs import Dfs
from src.modules.dfs_tree import construct_dfs_trees

def test_dfs():
    graph = Graph.load_from_file('pvl_6', True)
    dfs = Dfs(graph)

    assert dfs.col == {'A': 'black', 'B': 'black', 'C': 'black', 'D': 'black', 'E': 'black', 'F': 'black', 'G': 'black', 'H': 'black', 'I': 'black', 'J': 'black'}
    assert dfs.pi == {'A': 'nil', 'B': 'A', 'C': 'B', 'D': 'A', 'E': 'D', 'F': 'E', 'G': 'nil', 'H': 'G', 'I': 'H', 'J': 'nil'}
    assert dfs.get_array_visited() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    assert dfs.get_array_finished() == ['C', 'B', 'F', 'E', 'D', 'A', 'I', 'H', 'G', 'J']

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