# https://www.acmicpc.net/problem/16235
"""
1. 처음에는 모든 칸에 양분 5
2.  봄 - 나이만큼 양분을 먹고, 나이가 1증가
    나이가 어린 나무부터 양분을 먹는다.
    나이만큼 양분을 먹지 못하면 죽는다.

    여름 - 봄에 죽은 나무가 양분으로 변한다.
    각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. (소수점 아래는 버린다.)

    가을 - 나무가 번식한다.
    번식하는 나무는 나이가 5의 배수여야하고
    인접한 8개 칸에 나이가 1인 나무가 생긴다.

    겨울 - 로봇이 양분을 추가한다. (따로 입력)

3. K년이 지난 후 살아있는 나무의 수를 구하라
"""
from collections import deque


N, M, K = map(int, input().split())
robot = [list(map(int, input().split())) for _ in range(N)]
energy = [[5 for _ in range(N)] for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    # 봄
    deads = []
    birth_trees = deque()
    for x in range(N):
        for y in range(N):
            for _ in range(len(trees[x][y])):
                tree = trees[x][y].popleft()
                if tree > energy[x][y]:
                    deads.append((x, y, tree//2))
                    continue
                energy[x][y] -= tree
                trees[x][y].append(tree + 1)
                if (tree + 1) % 5 == 0:
                    birth_trees.append((x, y))
            # 겨울
            energy[x][y] += robot[x][y]
    # 여름
    for dead_tree in deads:
        x, y, z = dead_tree
        energy[x][y] += z
    # 가을
    for birth_tree in birth_trees:
        x, y = birth_tree
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            trees[nx][ny].appendleft(1)

answer = 0
for x in range(N):
    for y in range(N):
        answer += len(trees[x][y])
print(answer)
