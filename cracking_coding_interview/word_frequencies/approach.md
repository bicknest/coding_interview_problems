# Approach

First strip the string of all punctuation.

Second, chunk the string out into words by splitting on the spaces.

Then decide how you want to deal with capitalization. I set everything to lowercase to make sure we count Bingo and bingo as the same word

* Note: some people may decide that Set and set are two different words, justify the choice you make and try not to make things to complicated.

Create a data structure (I would use Set in JS and Counter in Python) that allows for a key (word) and value (count number)
Make a pass over your prepared array/list of words and count the instances that are the same. The approach will differ depending on language.

Python has a built-in data structure in collections.Counter that will give quite an elegant solution.

With JS I would use a Map and check if there exists a word in the map already, add with count of zero if not, up the coutn if it does
