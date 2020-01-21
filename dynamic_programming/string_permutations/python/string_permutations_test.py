from string_permutations import get_permutations

def test_simple_string():
    simple_string = 'ab'
    expected_set = set(['ab', 'ba'])
    assert get_permutations(simple_string) == expected_set

def test_a_string_with_three_letters():
    three_string = 'abc'
    expected_set = set(['abc', 'bac', 'cab', 'cba', 'bca', 'acb'])
    assert get_permutations(three_string) == expected_set

def test_a_dupe_string():
    dupe_string = 'aab'
    expected_set = set(['aab', 'aba', 'baa'])
