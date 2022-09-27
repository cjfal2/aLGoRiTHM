import sys
input = sys.stdin.readline

N = int(input().strip())
Q = [list(map(int, input().strip().split())) for _ in range(N)]


L = [Q[0]] + [[0, 0, 0] for _ in range(N-1)]
R = [Q[0]] + [[0, 0, 0] for _ in range(N-1)]

for h in range(1, N):
    L[h][0] = max(L[h-1][0], L[h-1][1]) + Q[h][0]
    L[h][1] = max(L[h-1][0], L[h-1][1], L[h-1][2]) + Q[h][1]
    L[h][2] = max(L[h-1][1], L[h-1][2]) + Q[h][2]

    R[h][0] = min(R[h-1][0], R[h-1][1]) + Q[h][0]
    R[h][1] = min(R[h-1][0], R[h-1][1], R[h-1][2]) + Q[h][1]
    R[h][2] = min(R[h-1][1], R[h-1][2]) + Q[h][2]


print(max(L[N-1][0],L[N-1][1],L[N-1][2]), min(R[N-1][0],R[N-1][1],R[N-1][2]))

