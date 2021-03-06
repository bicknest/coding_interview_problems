from k_most_frequent_words import k_most_frequent_words, k_most_frequent_words_efficient


def test_something_easy():
    words = ["blah", "blah", "blah", "b"]
    k = 1

    assert k_most_frequent_words(words, k) == ["blah"]


def test_something_harder():
    words = ["lol", "lassie", "lol", "bah", "boo", "bob", "boo", "lassie"]
    k = 2

    assert k_most_frequent_words(words, k) == ["boo", "lassie"]


def test_k_is_equal_to_unique_words():

    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4

    assert k_most_frequent_words(words, k) == ["the", "is", "sunny", "day"]

def test_something_easy_efficient():
    words = ["blah", "blah", "blah", "b"]
    k = 1

    assert k_most_frequent_words_efficient(words, k) == ["blah"]


def test_something_harder_efficient():
    words = ["lol", "lassie", "lol", "bah", "boo", "bob", "boo", "lassie"]
    k = 2

    assert k_most_frequent_words_efficient(words, k) == ["boo", "lassie"]


def test_k_is_equal_to_unique_words_efficient():

    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4

    assert k_most_frequent_words_efficient(words, k) == ["the", "is", "sunny", "day"]
