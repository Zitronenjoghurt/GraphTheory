from graph_protocol import IGraph, INode

class ITree(IGraph):
    @staticmethod
    def load_from_file(tree_name: str, directed: bool = False) -> None:
        ...
    def get_root(self) -> INode:
        ...
    def add_child(self, child: str, parent: str) -> bool:
        ...