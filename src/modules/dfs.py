from ..interfaces.graph_protocol import IGraph, INode
from ..classes.tree import Tree

# Depth Field Search
# Traversal algorithm
class Dfs():
    def __init__(self, graph: IGraph) -> None:
        # discovery time
        self.d = {}

        # finishing time
        self.f = {} 

        # pi(node) = node which discovered the specified node
        self.pi = {node: "nil" for node in graph.get_node_names()} 

        # white = unvisited, grey = visited, black = finished
        self.col = {node: "white" for node in graph.get_node_names()}  

        self.time = 1
        for node in graph.get_nodes():
            if self.col[node.get_name()] == "white":
                self.dfs_visit(node)

        self.trees: list[Tree] = []
        self.construct_trees()

    def dfs_visit(self, node: INode) -> None:
        node_name = node.get_name()

        self.col[node_name] = "grey"
        self.d[node_name] = self.time
        self.time += 1
        
        for neighbor in node.get_neighbors():
            neighbor_name = neighbor.get_name()
            if self.col[neighbor_name] == "white":
                self.pi[neighbor_name] = node_name
                self.dfs_visit(neighbor)
        
        self.col[node_name] = "black"
        self.f[node_name] = self.time
        self.time += 1

    def construct_trees(self) -> None:
        for node, parent in self.pi.items():
            if parent == "nil":
                self.trees.append(Tree(node))
            else:
                self.add_to_trees(node, parent)
    
    def add_to_trees(self, node, parent) -> None:
        for tree in self.trees:
            if tree.has_node(parent):
                tree.add_node(parent, node)