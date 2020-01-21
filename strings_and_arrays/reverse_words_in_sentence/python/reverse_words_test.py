from reverse_words import reverse_words_and_sentence, reverse_in_place

def test_if_word_is_reversed():
    word = ["a", "r", "r", "a", "y"]
    reversed_word = ["y", "a", "r", "r", "a"]
    reverse_in_place(word, 0, len(word) - 1)
    assert word == reversed_word

def test_reverses_one_char_array():
    word = ["a"]
    reversed_word = ["a"]
    reverse_in_place(word, 0, 0)
    assert word == reversed_word

def tests_reverses_sentence():
    sentence = "We had a fun time at the park"
    answer = "park the at time fun a had We"
    reversed_sentence = reverse_words_and_sentence(sentence)
    assert reversed_sentence == answer
