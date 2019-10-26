# Approach

Can do this one in O(n) time compexity and in place, so with O(1) space complexity. (sort of)

**NOTE that in javascript Strings are immutable, so you will have to create at least one array size n**
**Alternatively if your function takes an array of chars that make up your sentence as an input you can do this**


First reverse the whole string in place, then iterate through each word (broken up by spaces)
and reverse the words.

Reversing the string in place takes O(n)

Even though we may end up with a loop inside
a loop, it's possible to reason that iterating through and reversing each word
can only possibly take up to O(n). Each nested loop will only loop through a subset
of the original set size n. Thinking carefully, we can see that all of these subsets of n
will actually add up to n itself. So the whole loop will take O(n)

Overall O(n) + O(n) = O(n) time complexity

If we do all the reversing "in place" we get O(1) additional space complexity
