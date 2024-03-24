a = 0
for _ in range(int(input())):
    a += sum(list(map(int, input().split())))
print(a)