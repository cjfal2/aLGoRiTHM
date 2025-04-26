N, M = map(int, input().split())

points = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            points.append((i, j))

# 1의 좌표 두 개를 꺼내서 택시 거리 계산
(y1, x1), (y2, x2) = points
taxi_distance = abs(x1 - x2) + abs(y1 - y2)

print(taxi_distance)
