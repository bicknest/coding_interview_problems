def trapping_rain_water(elevations):
    water_count = 0
    for i in range(1, len(elevations) - 1):
        left = elevations[i]
        for j in range(i):
            left = max(left, elevations[j])

        right = elevations[i]

        for j in range(i + 1, len(elevations)):
            right = max(right, elevations[j])

        water_count = water_count + (min(left, right) - elevations[i])

    return water_count
