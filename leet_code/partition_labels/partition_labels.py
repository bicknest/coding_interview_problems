def partition_labels(s):

    # build a letter map
    letter_map = dict()
    for i in range(len(s)):
        char = s[i]
        if letter_map.get(char) is None:
            letter_map[char] = (i, i)
        else:
            start, end = letter_map[char]
            letter_map[char] = (start, i)

    """
    NOTE: here if using a dict that guarantees to retain insertion order
    then this sort is not needed
    (ASIDE: this is true in python 3 and on. somehow when commenting out the sort in my leetcode submission the execution got slower though????)
    """
    partition_end = 0
    partition_start = 0
    partition_lengths = []
    sorted_letter_ranges = list(letter_map.items())
    sorted_letter_ranges.sort(key=lambda x: x[1][0])
    for letter, r in sorted_letter_ranges:
        start, end = r
        if start > partition_end:
            partition_lengths.append(partition_end - partition_start + 1)
            partition_start = start
            partition_end = end
        else:
            partition_end = max(end, partition_end)

    partition_lengths.append(partition_end - partition_start + 1)

    return partition_lengths
