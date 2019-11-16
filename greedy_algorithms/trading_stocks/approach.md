#Approach

This problem can be solved with one pass over the array (O(n) time) with a greedy approach.
Iterate over each price, while keeping track of the minimum price. Also keep track of the biggest difference between lowest price and each price as you iterate.

This algorithm will run in O(n) time (one loop over the array) and with O(2) constant space complexity (you only have to keep track of 2 new variables)
