Using dynamic programming there are multiple ways to solve this problem:

1. Recursive with memoization
2. Solve it bottom up 


2.

Start with the base case that there's one way to create the amount zero, and progressively add to each of our denominations

The numbers of new ways we can make a higherAmount when we account for a new coin is simply waysOfDoingNCents[higherAmount - coin], where we know
that the value already includes combinations involving coin (because we went bottom up, we know smaller versions have already been calculated)
