* Approach

First we should do a BFS of the graph from sender and stop once we find the recipient.

Because we need to reconstruct the path that we took to get to the recipient, we are going to keep track of
how we reached each node.

Then with the object we have created that holds all the ways we reached each node, we will backtrack from recipient to sender
and construct the shortest path.


* Complexity

Time complexity of BFS is O (N + M), backtracking is another O(N), so overall O(N)

Space complexity: the queue of nodes to visit, the mapping of nodes to previous nodes, and the final path...all store constant amount of info per node ergo O(N)

Learnings:
The tricky part was the backtracking to assemble the path we used to reach our endNode. In general it's helpful to think of backtracking as two steps:
1. Figuring out what additional information we need to store in order to rebuild our path at the end (howWeReachedNodes)
2. Figuring out how to reconstruct the path from that information
