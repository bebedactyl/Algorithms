
def cPairDist(points):
    """It takes in a list of 1-D points (i.e., integers) and returns the distance between the closest pair of points."""

    points.sort()
    return recCPairDist(points)

def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/conquer/combine steps."""

    # Divide: Split the list into two equal pieces.
    list_length = len(points)
    mid_point = list_length // 2
    # Conquer: Recursively find the closest pair distance in each sublist (obtains distances 1 and 2 from above).
    if list_length == 2:
        return abs(points[0]-points[1])
    if list_length == 3:
        distances = []
        x = abs(points[0] - points[1])
        distances.append(x)
        y = abs(points[1] - points[2])
        distances.append(y)
        return min(distances)
    minLeft = recCPairDist(points[:mid_point])
    minRight = recCPairDist(points[mid_point:])
    # Combine: Compute the remaining distance (3 from above), and combine them by taking the minimum of the three.
    minThree = abs(points[mid_point] - points[mid_point - 1])
    return min(minLeft, minRight, minThree)

# Testing
points = [7, 4, 12, 14, 2, 10, 16, 6]
print(cPairDist(points))
points2 = [7, 4, 12, 14, 2, 10, 16, 5]
print(cPairDist(points2))
points3 = [14, 8, 2, 6, 3, 10, 12]
print(cPairDist(points3))