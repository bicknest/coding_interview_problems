from vector import Vector

def test_print_vector():
    v = Vector(3, 4)
    assert repr(v) == 'Vector(3, 4)'

def test_add_vector():
    v1 = Vector(1, 1)
    v2 = Vector(2, 2)
    v = v1 + v2
    v_expect = Vector(3, 3)
    assert repr(v) == repr(v_expect)

def test_multiply_vector_by_scalar():
    v1 = Vector(1, 3)
    v = v1 * 3
    v_expect = Vector(3, 9)
    assert repr(v) == repr(v_expect)

def test_get_vector_magnitude():
    v1 = Vector(3, 4)
    assert abs(v1) == 5.0
