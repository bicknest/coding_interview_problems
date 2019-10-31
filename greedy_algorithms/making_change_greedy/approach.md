#Approach

This problem can be solved with the greedy approach. Greedily check the highest denomination first
and iterate through all denominations with the remainder from the previous coin. Bonus: figure out why this works
with a greedy approach? What if we change the denominations to 1, 10, 25?


Create a list of denominations in ascending order.
Iterate through that list, dividing the total number of cents by the denomination, adding that
to a running total, then changing the total number of cents to what is left over.

This algorithm will run in O(4) (loop through the 4 denominations) which is constant time, and O(4) which is constant space.
