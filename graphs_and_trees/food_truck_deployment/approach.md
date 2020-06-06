# Approach

This problem is essentially a graph BFS problem with a few extra complications and things to think about:
    - Can we solve the problem without searching the whole graph? If so, what are the tradeoffs/how much preformance improvement do you get?
    - How will we keep track of and define parks?
    - How do we want to represent the graph? Convert to Adjacency list? Keep as is and write some helper functions to generate our neighbor list on each iteration of BFS?
        - https://mathworld.wolfram.com/GridGraph.html


One approach to this problem would be:
    - iterate over the entire grid of the city (N x M), and build a set of all blocks that we should visit
        - we know that we need to visit every park block to understand how many parks there are in the city
        - creating the set of all park blocks will help us keep track later of which park blocks we've visited and which park blocks are left to visit
        - it will also supply us with starting points to start our BFSes
    - now that we know all of the blocks we must visit
        - start at arbitrary block from our park blocks set we have created
        - remove this block from the park block set
        - BFS from this block, stopping the search when reaching a commercial block, and removing any park blocks you visit from the park blocks to visit set
        - once the BFS is exhausted for that particular park block that you started at, increment a counter
        - start another BFS from the next arbitrary park block from your park block to visit set
        - stop and return the counter, once you have removed every park block from the park block to visit set

O(N x M) + O(K + E)

where k = (N x M) and E = 2MN - M - N

So O(N x M) + O(N x M) + O(N x M) = O(N x M)


Handling graph representation:
    - based on this site: https://www.redblobgames.com/pathfinding/grids/graphs.html it seems that the way to go for
        representing grid graphs would be to keep it as just the list of vertices and then generate the possible neighbors on
        each iteration with a helper function
