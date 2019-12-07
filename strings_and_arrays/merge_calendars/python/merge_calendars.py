# Merge two calendars

# Input is a list of tuples where the first item in tuple is start time and second item is end time

def merge_calendars(calendar):

    if len(calendar) < 2:
        return calendar

    def sort_calendar(event):
        return event[0]

    calendar.sort(key=sort_calendar)

    update_index = 0

    for i in range(1, len(calendar)):
        if calendar[update_index][1] >= calendar[i][0]:

            calendar[update_index][1] = max(calendar[update_index][1], calendar[i][1]) 

            calendar[update_index][0] = min(calendar[update_index][0], calendar[i][0])

        else:
            calendar[update_index + 1] = calendar[i]
            update_index += 1

    length_diff = len(calendar) - update_index
    for i in range(1, length_diff):
        calendar.pop()
    
    return calendar
