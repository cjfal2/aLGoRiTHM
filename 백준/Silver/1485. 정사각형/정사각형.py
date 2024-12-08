import math

def is_square(points):
    def distance(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    distances = []
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(distance(points[i], points[j]))
    
    distances.sort()
    if len(distances) == 6 and distances[0] == distances[1] == distances[2] == distances[3]:
        if distances[4] == distances[5] and distances[4] > distances[0]:
            return 1
    return 0


T = int(input())
for _ in range(T):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    print(is_square(points))
    
