a = dict()
for _ in range(int(input())):
    w = input()
    a[w] = 1 if w not in a else a[w] + 1

b = dict()
for k, v in a.items():
    if v not in b:
        b[v] = [k]
    else:
        b[v].append(k)

print(sorted(sorted(b.items())[-1][1])[0])
