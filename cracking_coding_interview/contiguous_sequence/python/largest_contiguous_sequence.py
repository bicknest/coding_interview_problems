def largest_contiguous_sequence(sequence):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, len(sequence)):
        max_ending_here += sequence[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far
