def pair_of_sums(pairs, target_sum):
    potential_additives = {target_sum - x for x in pairs}
    pairs_set = set(pairs)
    return potential_additives & pairs_set
