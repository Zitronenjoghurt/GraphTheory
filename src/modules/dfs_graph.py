from ..classes.graph import Graph
from ..classes.tree import Tree
from .dfs import Dfs

def construct_dfs_graph(dfs: Dfs) -> Graph:
    pi = dfs.pi
    nodes = dfs.get_discovery_sequence()
    edges = []

    for node, parent in pi.items():
        if parent != "nil":
            edges.append((parent, node))

    return Graph(nodes, edges, True)

def construct_dfs_trees(dfs: Dfs) -> list[Tree]:
    pi = dfs.pi
    trees: list[Tree] = []
    
    for node, parent in pi.items():
            if parent == "nil":
                trees.append(Tree(node))
            else:
                add_to_trees(node, parent, trees)

    return trees

def add_to_trees(node: str, parent: str, trees: list[Tree]) -> None:
     for tree in trees:
            if tree.has_node(parent):
                tree.add_node(parent, node)