#Approach

Sort the two calendars by their start dates
O(nlgn)
O(1) extra space

Traverse the sorted intervals starting from first interval and check:
    a) If the current meeting overlaps with the previous interval, take the max of the two ends
    and the mins of the starts and set that as the new start and end dates. Do not update your index pointer
    b) If no overlap add the current meeting you to the array and update your new index pointer

O(n) and O(1) extra space (merging the calendar in space

Overall this solution Is O(nlgn) time complexity and O(1) space complexity.

There is another solution where we would not have to keep track of an extra pointer but would have to push
all of our merged meetings to a new stack. This would take O(n) worst-case in extra space.
