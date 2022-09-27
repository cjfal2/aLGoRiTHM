import sys
input = sys.stdin.readline

N = int(input().strip())
L = [list(map(int, input().strip().split())) for _ in range(N)]


R = [L[0]] + [[0, 0, 0] for _ in range(N-1)]

for h in range(1, N):
    R[h][0] = min(R[h-1][1], R[h-1][2]) + L[h][0]
    R[h][1] = min(R[h-1][0], R[h-1][2]) + L[h][1]
    R[h][2] = min(R[h-1][0], R[h-1][1]) + L[h][2]

print(min(R[N-1][0],R[N-1][1],R[N-1][2]))

