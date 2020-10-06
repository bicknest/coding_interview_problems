## Burst Balloons

Hard problem:

If we try to brute force this solution, we would try to findd every possible order the balloons could be burst.
At each step we burst one balloon, the number of possibilites would be (N) * (N-1) * (N -2)... giving us time complexity of O(N!)

We can make a small improvement to this by caching the set of existing balloons. Since each balloon can be burst or not burst, and we are incurring extra time creating a set of balloons
each time, we are still looking at a solution worse than O(2^N)

Two techniques to use to optimize the solution:
1. Divide and Conquer
    - after bursting balloon i, we can divide the problem into the baloons to the left of i (nums[0:i]) and to the right of i nums[i+1:])
    - to find the optimal solution we check every optimal solution after bursting each balloon
    - since we will find the optimal solution for every range in nums, and we burst every balloon in every range to find the optimal solution, we have an O(N^2) x O(N)  O(N^3) solution
    - however if we try to divide our problem in the order where we burst balloons first, we are unable to keep track of what balloons the endpoints of our intervals are adjacent to

2. Working Backwards
    - Above we start with all the balloons and try to burst them. This causes adjacency issues. Instead we can start with no balloons and add them in reverse order of how they were popped.
    - Each time add a balloon, we can divide and conquer on its left and right sides, letting us add new balloons in between.

    - this gets rid of adjacency issues. For the left interval, we know the left boundary stays the same, and we know that our right boundary is the element we just added. The opposite goes for the right interval. Compute coins added easily by nums[left] * nums[i] * nums[right].




Algorithm:

- to deal with edges of array can reframe the problem into only bursting the non-edge balloons and adding ones on the sides
- define a function dp to return the maximum number of coins obtainable on the open interval (left, right)
- base case is if there are no integers left + 1 == right
- we add each balloon on the interval, divide and conquer the left and right sides, and find maximum score
- the best score after adding the ith baloon is given by:
nums[left] * nums[i] nums[right] + dp(left, i) + dp(i, right)
