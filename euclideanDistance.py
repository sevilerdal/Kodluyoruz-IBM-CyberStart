import math

# Define points
points = [(1,1) , (1,2) , (2,2) , (2,3)]


# Calculate distance between two points
def euclideanDistance(point1, point2):
    x0,y0 = point1
    x1,y1 = point2
    distance = math.sqrt((x1-x0)**2 + (y1-y0)**2)
    return distance


distances = []


# Calculate distance for every point in points
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)


# Find minimum distance
minDistance = min(distances)

# Print minimum distance
print ("Minimum distance : ", minDistance)