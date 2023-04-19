import sys
input = sys.stdin.readline
for _ in range(int(input().strip())):
    print("odd") if int(input().strip())%2 else print("even")