from is_binary_search_tree import is_binary_search_tree

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def test_not_value_in_parent_node():
    root_node = Node(None, None, None)
    assert is_binary_search_tree(root_node) == "Tree root needs a value"

def test_with_two_items():
    root_node = Node(10)
    root_node.right = Node(15)
    assert is_binary_search_tree(root_node) == True

def test_true_with_one_left_node():
    root_node = Node(10)
    root_node.left = Node(3)
    assert is_binary_search_tree(root_node) == True

def test_true_with_big_right_tree():
    root_node = Node(10)
    root_node.right = Node(12)
    root_node.right.right = Node(15)
    root_node.right.right.irght = Node(17)
    assert is_binary_search_tree(root_node) == True

def test_true_with_interesting_structure():
    root_node = Node(100)
    root_node.left = Node(10)
    root_node.left.right = Node(15)
    root_node.left.right.right = Node(19)
    assert is_binary_search_tree(root_node) == True

def test_false_with_wrong_structure():
    root_node = Node(100)
    root_node.left = Node(150)
    root_node.right = Node(80)
    assert is_binary_search_tree(root_node) == False

