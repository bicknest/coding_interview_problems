#Approach

A naive and incorrect solution that may first come to mind would be to traverse the right side of the tree at every point and find the parent
of the largest node. This solution does not cover the case where the second largest node is a left child of the largest node.

The correct approach is to traverse the right-side of the tree, then break the problem up into two pieces.

First: if you are at a node that has no left child, and no right grandchild, (i.e. currentNode.right.right) then you must be at the second largest node
Second: if you are at the largest node (no right child, when traversing the tree), but has a left child, then find the largest child of the tree on the left

So write a function to find the largest node in a tree (easy)
Then write a function that traverses the right side of the tree, checking each node for the cases above. If the first case, return the node value, if the second case, call the findLargest function on the node

The time complexity is one walk down the height of the tree O(h) in worst-case. If the tree is well balanced, it is will be ~O(lg(n))
The space complexity is O(1), don't need to store any thing other than a couple variables.
