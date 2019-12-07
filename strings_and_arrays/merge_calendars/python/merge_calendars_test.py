from merge_calendars import merge_calendars

def test_merges_two_meeting_calendar():
    calendar = [[1, 4], [3, 7]]
    assert merge_calendars(calendar) == [[1, 7]]

def test_merges_large_meeting_set():
    calendar = [[1, 6], [7, 9], [3, 4], [2, 6]]
    assert merge_calendars(calendar) == [[1, 6], [7, 9]]

def test_returns_empty_list():
    calendar = []
    assert merge_calendars(calendar) == []

def test_returns_meeting_passed_only_one():
    calendar = [[1, 5]]
    assert merge_calendars(calendar) == calendar
