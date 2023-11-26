from src.classes.tree import Tree

def test_init():
    tree = Tree('A')
    assert tree.get_root().get_name() == 'A'
    assert tree.get_node_names() == ['A']
    assert tree.get_edges() == []

def test_add_node():
    tree = Tree('A')

    assert tree.add_node('A', 'B') == True
    assert tree.add_node('A', 'B') == False

    assert tree.add_node('B', 'C') == True
    assert tree.add_node('B', 'C') == False

    assert tree.add_node('B', 'A') == False
    assert tree.add_node('C', 'A') == False
    assert tree.add_node('C', 'B') == False