from ..interfaces.graph_protocol import IGraph
from .dfs import Dfs
from .dfs_graph import construct_dfs_trees

# Kosaraju Algorithm
# Finds strongly connected components (SCC's) 
def find_sccs(graph: IGraph) -> list[list[str]]:
    first_dfs = Dfs(graph)

    # Next visit order is from last finished to first finished
    visit_order = list(reversed(first_dfs.get_finishing_sequence()))

    reversed_graph = graph.get_inverted_graph()
    second_dfs = Dfs(reversed_graph, visit_order)

    trees = construct_dfs_trees(second_dfs)
    return [tree.get_node_names() for tree in trees]