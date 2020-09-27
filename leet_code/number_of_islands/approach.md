## Approach

Loop through each element in the 2d array. Once you get to a 1, do a bfs, on all squares that are 1s. Once you travel to a square, add it to the set.

When a BFS is exhuasted, increment a counter.

Keep looping through the 2d array, stopping at the next 1 that is not in the set.



BFS goes like this:

create a 2d visited array
create a queue

add the first to the frontier of things to search:

while frontier exists:
    pop from frontier
    generate the neighbors of that frontier
    for each neighbor
        if you haven't visited them
            append it to frontier
            now set it to one you have visited
