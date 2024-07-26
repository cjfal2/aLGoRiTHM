import math

def get_PPI(W, H):
    return math.sqrt(W*W + H*H) / 77

N = int(input())
monitors = [list(map(int, input().split())) for _ in range(N)]
temp = []
for i in range(1, N+1):
    temp.append((get_PPI(*monitors[i-1]), i))
temp.sort(key=lambda x: (-x[0], x[1]))
for t, a in temp:
    print(a)