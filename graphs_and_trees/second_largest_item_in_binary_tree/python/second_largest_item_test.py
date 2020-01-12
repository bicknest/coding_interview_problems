from second_largest_item import find_second_largest

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def test_not_two_nodes():
    root_node = Node(10, None, None)
    assert find_second_largest(root_node) == "Tree must have two nodes"


def tests_return_with_two_nodes():
    root_node = Node(10)
    root_node.right = Node(15)
    assert find_second_largest(root_node) == 10

def tests_return_with_one_left_node():
    root_node = Node(10)
    root_node.left = Node(3)
    assert find_second_largest(root_node) == 3

def tests_with_big_right_tree():
    root_node = Node(10)
    root_node.right = Node(12)
    root_node.right.right = Node(15)
    root_node.right.right.right = Node(17)
    assert find_second_largest(root_node) == 15

def tests_with_a_left_and_big_right_tree():
    root_node = Node(100)
    root_node.left = Node(10)
    root_node.left.right = Node(15)
    root_node.left.right.right = Node(19)
    assert find_second_largest(root_node) == 19
