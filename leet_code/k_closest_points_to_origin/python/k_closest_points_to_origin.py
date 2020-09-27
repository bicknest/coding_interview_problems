import math
def k_closest_points(plane, k):
    annotated_plane = []
    for x, y in plane:
        distance = math.sqrt(pow(x, 2) + pow(y, 2))
        annotated_plane.append((x, y, distance))

    annotated_plane.sort(key=lambda x: x[2])
    k_annotated_plane = annotated_plane[:k]
    return [[x, y] for x, y, z in k_annotated_plane]
