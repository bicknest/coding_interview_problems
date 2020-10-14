from word_break import word_break


def test_word_break():
    s = "leetcode"
    word_dict = ["leet", "code"]
    assert word_break(s, word_dict) is True


def test_word_break_apple():
    s = "applepenapple"
    word_dict = ["apple", "pen"]
    assert word_break(s, word_dict) is True


def test_word_break_false():
    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    assert word_break(s, word_dict) is False
