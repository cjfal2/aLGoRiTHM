import sys
input = sys.stdin.readline

N = int(input().strip())
temp = []

for _ in range(N):
    a = input().strip()
    if len(a) != 1:
        b = a.split(" ")
        temp.append(int(b[-1]))
    elif a == "2":
        if temp:
            print(temp.pop())
        else:
            print(-1)
    elif a == "3":
        print(len(temp))
    elif a == "4":
        if temp:
            print(0)
        else:
            print(1)
    else:
        if temp:
            print(temp[-1])
        else:
            print(-1)
