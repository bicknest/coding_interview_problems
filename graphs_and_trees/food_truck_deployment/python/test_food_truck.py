from food_truck import number_of_possible_food_trucks

def test_a_simple_city():
    """
    city:
    0 0 0 0 1
    1 0 0 0 1
    0 0 0 0 0
    1 1 1 1 1
    rows: 4
    columns: 5
    number_of_trucks: 3
    """
    city = [[0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
    rows = len(city)
    columns = len(city[0])

    assert number_of_possible_food_trucks(city, rows, columns) == 3


def test_entire_city_as_one_park():
    """
    city:
    1 1 1
    1 1 1
    1 1 1
    rows: 3
    columns: 3
    number_of_trucks: 1
    """
    city = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    rows = len(city)
    columns = len(city[0])
    assert number_of_possible_food_trucks(city, rows, columns) == 1


def test_entire_city_commercial_area():
    """
    city:
    0 0 0
    0 0 0
    0 0 0
    rows: 3
    columns: 3
    number_of_trucks: 0
    """

    city = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rows = len(city)
    columns = len(city[0])
    assert number_of_possible_food_trucks(city, rows, columns) == 0

def test_more_complicated_city_with_diagnoals():
    """
    city:
    0 1 0 1 0 1
    1 0 1 1 0 1
    1 0 0 1 1 0
    0 1 0 0 0 1
    rows: 4
    columns: 6
    number_of_trucks: 6
    """
    
    city = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 1]]
    rows = len(city)
    columns = len(city[0])
    assert number_of_possible_food_trucks(city, rows, columns) == 6
