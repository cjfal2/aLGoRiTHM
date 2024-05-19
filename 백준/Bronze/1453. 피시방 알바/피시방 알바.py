a = 0
input()
t = set(list(range(1, 101)))
for j in list(map(int, input().split())):
    if j in t:
        t.remove(j)
    else:
        a += 1
print(a)