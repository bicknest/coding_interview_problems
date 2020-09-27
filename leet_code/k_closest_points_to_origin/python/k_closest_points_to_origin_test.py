from k_closest_points_to_origin import k_closest_points

def test_a_few_points():
    points = [[1,3],[-2,2]]
    k = 1
    assert k_closest_points(points, k) == [[-2, 2]]

def test_more_points():
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(k_closest_points(points, k))
    assert k_closest_points(points, k) == [[3, 3], [-2, 4]]
