import json
import matplotlib.pyplot as plt
import networkx as nx
import os

from ..modules.utilities import get_safe
from networkx.drawing.nx_pydot import to_pydot
from typing import Optional

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPH_FILE_PATH = os.path.join(CURRENT_DIR, '..', 'data', 'graphs.json')

# start preparing graph data
with open(GRAPH_FILE_PATH, 'r') as f:
        data = json.load(f)
GRAPHS = {}
for name, graph in data.items():
    GRAPHS[name] = {}
    GRAPHS[name]['nodes'] = graph['nodes'] 
    GRAPHS[name]['edges'] = []
    GRAPHS[name]['weights'] = []
    for edge in graph['edges']:
        GRAPHS[name]['edges'].append((edge[0], edge[1]))
        if len(edge) == 3:
            GRAPHS[name]['weights'].append(edge[2])
# finished preparing graph data

class Graph:
    def __init__(self, nodes: list|None = None, edges: list[tuple]|None = None, directed: bool = False, weights: list[int]|None = None) -> None:
        # Refrain from using mutable default arguments
        if nodes is None:
            nodes = []
        if edges is None:
            edges = []
        if weights is None:
            weights = []

        self.directed = directed
        self.edges = []
        
        self.nodes = {}
        for node in nodes:
            self.nodes[node] = Node(node)

        for i, edge in enumerate(edges):
            weight = get_safe(weights, i)
            if weight is not None:
                self.add_edge(edge[0], edge[1], weight)
            else:
                self.add_edge(edge[0], edge[1])

    @staticmethod
    def load_from_file(graph_name: str, directed: bool = False) -> Optional['Graph']:
        if graph_name not in GRAPHS:
            return None
        
        graph = GRAPHS[graph_name]
        return Graph(graph['nodes'], graph['edges'], directed, graph['weights'])

    def get_node(self, name: str) -> Optional['Node']:
        return self.nodes.get(name, None)
    
    def has_node(self, name: str) -> bool:
        return self.get_node(name) is not None
    
    def get_nodes(self) -> list['Node']:
        return list(self.nodes.values())
    
    def get_node_names(self) -> list[str]:
        return list(self.nodes.keys())
    
    def get_edges(self) -> list[tuple[str, str]]:
        return self.edges
    
    def get_edges_inverted(self) -> list[tuple[str, str]]:
        edges = self.get_edges()
        return [(b, a) for a, b in edges]
    
    def get_inverted_graph(self) -> 'Graph':
        if self.directed:
            nodes = self.get_node_names()
            edges = self.get_edges_inverted()
            return Graph(nodes, edges, True)
        return self
    
    def add_node(self, name: str) -> bool:
        if name in self.nodes:
            return False
        
        self.nodes[name] = Node(name)
        return True
    
    def remove_node(self, name: str) -> bool:
        if name not in self.nodes:
            return False
        
        node = self.nodes.pop(name)
        for neighbor in node.get_neighbors():
            neighbor.remove_neighbor(node)
        
        return True
    
    def add_edge(self, node1: str, node2: str, weight: int = 1) -> bool:
        if self.get_node(node1) is None or self.get_node(node2) is None:
            return False
        
        if (node1, node2) in self.edges:
            return False

        self.edges.append((node1, node2))
        self.get_node(node1).add_neighbor(self.get_node(node2), weight)
        
        if not self.directed:
            self.edges.append((node2, node1))
            self.get_node(node2).add_neighbor(self.get_node(node1), weight)

        return True
    
    def remove_edge(self, node1: str, node2: str) -> bool:
        if self.get_node(node1) is None or self.get_node(node2) is None:
            return False
        
        if (node1, node2) not in self.edges:
            if self.directed:
                return False
            if (node2, node1) not in self.edges:
                return False

        if self.directed or (node1, node2) in self.edges:
            self.edges.remove((node1, node2))
        
        if not self.directed and (node2, node1) in self.edges:
            self.edges.remove((node2, node1))

        self.get_node(node1).remove_neighbor(self.get_node(node2))
        if not self.directed:
            self.get_node(node2).remove_neighbor(self.get_node(node1))

        return True
    
    def set_edge_weight(self, node1: str, node2: str, weight: int) -> bool:
        first = self.get_node(node1).set_weight(node2, weight)

        second = True
        if not self.directed:
            second = self.get_node(node2).set_weight(node1, weight)

        return first and second
    
    def to_mermaid(self, direction: str = "LR") -> str:
        mermaid = f"graph {direction};\n"
        
        for edge in self.get_edges():
            mermaid += f"{edge[0]} --> {edge[1]}\n"
        
        return mermaid

    def to_nx_graph(self) -> nx.Graph | nx.DiGraph:
        graph = nx.DiGraph() if self.directed else nx.Graph()

        graph.add_nodes_from(self.get_node_names())
        graph.add_edges_from(self.get_edges())

        return graph
    
    def visualize(self, layout: str = "spring") -> None:
        graph = self.to_nx_graph()

        match layout:
            case 'circular':
                pos = nx.circular_layout(graph)
            case 'spring':
                pos = nx.spring_layout(graph)
            case 'spectral':
                pos = nx.spectral_layout(graph)
            case 'shell':
                pos = nx.shell_layout(graph)
            case 'kamada_kawai':
                pos = nx.kamada_kawai_layout(graph)
            case _:
                pos = nx.random_layout(graph)

        nx.draw(graph, pos, with_labels=True, node_color='lightgray', node_size=500, edge_color='black', font_size=15)

        plt.show()
    
    # Requires installing graphviz on your system
    # https://graphviz.org/download/
    # Layouts include: dot, neato, fdp, sfdp, twopi, circo
    def visualize_pydot(self, layout: str = 'dot') -> None:
        try: 
            graph = self.to_nx_graph()
            pydot_graph = to_pydot(graph)
            pydot_graph.set_layout(layout)
            pydot_graph.write_png('graph.png')
        except Exception:
            print("Make sure you have graphviz installed on your system and added to your PATH variable\nhttps://graphviz.org/download/")

class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors = {}
        self.weights = {}

    def get_name(self) -> str:
        return self.name

    def add_neighbor(self, neighbor: 'Node', weight: int = 1) -> bool:
        name = neighbor.get_name()
        if name in self.neighbors:
            return False
        
        self.neighbors[name] = neighbor
        self.weights[name] = weight
        return True

    def remove_neighbor(self, neighbor: 'Node') -> bool:
        name = neighbor.get_name()
        if name not in self.neighbors:
            return False
        
        self.neighbors.pop(name)
        return True
    
    def set_weight(self, neighbor: str, weight: int) -> bool:
        if neighbor not in self.neighbors:
            return False
        
        self.weights[neighbor] = weight
        return True
    
    def get_neighbor(self, name: str) -> Optional['Node']:
        return self.neighbors.get(name, None)
    
    def get_neighbors(self) -> list['Node']:
        return list(self.neighbors.values())
    
    def get_neighbor_names(self) -> list[str]:
        return [neighbor.get_name() for neighbor in self.get_neighbors()]
    
    def get_weight(self, neighbor: str) -> Optional[int]:
        return self.weights.get(neighbor, None)

    def get_weights(self) -> dict[str, int]:
        return self.weights