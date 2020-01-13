class NodeAndBounds(object):
    def __init__(self, node, upper_bound, lower_bound):
        self.node = node
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

def is_binary_search_tree(tree_root):
    if not tree_root or not tree_root.value:
        return "Tree root needs a value"

    node_stack = []
    node_stack.append(NodeAndBounds(tree_root, float("inf"), float("-inf")))

    while len(node_stack) != 0:
        node_bounds = node_stack.pop()
        node = node_bounds.node
        upper_bound = node_bounds.upper_bound
        lower_bound = node_bounds.lower_bound
        if (node and node.value >= upper_bound) or (node and node.value <= lower_bound):
            return False

        if node and node.right:
            node_stack.append(
                NodeAndBounds(node.right, upper_bound, node.value)
            )
        if node and node.left:
            node_stack.append(
                NodeAndBounds(node.right, node.value, lower_bound)
            )

    return True
