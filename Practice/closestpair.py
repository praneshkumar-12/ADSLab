import random
import math


def generate_random_points(n):
    points = []

    for i in range(n):
        points.append((random.randint(-500, 500), random.randint(-500, 500)))

    return points


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def brute_force(points):
    min_dist = float("inf")
    min_points = None

    for inner_point in points:
        for outer_point in points:
            if inner_point == outer_point:
                continue

            distance = calculate_distance(inner_point, outer_point)

            if distance < min_dist:
                min_dist = distance
                min_points = (inner_point, outer_point)

    return min_points, min_dist


def optimized_way(points):
    points = sorted(points, key=lambda x: x[0])

    if len(points) == 2 or len(points) == 3:
        return brute_force(points)

    mid = len(points) // 2

    left_subarray = points[:mid]
    right_subarray = points[mid:]

    min_points_left, min_dist_left = optimized_way(left_subarray)
    min_points_right, min_dist_right = optimized_way(right_subarray)

    if min_dist_left < min_dist_right:
        min_point, min_dist = min_points_left, min_dist_left
    else:
        min_point, min_dist = min_points_right, min_dist_right

    mid_x = (points[mid - 1][0] + points[mid][0]) / 2

    strip = [point for point in points if abs(mid_x - point[0]) < min_dist]

    strip.sort(key=lambda x: x[1])

    min_point_strip, min_dist_strip = brute_force(strip)

    if min_dist_strip < min_dist:
        min_point, min_dist = min_point_strip, min_dist_strip

    return min_point, min_dist


if __name__ == "__main__":
    points = generate_random_points(100)

    print("Brute force way of finding the closest pair:")
    pair, distance = brute_force(points)
    print("Pair:", pair)
    print("Distance:", distance)

    print("Optimized Way of finding the closest pair:")
    pair, distance = optimized_way(points)
    print("Pair:", pair)
    print("Distance:", distance)

    # plot_points_with_shortest_distance(points)
