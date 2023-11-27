from ..interfaces.graph_protocol import IGraph, INode

# Depth Field Search
# Traversal algorithm
class Dfs():
    def __init__(self, graph: IGraph, node_order: list[str] = None) -> None:
        # discovery time
        self.d = {}

        # finishing time
        self.f = {} 

        # low value
        self.l = {}

        # pi(node) = node which discovered the specified node
        self.pi = {node: "nil" for node in graph.get_node_names()} 

        # white = unvisited, grey = visited, black = finished
        self.col = {node: "white" for node in graph.get_node_names()}  

        # contains step-by-step what the DFS did at what time
        self.log = []

        nodes = graph.get_node_names()
        if node_order is not None:
            nodes = node_order
        
        self.time = 1
        for node_name in nodes:
            node = graph.get_node(node_name)
            if self.col[node.get_name()] == "white":
                self.dfs_visit(node)

    def dfs_visit(self, node: INode) -> None:
        node_name = node.get_name()

        self.col[node_name] = "grey"
        self.d[node_name] = self.time
        self.l[node_name] = self.time
        self.log.append(f"{self.time}: discovered {node_name}")
        self.time += 1
        
        for neighbor in node.get_neighbors():
            neighbor_name = neighbor.get_name()
            if self.col[neighbor_name] == "white":
                self.pi[neighbor_name] = node_name
                self.dfs_visit(neighbor)

                previous_l = self.l[node_name]
                self.l[node_name] = min(self.l[node_name], self.l[neighbor_name])
                current_l = self.l[node_name]
                self.log.append(f"{self.time}: update low value of {node_name} ({previous_l} to {current_l}) by 1st condition")

            if self.col[neighbor_name] == "grey" and self.pi[node_name] != neighbor_name:
                previous_l = self.l[node_name]
                self.l[node_name] = min(self.l[node_name], self.d[neighbor_name])
                current_l = self.l[node_name]
                self.log.append(f"{self.time}: update low value of {node_name} ({previous_l} to {current_l}) by 2nd condition")
        
        self.col[node_name] = "black"
        self.f[node_name] = self.time
        self.log.append(f"{self.time}: finished {node_name}")
        self.time += 1

    def get_discovery_sequence(self) -> list[str]:
        return list(self.d.keys())
    
    def get_finishing_sequence(self) -> list[str]:
        return list(self.f.keys())
    
    def get_discovery_times(self) -> dict[str, int]:
        return self.d
    
    def get_finishing_times(self) -> dict[str, int]:
        return self.f
    
    def get_low_values(self) -> dict[str, int]:
        return self.l
    
    def get_pi(self) -> dict[str, str]:
        return self.pi
    
    def get_colors(self) -> dict[str, str]:
        return self.col
    
    def get_log(self) -> list[str]:
        return self.log
    
    def get_log_string(self) -> str:
        return '\n'.join(self.log)