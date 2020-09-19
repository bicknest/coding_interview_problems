## Approach

Iterate through the array keeping track of all the "potential" additives that will get us to the target in some hashable data structure.

While iterating check the hashable data structure to see if the current number in the array you are at is in it.

If it is, return the index that you stored in the hashable data structure, as well as the current index you are at.

The time complexity of this should be O(n) because you only have to iterate through the array at most once.

The space complexity of this method is O(n) because you have to create a new data structure to hold all the hased indices.
