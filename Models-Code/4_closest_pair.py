import random
import math

# Function to generate random points
def generate_random_points(n):
    points = []

    # Generate n random points within the range (-500, 500)
    for i in range(n):
        points.append((random.randint(-500, 500), random.randint(-500, 500)))

    return points


# Function to calculate the distance between two points
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Use the distance formula to calculate the distance
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


# Brute force approach to find the closest pair of points
def brute_force(points):
    min_dist = float("inf")  # Initialize the minimum distance to infinity
    min_points = None  # Initialize the closest pair of points to None

    # Iterate over each point in the list
    for inner_point in points:
        for outer_point in points:
            if inner_point == outer_point:
                continue

            # Calculate the distance between the current pair of points
            distance = calculate_distance(inner_point, outer_point)

            # Update the minimum distance and closest pair of points if necessary
            if distance < min_dist:
                min_dist = distance
                min_points = (inner_point, outer_point)

    return min_points, min_dist


# Optimized approach to find the closest pair of points
def optimized_way(points):
    points = sorted(points, key=lambda x: x[0])  # Sort the points based on their x-coordinate

    # Base case: if there are only 2 or 3 points, use brute force approach
    if len(points) == 2 or len(points) == 3:
        return brute_force(points)

    mid = len(points) // 2  # Find the middle index

    # Divide the points into left and right subarrays
    left_subarray = points[:mid]
    right_subarray = points[mid:]

    # Recursively find the closest pair of points in the left and right subarrays
    min_points_left, min_dist_left = optimized_way(left_subarray)
    min_points_right, min_dist_right = optimized_way(right_subarray)

    # Determine the minimum distance and closest pair of points from the left and right subarrays
    if min_dist_left < min_dist_right:
        min_point, min_dist = min_points_left, min_dist_left
    else:
        min_point, min_dist = min_points_right, min_dist_right

    mid_x = (points[mid - 1][0] + points[mid][0]) / 2  # Calculate the x-coordinate of the middle point

    # Create a strip of points within the minimum distance from the middle line
    strip = [point for point in points if abs(mid_x - point[0]) < min_dist]

    strip.sort(key=lambda x: x[1])  # Sort the strip based on their y-coordinate

    # Find the closest pair of points within the strip
    min_point_strip, min_dist_strip = brute_force(strip)

    # Update the minimum distance and closest pair of points if necessary
    if min_dist_strip < min_dist:
        min_point, min_dist = min_point_strip, min_dist_strip

    return min_point, min_dist


if __name__ == "__main__":
    points = generate_random_points(100)  # Generate 100 random points

    print("Brute force way of finding the closest pair:")
    pair, distance = brute_force(points)
    print("Pair:", pair)
    print("Distance:", distance)

    print("Optimized Way of finding the closest pair:")
    pair, distance = optimized_way(points)
    print("Pair:", pair)
    print("Distance:", distance)

    # plot_points_with_shortest_distance(points)  # Uncomment this line to plot the points with the shortest distance
