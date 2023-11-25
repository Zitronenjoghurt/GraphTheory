from collections import Counter
from random import choice, shuffle

# Label Propagation Algorithm
# Used to find clusters in a graph
def lpa(graph, max_iterations: int = 100000) -> list[list[str]]:
    nodes = graph.get_nodes()
    cluster_state = {node : node for node in nodes}

    changed = True
    iterations = 0
    while changed and iterations < max_iterations:
        changed = False
        shuffle(nodes)

        for node in nodes:
            new_cluster = determine_cluster(graph, cluster_state, node)

            if new_cluster != cluster_state[node]:
                changed = True
                cluster_state[node] = new_cluster

        iterations += 1
    
    return map_result(cluster_state)

def get_neighbor_clusters(cluster_state: dict[str, str], nodes: list) -> list:
    result = []
    for node in nodes:
        result.append(cluster_state[node])

    return result

def most_common_cluster(clusters: list, current_cluster: str) -> str:
    counts = Counter(clusters)
    max_amount = counts.most_common(1)[0][1]

    most_common = [item for item, amount in counts.items() if amount == max_amount]
    
    if len(most_common) == 1:
        return most_common[0]
    
    # Choose current cluster to encourage the formation of more clusters
    if current_cluster in most_common:
        return current_cluster
    
    return choice(most_common)

def determine_cluster(graph, cluster_state: dict[str, str], node_name: str) -> str:
    node = graph.get_node(node_name)
    neighbors = node.get_neighbor_names()

    neighbor_clusters = get_neighbor_clusters(cluster_state, neighbors)
    return most_common_cluster(neighbor_clusters, cluster_state[node_name])

def map_result(cluster_state: dict[str, str]) -> list[list[str]]:
    result = {}

    for node, cluster in cluster_state.items():
        if cluster not in result.keys():
            result[cluster] = []
        
        if node not in result[cluster]:
            result[cluster].append(node)
    
    return result.values()