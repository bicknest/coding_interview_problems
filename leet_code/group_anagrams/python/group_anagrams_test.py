from group_anagrams import group_anagrams

def test_some_anagrams():
    strings = ["tea", "ate", "nat", "tan", "bat"]
    grouped = [['tea', 'ate'], ['nat', 'tan'], ['bat']]
    assert group_anagrams(strings) == grouped

def test_edge_case_empty_string():
    strings = [""]
    grouped = [[""]]
    assert group_anagrams(strings) == grouped

def test_edge_case_two_empty_strings():
    strings = ["", ""]
    grouped = [["", ""]]
    assert group_anagrams(strings) == grouped
