import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    a, b = input().strip().split()
    a = int(a) - 1
    b = list(b)
    b.pop(a)
    print(*b, sep="")