n = int(input())
now = 0
a = 0
for i in list(map(int, input().split())):
    if i == now:
        now = (now + 1) % 3
        a += 1
print(a)