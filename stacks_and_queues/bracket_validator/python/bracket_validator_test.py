from bracket_validator import is_code_valid

def test_a_simple_code_input():
    code = "functionCall()"
    assert is_code_valid(code) is True

def test_a_simple_false_input():
    code = "functionCall("
    assert is_code_valid(code) is False

def test_some_nested_brackets():
    code = "functionCall({payload: {object}}[{[data and cool code]}])"
    assert is_code_valid(code) is True

def test_return_false_with_wrong_nested():
    code = "functionCall({payload: }})[]"
    assert is_code_valid(code) is False

    def test_return_false_not_enough_openers():
        code = "functionCall()))))";
        assert is_code_valid(code) is False
