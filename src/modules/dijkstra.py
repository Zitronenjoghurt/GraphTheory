from ..interfaces.graph_protocol import IGraph
from typing import Optional

# Full analysis will calculate the shortest path from every node to every other node
class Dijkstra:
    def __init__(self, graph: IGraph, start_node: str|None = None, full_analysis: bool = False) -> None:
        self.graph = graph
        self.distances = {}
        self.origins = {}

        if full_analysis:
            self.full_analysis()
        elif start_node is not None:
            self.run_dijkstra(start_node)

    def full_analysis(self) -> None:
        for node in self.graph.get_node_names():
            self.run_dijkstra(node)

    def run_dijkstra(self, start_node: str) -> None:
        node_names = self.graph.get_node_names()
        distances = {node: 0 if node == start_node else float('inf') for node in node_names}
        origin = {node: node for node in node_names}
        unvisited = [node for node in node_names]

        current_node = self.graph.get_node(start_node)
        while len(unvisited) != 0:
            current_node_name = current_node.get_name()
            current_distance = distances[current_node_name]
            for neighbor in current_node.get_neighbors():
                neighbor_name = neighbor.get_name()
                if neighbor_name not in unvisited:
                    continue
                
                distance = current_distance + current_node.get_weight(neighbor_name)
                if distance < distances[neighbor_name]:
                    distances[neighbor_name] = distance
                    origin[neighbor_name] = current_node_name
            
            unvisited.remove(current_node_name)
            next_node_name = self.select_next_node(distances, unvisited)
            if next_node_name is None:
                break
            
            current_node = self.graph.get_node(next_node_name)

        self.distances[start_node] = distances
        self.origins[start_node] = origin

    def get_distances(self) -> dict[str, dict[str, int]]:
        return self.distances
    
    def get_node_distances(self, node: str) -> Optional[dict[str, int]]:
        return self.distances.get(node, None)
    
    def get_origins(self) -> dict[str, dict[str, str]]:
        return self.origins
    
    def get_node_origins(self, node: str) -> Optional[dict[str, str]]:
        return self.origins.get(node, None)
    
    def get_origin_node(self, start_node: str, current_node: str) -> Optional[str]:
        origins = self.get_node_origins(start_node)
        if origins is None:
            return None
        
        return origins.get(current_node, None)
    
    def is_analyzed(self, node: str) -> bool:
        return self.get_node_distances(node) is not None and self.get_node_origins(node) is not None

    def get_shortest_path(self, start_node: str, end_node: str) -> list[str]:
        if not self.is_analyzed(start_node):
            self.run_dijkstra(start_node)

        if start_node == end_node:
            return [start_node]
        
        closer_end_node = self.get_origin_node(start_node, end_node)
        if closer_end_node == end_node:
            return []
        
        return self.get_shortest_path(start_node, closer_end_node) + [end_node]

    @staticmethod
    def select_next_node(distances: dict[str, int|float], univisted: list[str]) -> Optional[str]:
        min_node = None
        min_distance = float('inf')
        for node, distance in distances.items():
            if distance < min_distance and node in univisted:
                min_node = node
                min_distance = distance
        return min_node