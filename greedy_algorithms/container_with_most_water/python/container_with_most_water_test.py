from container_with_most_water import container_with_most_water

def test_container_with_no_tricky_edge_problem():
    heights = [1,8,6,2,5,4,8,3,7]
    assert container_with_most_water(heights) == 49

def test_container_tricky_edge_problem():
    heights = [1,2,4,3]
    assert container_with_most_water(heights) == 4

def test_container_edge_one():
    heights = [1, 1, 1, 1, 100, 1, 1, 1, 1]
    assert container_with_most_water(heights) == 8

def test_container_edge_two():
    heights = [1, 1, 1, 1, 100, 1, 1, 1, 1, 50]
    assert container_with_most_water(heights) == 250
