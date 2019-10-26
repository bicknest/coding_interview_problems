#Problem Definition

You are trying to figure out all the available times that you and another person have to meet.
You have a single array of meeting objects, each which has a startTime and endTime.
The endTime and startTime are integers that indicate 30 minute blocks past 9:00 am the earliest time for a meeting.
You need to write a program to merge all the meetings to figure out availability.
If meetings touch, then they need to be merged.

Input: an array of unsorted meeting objects: [{startTime: 1, endTime, 3}, {startTime, 8, endTime: 9}, {startTime: 4, endTime: 6}]

Output: one array with objects of the same shape
