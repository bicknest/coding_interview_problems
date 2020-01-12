def find_largest(root):
    if root.right:
        return find_largest(root.right)
    return root.value


def find_second_largest(root_node):
    if (not root_node or (not root_node.left and not root_node.right)):
        return "Tree must have two nodes"

    current = root_node

    while current:
        if current.left and not current.right:
            return find_largest(current.left)

        if current.right and not current.left and not current.right.right:
            return current.value

        current = current.right
