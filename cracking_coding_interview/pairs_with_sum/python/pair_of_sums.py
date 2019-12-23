def pair_of_sums(pairs, target_sum):
    potential_addends = {target_sum - x for x in pairs}
    pairs_set = set(pairs)
    return potential_addends & pairs_set
