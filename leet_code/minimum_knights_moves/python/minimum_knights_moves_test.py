from minimum_knights_moves import minimum_knights_moves

def test_a_single_move():
    assert minimum_knights_moves(2, 1) == 1

def test_a_few_moves():
    assert minimum_knights_moves(5, 5) == 4
