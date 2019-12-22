from collections import Counter
import string

PUNCTUATION_SET = set(string.punctuation)

def count_word_frequencies(book):
    book = "".join(ch for ch in book if ch not in PUNCTUATION_SET)
    word_list = book.split(" ")
    word_list = [word.lower() for word in word_list]
    word_freq_dict = Counter(word_list)
    return word_freq_dict
