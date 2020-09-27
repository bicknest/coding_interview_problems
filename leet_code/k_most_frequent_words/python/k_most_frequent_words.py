from collections import Counter

def k_most_frequent_words(words, k):
    word_counts = list(Counter(words).items())
    word_counts.sort(key=lambda x: x[1])
    word_counts.reverse()
    prev_count = 0
    sort_count_list = []
    final_words = []
    for word, count in word_counts:
        if count == prev_count:
            sort_count_list.append(word)
        else:
            sort_count_list.sort()
            final_words.extend(sort_count_list)
            sort_count_list = [word]
            prev_count = count

    sort_count_list.sort()
    final_words.extend(sort_count_list)

    return final_words[:k]


def k_most_frequent_words_efficient(words, k):
    count = Counter(words)
    candidates = list(count.keys())
    candidates.sort(key = lambda w: (-count[w], w))
    return candidates[:k]
