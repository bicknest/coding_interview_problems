from zig_zag_conversion import convert

def test_zig_zag_conversion():
    msg = "PAYPALISHIRING"
    num_rows = 3
    converted_string = convert(msg, num_rows)
    assert len(converted_string) == len(msg)
    assert converted_string == "PAHNAPLSIIGYIR"

def test_zig_zag_conversion_one_row():
    msg = "AB"
    num_rows = 1
    converted_string = convert(msg, num_rows)
    assert len(converted_string) == len(msg)
    assert converted_string == msg
