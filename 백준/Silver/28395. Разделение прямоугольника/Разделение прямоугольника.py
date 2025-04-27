import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, k, m = map(int, input().split())
    found = False
    for h in range(min(k, a-1)+1):
        v = k - h
        if 0 <= v <= b-1 and (h+1)*(v+1) == m:
            print(h, v)
            found = True
            break
    if not found:
        print(-1)
