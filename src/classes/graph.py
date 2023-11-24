import json
import os
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
    for edge in graph['edges']:
        GRAPHS[name]['edges'].append((edge[0], edge[1]))
# finished preparing graph data

class Graph:
    def __init__(self, nodes: list, edges: list[tuple], directed: bool = False) -> None:
        self.directed = directed
        
        self.nodes = {}
        for node in nodes:
            self.nodes[node] = Node(node)

        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def load_from_file(graph_name: str, directed: bool = False) -> Optional['Graph']:
        if graph_name not in GRAPHS:
            return None
        
        graph = GRAPHS[graph_name]
        return Graph(graph['nodes'], graph['edges'], directed)

    def get_node(self, name: str) -> Optional['Node']:
        return self.nodes.get(name, None)
    
    def add_node(self, name: str) -> bool:
        if name in self.nodes:
            return False
        
        self.nodes[name] = Node(name)
        return True
    
    def add_edge(self, node1: str, node2: str) -> bool:
        if not node1 or not node2:
            return False

        self.nodes[node1].add_neighbor(self.nodes[node2])
        if not self.directed:
            self.nodes[node2].add_neighbor(self.nodes[node1])

class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors = {}

    def get_name(self) -> str:
        return self.name

    def add_neighbor(self, neighbor: 'Node') -> bool:
        name = neighbor.get_name()
        if name in self.neighbors:
            return False
        
        self.neighbors[name] = neighbor
        return True

    def remove_neighbor(self, neighbor: 'Node') -> bool:
        name = neighbor.get_name()
        if name not in self.neighbors:
            return False
        
        self.neighbors.pop(name)
        return True
    
    def get_neighbor(self, name: str) -> Optional['Node']:
        return self.neighbors.get(name, None)