# Approach

Using dynamic programming this problem can be broken down into sub problems.

If we have all the permutations of "dog", how would we get all the permuations of "dogs".

We would just put the "s" in each possible position for each permutation of "dog".

Then find a base case to break on



SO:

Break on a string that is only one character long, and return a set with that string in it. Can't permutate that.

Next split the string two pieces, the last character and all the characters but the last.

Make a recursive call to your function with all the characters except last and assign that to a variable.

Next create a new set that will hold the permutations

Then loop over your all characters but last permutation set and insert the last char into each possible position using slice and concatentation
Add each of those created words to your permuatation set

Once the loop is finished, return the permutations so that the next function on call stack has it to iterate over and change all permutations


The run time of this algorithm will be O(n^2) as there will be n function calls and up to n loops over each function call.
