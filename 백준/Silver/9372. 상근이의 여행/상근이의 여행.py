import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    N, M = map(int, input().strip().split())
    for _ in range(M):
        a, b = map(int, input().strip().split())
    print(N-1)