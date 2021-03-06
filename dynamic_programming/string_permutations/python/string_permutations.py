def get_permutations(string):
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    all_chars_except_last_permutations = get_permutations(all_chars_except_last)

    permutations = set()

    # each perm should be of length
    for perm in all_chars_except_last_permutations:
        for position in range(len(all_chars_except_last) + 1):
            permutation = perm[:position] + last_char + perm[position:]
            permutations.add(permutation)

    return permutations
