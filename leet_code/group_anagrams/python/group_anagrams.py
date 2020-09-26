from collections import Counter

def group_anagrams(strs):
    anagrams = dict()
    for string in strs:
        hashable_char_count = tuple(sorted(Counter(string).elements()))
        if anagrams.get(hashable_char_count) is None:
            anagrams[hashable_char_count] = [string]
        else:
            anagrams[hashable_char_count].append(string)

    return [x[1] for x in anagrams.items()]
