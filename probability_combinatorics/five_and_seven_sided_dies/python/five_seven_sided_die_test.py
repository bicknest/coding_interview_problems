from five_seven_sided_die import rand7

def tests_a_few_rolls():
    roll1 = rand7()
    roll2 = rand7()
    roll3 = rand7()
    assert 0 < roll1 < 8
    assert 0 < roll2 < 8
    assert 0 < roll3 < 8
