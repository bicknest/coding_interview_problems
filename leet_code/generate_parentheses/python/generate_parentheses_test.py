from generate_parentheses import generate_parentheses

def test_generate_three():
    three_formed_set = ['()()()', '()(())', '((()))', '(()())', '(())()']
    assert sorted(generate_parentheses(3)) == sorted(three_formed_set)

def test_generate_four():
    four_formed_set = ['(((())))', '(()())()', '()(())()', '(())(())', '()(()())', '()()()()', '(()()())', '((()()))', '(())()()', '(()(()))', '((()))()', '((())())', '()((()))', '()()(())']
    assert sorted(generate_parentheses(4)) == sorted(four_formed_set)

def test_generate_edge():
    assert generate_parentheses(0) == [""]
