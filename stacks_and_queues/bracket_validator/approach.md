# Approach

Iterate through the string making sure that:
1. each closer corresponds to the most recently seen, unclosed opener
2. every opener and closer is a pair

Use a stack to keep track of the most recently seen unclosed opener. If the stack is ever empty when we come to a closer we know the closer doesn't have an opener.

So as we iterate:

If we see an opener, push it onto the stack
If we see a closer, we check to see if it is the closer for the opener at the top of the stack
If it is we pop from the stack, if it isn't or if the stack is empty we return false

This will take O(n) time complexity, where n is the number of chars in the string.
This will also take O(n) space complexity, as in worst case we would need to push all the chars onto a stack
