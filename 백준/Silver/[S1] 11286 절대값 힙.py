import heapq, sys
input = sys.stdin.readline

L = []
for _ in range(int(input().strip())):
    b = int(input().strip())
    a = (abs(b), b)
    if a[0] == 0:
        if not L:
            print(0)
        else:
            c = heapq.heappop(L)
            print(c[1])
    else:
        heapq.heappush(L, a)