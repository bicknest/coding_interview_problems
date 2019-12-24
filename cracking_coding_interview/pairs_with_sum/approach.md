# Approach

Fairly easy solution for this one.

Can do a pass over the pairs and create a set of all the addends that will add up to the sum.

If you are a optimizing for time, use a data structure to store the addends that is a hash mapping. This allows for quick look up rather than having to traverse the whole list/array to see if something exsits.

Once you have a set of the potential addends, then find the intersection between your pairs set and the set of potential addends.

This will take O(n) where n is the size of pairs for creating the set of addends.

It will take another O(n) to pass over the pairs array and look up from the hash table.

** Note: If you use a list or array instead of hash table, you will save a lot on space complexity as hash tables are space intensive, but if you use this same implementation your time complexity will be at worst O(n^2)

O(n) + O(n) = O(n)


# TODO:

Add an implementation that just traverses the array once, using a greedy approach.
