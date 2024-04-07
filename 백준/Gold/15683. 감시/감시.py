# CCTV의 방향을 돌려가면서 최대 탐색칸 수를 저장
# 처음부터 CCTV들을 모두 저장 => 최대 8개 까지 이므로 가능
# 5번부터 시작해서 1번까지

N, M = map(int, input().split())  # N, M: 세로, 가로
pan = []
total = N * M
cctv = []
wall = set()
for n in range(N):
    arr = list(map(int, input().split()))
    for m in range(M):
        if arr[m] in [1, 2, 3, 4, 5]:
            cctv.append([arr[m], n, m])
            total -= 1
        elif arr[m] == 6:
            wall.add((n, m))
            total -= 1
    pan.append(arr)
visited = [[0 for _ in range(M)] for _ in range(N)]
for z, k, u in cctv:
    visited[k][u] = 1
for k, u in wall:
    visited[k][u] = 1

cctv_amount = len(cctv)
answer = total + 1

directions = {
    1: [
        [(0, 1)],
        [(-1, 0)],
        [(0, -1)],
        [(1, 0)]
    ],
    2: [
        [(1, 0), (-1, 0)],
        [(0, 1), (0, -1)]
    ],
    3: [
        [(-1, 0), (0, 1)],
        [(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(-1, 0), (0, -1)]
    ],
    4: [
        [(-1, 0), (0, 1), (0, -1)],
        [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)],
        [(-1, 0), (0, -1), (1, 0)]
    ],
    5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]]
}


def back(depth):
    global answer

    if cctv_amount == depth:
        temp = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 0:
                    temp += 1
        # print("==============")
        # for p in visited:
        #     print(*p)
        # print("==============")
        answer = min(temp, answer)
        return

    number, x, y = cctv[depth]
    for dix in directions[number]:
        visited_point = set()
        for dx, dy in dix:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if N > nx >= 0 and M > ny >= 0 and (nx, ny) not in wall:
                    if visited[nx][ny] == 1:
                        continue
                    visited_point.add((nx, ny))
                else:
                    break

        for sx, sy in visited_point:
            visited[sx][sy] = 1
        back(depth + 1)
        for sx, sy in visited_point:
            visited[sx][sy] = 0


back(0)
print(answer)
