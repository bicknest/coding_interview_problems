from decode_string import decode_string

def test_an_easy_string():
    s = "3[a]2[bc]"
    output = "aaabcbc"
    decoded = decode_string(s)
    assert decoded == output

def test_nested_encoding():
    s = "3[a2[c]]"
    output = "accaccacc"
    assert output == decode_string(s)

def test_harder_string():
    s = "2[abc]3[cd]ef"
    output = "abcabccdcdcdef"
    assert output == decode_string(s)

def test_final_string():
    s = "abc13[cd]xyz"
    output = "abccdcdcdcdcdcdcdcdcdcdcdcdcdxyz"
    assert output == decode_string(s)
