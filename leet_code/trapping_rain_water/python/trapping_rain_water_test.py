from trapping_rain_water import trapping_rain_water

def test_example_case():
    elevations = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    trapped_water = 6
    assert trapping_rain_water(elevations) == trapped_water
