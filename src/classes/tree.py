from .graph import Graph, Node

class Tree(Graph):
    def __init__(self, root: str) -> None:
        super().__init__([root], directed=True)
        self.root = self.get_node(root)

    # Not implemented yet for Tree subclass
    @staticmethod
    def load_from_file(tree_name: str, directed: bool = False) -> None:
        return None

    def get_root(self) -> Node:
        return self.root
    
    def add_node(self, parent: str, node: str) -> bool:
        # Parent node does not exist
        if self.get_node(parent) is None:
            return False
        
        # Node already exists
        if self.get_node(node) is not None:
            return False
        
        super().add_node(node)
        self.add_edge(parent, node)

        return True