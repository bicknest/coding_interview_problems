# Approach

Use a greedy approach to solve this problem in one pass of the array. Product of three makes things tricky for the greedy approach though, because you will have to store a few things on each iteration:

-the minimum number you have seen
-the maximum number you have seen
-the minimum product of two you have seen
-the maximum product of two you have seen
-the maximum product of three you have seen

Figure out the above with the first three elements of the array, then iterate over the rest of the array updating the above values at each iteration. After you have iterated over the array, the maximum product of three will be your answer

This algorithm will take O(n) time complexity and O(5) space complexity
