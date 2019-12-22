def generate_diving_board_lengths(k, shorter, longer):
    set_of_lengths = set()
    for i in range(0, k + 1):
        length_to_add = (shorter * i) + (longer * (k - i))
        set_of_lengths.add(length_to_add)
    return set_of_lengths

