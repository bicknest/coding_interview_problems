"""

def find_max_length_index(walls, idx_one, idx_two):
    d = idx_two - idx_one
    if max((walls[idx_one] + d), walls[idx_two]) == walls[idx_two]:
        return idx_two
    return idx_one

def container_with_most_water(walls):
    max_area = min(walls[0], walls[1]) * 1
    max_area_index = 0
    max_length_index = find_max_length_index(walls, 0, 1)
    if walls[0] + 1 < walls[1]:
        max_area_index = 1
    for curr_index in range(2, len(walls)):
        print("\n"*8)
        print(max_area_index)
        print(max_length_index)
        current_area_with_max_area = (curr_index - max_area_index) * min(walls[curr_index], walls[max_area_index])
        current_area_with_max_length = (curr_index - max_length_index) * min(walls[curr_index], walls[max_length_index])
        print(current_area_with_max_area)
        print(current_area_with_max_length)
        max_area = max(max_area, current_area_with_max_area, current_area_with_max_length)
        max_length_index = find_max_length_index(walls, max_length_index, curr_index)
        if current_area_with_max_length > current_area_with_max_area:
            max_area_index = max_length_index

    return max_area
"""


## Approach too naive
## Need to come at the problem from either side
## if value of right wall is less than value of right wall, move in the right wall and vice versa


def container_with_most_water(height):
    l = 0
    r = len(height) - 1
    max_area = 0

    while (l < r):
        max_area = max(max_area, (r - l) * min(height[r], height[l]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
