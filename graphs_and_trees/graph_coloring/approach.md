# Approach

First off: is it always possible to find a legal coloring with D + 1 colors?
Each node has at most D neighbors and we have D + 1 colors. So, if we look at any node, there's always
at least one color that's not take by it's neighbors

So yes, D + 1 is always enough colors for a legal coloring

Brute force approach would be to just try every single combination of coloring AND THEN CHECK all M edges to see if that's
a valid coloring. This would require O (M * D^N) which is exponential time: terrible

Try to color more efficiently:

Instead of assigning the colors all at once (like in brute force) try coloring the nodes one by one. Assign a color to the first node, then find a legal
color for the second node, then third node, and keep going through a BFS

Keep track of illegalColors in a set

for each node, iterate through the neighbors and add the colors of neighbors to the illegalColor set

then for each color that we have been given check to see if it is in illegalColors
if it is not, then add it to a legal color array that we are keeping track of

after building up an array of legal colors assign this node's color the first element of legal color array


If we implement the algorithm like this, then what is the runtime?
We're iterating through each node in the graph, O(N) and in each iteration of the loop
we are iterating through neighbors which is O(D) and we iterate through array of colors which is O(D + 1)
Overall this is O(N * (D + D + 1)) which is just O(N * D)

There is actually a way of bringing this down to linear time, by not looking at every color on each iteration

Add a break to the loop iterating over your colors as soon as you find a color that is not in the illegalColor set.

If this is added then we'll try at most illegalColors.size + 1 colors in total. That's how many we'd need if we happen to test all the colors in illegalColors first, before finally testing the legal color last

illegal colors is at most the size of neighbors the node has
Each of our M edges of the graph adds a total of two neighbors to the whole loop
2 * M illegal colors in total
So now over the whole loop we are trying 2 * M + N

Add thtat to the O(M) of illegalColor gathering and we are at O(M + N), linear time

