# Approach

This is a classic problem. The naive approach may be to try and figure out some sort of weight -> value ratio and pack your knapsack with as many
with the highest ratio till they don't fit, then second highest and so on. This solution doesn't always output the optimal solution.

So...

Use dynamic programming and "brute force" it.

Starting at 1, calculate the max value you can fit in the bag for that capacity
Then as you up the capacity, calculate the new max value you can fit in the bag.
Do this by using previous max value you have stored and figuring out what extra items you can try and fit in the bag using the new capacity.

Once you have built an array that has all the values stored in it for each capacity, grab the value at [capacity] and return it.

You will have a nested loop that iterates over all the items in you array (M), for every integer from 1...capacity (N), therefore your time complexity will be O(N * M)

The solution given here creates an array that stores all the values, so it's space complexity is O(N).

A more complicated solution might be able to get you only storing the maximum weight of an item, (you only have to remember up to that far back in capacity), so if that number is less than N you could do it in that much less space complexity.
