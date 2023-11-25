from src.classes.graph import Graph

graph = Graph.load_from_file('pvl_6', True)
graph.visualize()