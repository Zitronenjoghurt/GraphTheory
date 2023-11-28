from src.classes.graph import Graph
from src.modules.dijkstra import Dijkstra

def test_init():
    graph = Graph.load_from_file("first_weighted", True)

    djk1 = Dijkstra(graph)
    assert djk1.get_distances() == {}
    assert djk1.get_origins() == {}

    djk2 = Dijkstra(graph, "A")
    assert djk2.get_distances() == {'A': {'A': 0, 'B': 4, 'C': 3, 'D': 6, 'E': 8, 'F': 14}}
    assert djk2.get_origins() == {'A': {'A': 'A', 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'D', 'F': 'E'}}

def test_select_next_node():
    distances = {'A': 0, 'B': 2, 'C': 1, 'D': 1, 'E': float('inf')}
    unvisited = ['A', 'B', 'C', 'D', 'E']
    assert Dijkstra.select_next_node(distances, unvisited) == 'A'

    unvisited = ['B', 'C', 'D', 'E']
    assert Dijkstra.select_next_node(distances, unvisited) == 'C'

    unvisited = ['B', 'E']
    assert Dijkstra.select_next_node(distances, unvisited) == 'B'

    unvisited = ['']
    assert Dijkstra.select_next_node(distances, unvisited) is None

def test_get_shortest_path():
    graph = Graph.load_from_file("first_weighted", True)
    djk = Dijkstra(graph)

    assert djk.get_shortest_path('A', 'B') == ["A", "B"]
    assert djk.get_shortest_path('A', 'C') == ["A", "C"]
    assert djk.get_shortest_path('A', 'D') == ["A", "B", "D"]
    assert djk.get_shortest_path('A', 'E') == ["A", "B", "D", "E"]
    assert djk.get_shortest_path('A', 'F') == ["A", "B", "D", "E", "F"]

    assert djk.get_shortest_path('B', 'A') == ['B', 'D', 'E', 'A']
    assert djk.get_shortest_path('B', 'C') == ['B', 'C']
    assert djk.get_shortest_path('B', 'D') == ['B', 'D']
    assert djk.get_shortest_path('B', 'E') == ['B', 'D', 'E']
    assert djk.get_shortest_path('B', 'F') == ['B', 'D', 'E', 'F']

    assert djk.get_shortest_path('C', 'A') == ['C', 'D', 'E', 'A']
    assert djk.get_shortest_path('C', 'B') == ['C', 'D', 'E', 'B']
    assert djk.get_shortest_path('C', 'D') == ['C', 'D']
    assert djk.get_shortest_path('C', 'E') == ['C', 'D', 'E']
    assert djk.get_shortest_path('C', 'F') == ['C', 'D', 'E', 'F']

    assert djk.get_shortest_path('D', 'A') == ['D', 'E', 'A']
    assert djk.get_shortest_path('D', 'B') == ['D', 'E', 'B']
    assert djk.get_shortest_path('D', 'C') == ['D', 'E', 'A', 'C']
    assert djk.get_shortest_path('D', 'E') == ['D', 'E']
    assert djk.get_shortest_path('D', 'F') == ['D', 'E', 'F']

    assert djk.get_shortest_path('E', 'A') == ['E', 'A']
    assert djk.get_shortest_path('E', 'B') == ['E', 'B']
    assert djk.get_shortest_path('E', 'C') == ['E', 'A', 'C']
    assert djk.get_shortest_path('E', 'D') == ['E', 'B', 'D']
    assert djk.get_shortest_path('E', 'F') == ['E', 'F']

    assert djk.get_shortest_path('F', 'A') == []
    assert djk.get_shortest_path('F', 'B') == []
    assert djk.get_shortest_path('F', 'C') == []
    assert djk.get_shortest_path('F', 'D') == []
    assert djk.get_shortest_path('F', 'E') == []