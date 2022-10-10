import heapq, sys
input = sys.stdin.readline

L = []
for _ in range(int(input().strip())):
    a = int(input().strip())
    if not a:
        if not L:
            print(0)
        else:
            print(heapq.heappop(L))
    else:
        heapq.heappush(L, a)