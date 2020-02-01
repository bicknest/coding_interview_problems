# Approach

In your new class, keep track of two stacks. One of the stacks will hold all of the data, the other stack will hold all the maxima.

Update the push, pop methods, so that we only push to the maxStack if the peek of current maxStack is less than the item we are pushing.
Only pop from maxStack if the item that gets popped is equal to the peek of maxStack.

Because of the push/pop nature of the stack, this will always make sure that maxStack holds the maxima that we actually care about.
