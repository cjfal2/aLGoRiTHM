from collections import deque
import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
L = [0] + list(map(int, input().split()))
Q = [deque() for _ in range(P+1)]
answer = [0 for _ in range(P+1)]

pan = []
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] != '.' and temp[j] != '#':
            T = int(temp[j])
            answer[T] += 1
            Q[T].append((i, j))
    pan.append(temp)

flag = True
while flag:
    flag = False
    for num in range(1, P+1):

        q, move = Q[num], L[num]
        if not q:
            continue

        for _ in range(move):
            if not q:
                break
            
            for _ in range(len(q)):
                x, y = q.popleft()
                for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == '.':
                        pan[nx][ny] = num
                        q.append((nx, ny))
                        answer[num] += 1
                        flag = True

print(*answer[1:])
