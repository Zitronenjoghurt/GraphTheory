from src.classes.graph import Graph
from src.modules.lpa import lpa
from src.modules.dfs import Dfs
from src.modules.dfs_graph import construct_dfs_trees, construct_dfs_graph

graph = Graph.load_from_file('pvl_6', True)

# Clustering
print(f"One possible clustering:\n{lpa(graph)}\n")

# Traversal
dfs = Dfs(graph)
print(f"Ordered by first visited:\n{dfs.get_discovery_sequence()}\n")
print(f"Ordered by first finished:\n{dfs.get_finishing_sequence()}\n")
print(f"Low values:\n{dfs.get_low_values()}\n")

trees = construct_dfs_trees(dfs)
dfs_graph = construct_dfs_graph(dfs)

# Visualization
# uncomment this to visualize it in a seperate window
# graph.visualize()
# uncomment this to export as png (requires graphviz)
# graph.visualize_pydot()