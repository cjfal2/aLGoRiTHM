import heapq

# Coord 클래스 정의
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# compare 클래스 정의
class Compare:
    def __init__(self):
        pass

    def __lt__(self, a, b):
        return a[0] < b[0]

maxHeap = []
check = [[0] * 1001 for _ in range(1001)]
N, M = map(int, input().split())

# 외곽에 있는 것부터 추가
# 수확하는 순간 주변에 있는 옥수수를 힙에 담기
# 수확하려는 때에는 힙에서 제일 위에 있는 옥수수를 수확하기

def push(y, x):
    heapq.heappush(maxHeap, (-check[y][x], Coord(x, y)))
    check[y][x] = 0

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, M + 1):
        check[i][j] = row[j - 1]
        if i == 1 or i == N or j == 1 or j == M:
            push(i, j)

K = int(input())

for _ in range(K):
    value, coord = heapq.heappop(maxHeap)
    x, y = coord.x, coord.y
    print(y, x)
    if y > 1 and check[y - 1][x]:
        push(y - 1, x)
    if y < N and check[y + 1][x]:
        push(y + 1, x)
    if x > 1 and check[y][x - 1]:
        push(y, x - 1)
    if x < M and check[y][x + 1]:
        push(y, x + 1)
