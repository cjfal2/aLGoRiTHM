import sys
input = sys.stdin.readline

N = int(input())
max_x, max_y, min_x, min_y = -10001, -10001, 10001, 10001
for _ in range(N):
    a, b = map(int, input().split())
    max_x = max(a, max_x)
    max_y = max(b, max_y)
    min_x = min(a, min_x)
    min_y = min(b, min_y)

if max_x == min_x or max_y == min_y:
    print(0)
    quit()

print((max_x-min_x)*(max_y-min_y))
