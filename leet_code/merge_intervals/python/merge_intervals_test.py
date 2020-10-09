from merge_intervals import merge_intervals

def test_merging_some_intervals():
    intervals = [[1,3],[2,6],[8,10],[15,18]] 
    output = [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals(intervals) == output


def test_merging_different_intervals():
    intervals = [[1,4],[4,5]]
    output = [[1, 5]]
    assert merge_intervals(intervals) == output


def test_merging_no_intervals():
    intervals = []
    output = []
    assert merge_intervals(intervals) == output

