from collections import Counter
import string

PUNCTUATION_SET = set(string.punctuation)

def count_word_frequencies(book):
    # strip the punctuation
    book = "".join(ch for ch in book if ch not in PUNCTUATION_SET)
    # create a list of words from the long string
    word_list = book.split(" ")
    # handle case issues
    word_list = [word.lower() for word in word_list]
    # create a dict with the counts
    word_freq_dict = Counter(word_list)
    return word_freq_dict
