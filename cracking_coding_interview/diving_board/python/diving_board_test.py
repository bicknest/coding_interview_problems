from diving_board import generate_diving_board_lengths

def test_simple_case():
    shorter = 2
    longer = 4
    length_set = set([shorter, longer])
    assert generate_diving_board_lengths(1, shorter, longer) == length_set

def test_with_k_at_two():
    shorter = 2
    longer = 4
    length_set = set([shorter + longer, shorter + shorter, longer + longer])
    assert generate_diving_board_lengths(2, shorter, longer) == length_set

def test_with_k_at_three():
    shorter = 2
    longer = 4
    length_set = set([shorter + shorter + shorter, longer + longer + longer, shorter + shorter + longer, longer + longer + shorter])
