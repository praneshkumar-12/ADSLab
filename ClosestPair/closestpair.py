import random
import math
import matplotlib.pyplot as plt


def create_random_points(n):
    random_points = []
    for i in range(n):
        random_points.append((random.randint(-10, 10), random.randint(-10, 10)))

    return random_points


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def brute_force(points):
    min_dist = float("inf")
    min_point = None

    for out_point in points:
        for in_point in points:
            if out_point == in_point:
                continue
            dist = calculate_distance(out_point, in_point)

            if dist < min_dist:
                min_dist = dist
                min_point = [out_point, in_point]

    return (min_point, min_dist)


def optimized_way(points):
    x_sorted_points = sorted(points, key=lambda x: x[0])

    min_point, min_dist = optimized_find_distance(x_sorted_points)

    return min_point, min_dist


def optimized_find_distance(points):
    if len(points) == 2 or len(points) == 3:
        return brute_force(points)

    mid = len(points) // 2

    left_subarray = points[:mid]
    right_subarray = points[mid:]

    min_point_left, min_dist_left = optimized_find_distance(left_subarray)
    min_point_right, min_dist_right = optimized_find_distance(right_subarray)

    if min_dist_left < min_dist_right:
        min_point, min_dist = min_point_left, min_dist_left
    else:
        min_point, min_dist = min_point_right, min_dist_right

    mid_x = (points[mid - 1][0] + points[mid][0]) / 2
    strip = [point for point in points if abs(point[0] - mid_x) < min_dist]

    strip.sort(key=lambda point: point[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            dist = calculate_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                min_point = (strip[i], strip[j])
            j += 1

    return min_point, min_dist


def plot_points_with_shortest_distance(points):
    # Calculate the shortest distance and the closest pair of points using a brute-force method
    def calculate_shortest_distance(points):
        min_distance = float("inf")
        closest_pair = None

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                point1 = points[i]
                point2 = points[j]

                # Calculate the Euclidean distance between the points
                distance = math.sqrt(
                    (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
                )

                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (point1, point2)

        return closest_pair, min_distance

    # Get the closest pair and shortest distance
    closest_pair, shortest_distance = calculate_shortest_distance(points)

    # Create a plot
    plt.figure(figsize=(10, 10))

    # Plot each point
    for point in points:
        plt.scatter(*point, c="blue")
        plt.text(point[0], point[1], f"{point}", fontsize=9, ha="right", va="bottom")

    # Plot the shortest distance line and annotate the distance
    point1, point2 = closest_pair
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], c="red", linestyle="-")

    # Calculate the midpoint of the line
    mid_x = (point1[0] + point2[0]) / 2
    mid_y = (point1[1] + point2[1]) / 2

    # Annotate the distance at the midpoint of the line
    plt.text(mid_x, mid_y, f"{shortest_distance:.2f}", fontsize=10, color="red")

    # Set the axis limits
    plt.xlim(min([p[0] for p in points]) - 2, max([p[0] for p in points]) + 2)
    plt.ylim(min([p[1] for p in points]) - 2, max([p[1] for p in points]) + 2)

    # Set aspect ratio to be equal
    plt.gca().set_aspect("equal", adjustable="box")

    # Add labels to the axes
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")

    # Add a title to the plot
    plt.title("Plot of Points with Shortest Distance")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # points = [(-5, -3), (9, -9), (0, 9), (1, 6), (7, -1), (3, -10), (-5, -1), (-6, -5)]

    points = create_random_points(10)

    print("Brute force way of finding the closest pair:")
    pair, distance = brute_force(points)
    print("Pair:", pair)
    print("Distance:", distance)

    print("Optimized Way of finding the closest pair:")
    pair, distance = optimized_way(points)
    print("Pair:", pair)
    print("Distance:", distance)

    plot_points_with_shortest_distance(points)
