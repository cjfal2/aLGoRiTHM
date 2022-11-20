import sys
input = sys.stdin.readline

for _ in range(3):
    co = 0
    for _ in range(int(input().strip())):
        i = int(input().strip())
        co += i
    if co > 0:
        print("+")
    elif co == 0:
        print("0")
    else:
        print("-")
        