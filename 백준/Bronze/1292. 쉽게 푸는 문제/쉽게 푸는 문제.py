a, b = map(int, input().split())
temp = []
n = 0
for i in range(1, 200):
    n += 1
    for _ in range(n):
        temp.append(i)
answer = sum(temp[a-1:b])
print(answer)