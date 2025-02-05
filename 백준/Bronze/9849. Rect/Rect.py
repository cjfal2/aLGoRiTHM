import sys

input = sys.stdin.readline


n = int(input().strip())
x1, x2, y1, y2 = map(int, input().strip().split())

intersect_x1, intersect_x2 = x1, x2
intersect_y1, intersect_y2 = y1, y2


for _ in range(n - 1):
    a, b, c, d = map(int, input().strip().split())

    intersect_x1 = max(intersect_x1, a)
    intersect_x2 = min(intersect_x2, b)

    intersect_y1 = max(intersect_y1, c)
    intersect_y2 = min(intersect_y2, d)

if intersect_x1 < intersect_x2 and intersect_y1 < intersect_y2:
    area = (intersect_x2 - intersect_x1) * (intersect_y2 - intersect_y1)
else:
    area = 0

print(area)

