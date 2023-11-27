from src.classes.graph import Graph
from src.modules.lpa import lpa
from src.modules.dfs import Dfs
from src.modules.dfs_graph import construct_dfs_trees, construct_dfs_graph
from src.modules.kosaraju import find_sccs

graph = Graph.load_from_file('pvl_6', True)

# Traversal
dfs = Dfs(graph)
print(dfs.get_log_string())
print(f"\npi:\n{dfs.get_pi()}\n")
print(f"Ordered by first visited:\n{dfs.get_discovery_sequence()}\n")
print(f"Ordered by first finished:\n{dfs.get_finishing_sequence()}\n")
print(f"Discovery times:\n{dfs.get_discovery_times()}\n")
print(f"Finishing times:\n{dfs.get_finishing_times()}\n")
print(f"Low values:\n{dfs.get_low_values()}\n")
print(f"Strongly connected components:\n{find_sccs(graph)}\n")

trees = construct_dfs_trees(dfs)
dfs_graph = construct_dfs_graph(dfs)

# Clustering
print(f"One possible clustering:\n{lpa(graph)}\n")

# Visualization
# uncomment for mermaid representation
print(graph.to_mermaid("TD"))
# uncomment this to visualize it in a seperate window
# graph.visualize()
# uncomment this to export as png (requires graphviz)
# graph.visualize_pydot()