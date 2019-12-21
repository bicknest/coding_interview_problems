from word_frequencies import count_word_frequencies

def test_book_with_same_word_three_times():
    book = 'bingo bingo bingo'
    freq_dict = count_word_frequencies(book)
    assert freq_dict['bingo'] == 3

def test_book_with_punctuation():
    book = 'bingo, bingo: bingo.'
    freq_dict = count_word_frequencies(book)
    assert freq_dict['bingo'] == 3

def test_book_with_capitalization():
    book = "Bingo, bingo: album."
    freq_dict = count_word_frequencies(book)
    assert freq_dict["bingo"] == 2
    assert freq_dict["album"] == 1
