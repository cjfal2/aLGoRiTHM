import sys
input = sys.stdin.readline

N = int(input().strip())
L = [list(map(int, input().strip().split())) for _ in range(N)]


ans = big = sys.maxsize
for start in range(3):
    new = [[big, big, big]]
    new[0][start] = L[0][start]
    R = new + [[0, 0, 0] for _ in range(N-1)]

    for h in range(1, N):
        R[h][0] = min(R[h-1][1], R[h-1][2]) + L[h][0]
        R[h][1] = min(R[h-1][0], R[h-1][2]) + L[h][1]
        R[h][2] = min(R[h-1][0], R[h-1][1]) + L[h][2]
    
    for end in range(3):
        if start != end:
            ans = min(R[-1][end], ans)
print(ans)

