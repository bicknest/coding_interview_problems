def merge_intervals(intervals):
    if len(intervals) < 1:
        return []

    intervals.sort(key=lambda x: x[0])

    new_intervals = []
    min_start, max_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= max_end:
            max_end = max(max_end, end)
        else:
            new_intervals.append([min_start, max_end])
            min_start = start
            max_end = end


    new_intervals.append([min_start, max_end])

    return new_intervals
