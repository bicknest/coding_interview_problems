#Approach


First to solve the problem we need to have a working definition for what a binary search tree is:

A binary search is a node-based binary tree data structure that has the following properties:

-The left subtree of a node contains only nodes with keys lesser than the node's keys
-The right subtree of a node contains only nodes with keys larger than the node's keys
-The left and right subtree each must also be a binary search tree

Knowing what a binary search tree is we can now present some solutions

Iterative Approach:

It is apparent that we will have to traverse the entire tree and check each node to understand if it is a proper Binary Search Tree

Because we know this, we know we should search or traverse the entire tree

Here we will use a depth first search approach, which will allow us to use a stack for storing the nodes we need to check

In addition to searching the tree we also have to make sure it is a BST.
To accomplsh this, with each node we store, we should store an associated upper bound and lower bound to indicate the range we know the node's value must be in.

The algorithm will essentially look like this:

-create a nodeStack that we will be pushing our nodes and corresponding upper/lower bounds to
-push the treeRoot onto that stack, along with max number upper bound and min number lower bound. represent this information as an object {node: currentNode, upperBound: infinity, lowerBound: negInfinity}
-while(nodeStack) has a length
    -pop an object off the node stack
    -check to see if the value at this node stack is below/above your upper/lower bounds, return false if it is
    -o/w if node has a right child, push that node onto the nodeStack with an update lowerBound as the parents node value
    -if node has a left child, push that node onto the nodeStack with an updated upperBound as the parent's node value

-if the while loop completes without ever returning a negative value return true

Complexity:

As noted above we will have to traverse the entire tree, so time complexity will be O(n).

Space complexity should be O(n/2) -> O(n)

NOTE: think about how using BFS instead of DFS would change complexity.
