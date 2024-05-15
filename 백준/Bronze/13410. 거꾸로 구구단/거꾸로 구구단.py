temp = []
a, b = map(int, input().split())
for i in range(1, b+1):
    c = str(a * i)[::-1]
    temp.append(int(c))
temp.sort()
print(temp[-1])