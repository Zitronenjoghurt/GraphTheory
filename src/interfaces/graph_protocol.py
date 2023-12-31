import networkx as nx
from typing import Optional, Protocol

class IGraph(Protocol):
    def load_from_file(graph_name: str, directed: bool = False) -> Optional['IGraph']:
        ...
    def get_node(self, name: str) -> Optional['INode']:
        ...
    def has_node(self, name: str) -> bool:
        ...
    def get_nodes(self) -> list['INode']:
        ...
    def get_node_names(self) -> list[str]:
        ...
    def get_edges(self) -> list[tuple[str, str]]:
        ...
    def get_edges_inverted(self) -> list[tuple[str, str]]:
        ...
    def get_inverted_graph(self) -> 'IGraph':
        ...
    def add_node(self, name: str) -> bool:
        ...
    def remove_node(self, name: str) -> bool:
        ...
    def add_edge(self, node1: str, node2: str, weight: int = 1) -> bool:
        ...
    def remove_edge(self, node1: str, node2: str) -> bool:
        ...
    def set_edge_weight(self, node1: str, node2: str, weight: int) -> bool:
        ...
    def to_mermaid(self, direction: str = "LR") -> str:
        ...
    def to_nx_graph(self) -> nx.Graph | nx.DiGraph:
        ...
    def visualize(self, layout: str = "spring") -> None:
        ...
    def visualize_pydot(self, layout: str = 'dot') -> None:
        ...

class INode(Protocol):
    def get_name(self) -> str:
        ...
    def add_neighbor(self, neighbor: 'INode') -> bool:
        ...
    def remove_neighbor(self, neighbor: 'INode') -> bool:
        ...
    def set_weight(self, neighbor: str, weight: int) -> bool:
        ...
    def get_neighbor(self, name: str) -> Optional['INode']:
        ...
    def get_neighbors(self) -> list['INode']:
        ...
    def get_neighbor_names(self) -> list[str]:
        ...
    def get_weight(self, neighbor: str) -> Optional[int]:
        ...
    def get_weights(self) -> dict[str, int]:
        ...