from decode_ways import decode_ways


def test_easy_case():
    s = "12"
    assert decode_ways(s) == 2


def test_harder_case():
    s = "226"
    assert decode_ways(s) == 3


def test_zero_case():
    s = "0"
    assert decode_ways(s) == 0


def test_non_case():
    s = ""
    assert decode_ways(s) == 0
