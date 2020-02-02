from max_stack import MaxStack

def test_should_easily_keep_track_of_pushing():
    my_max_stack = MaxStack()
    my_max_stack.push(1)
    my_max_stack.push(2)
    my_max_stack.push(3)
    assert my_max_stack.get_max() is 3

def test_should_keep_track_of_descending_stack_pushing():
    my_max_stack = MaxStack()
    my_max_stack.push(3)
    my_max_stack.push(2)
    my_max_stack.push(1)
    assert my_max_stack.get_max() is 3

def test_should_keep_track_of_some_pushing_and_popping():
    my_max_stack = MaxStack()
    should_be_none = my_max_stack.pop()
    my_max_stack.push(3)
    my_max_stack.push(19)
    my_max_stack.pop()
    my_max_stack.push(4)
    my_max_stack.push(2)
    my_max_stack.pop()
    assert my_max_stack.get_max() is 4
    assert should_be_none is None
