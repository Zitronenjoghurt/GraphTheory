from src.classes.tree import Tree

def test_init():
    tree = Tree('A')
    assert tree.get_root().get_name() == 'A'
    assert tree.get_node_names() == ['A']
    assert tree.get_edges() == []

def test_add_child():
    tree = Tree('A')

    assert tree.add_child('B', 'A') == True
    assert tree.add_child('B', 'A') == False

    assert tree.add_child('C', 'B') == True
    assert tree.add_child('C', 'B') == False

    assert tree.add_child('A', 'B') == False
    assert tree.add_child('A', 'C') == False
    assert tree.add_child('B', 'C') == False