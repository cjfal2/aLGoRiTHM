n = input()
t = 0
while len(n) != 1:
    t += 1
    num = 0
    for m in n:
        num += int(m)
    n = str(num)
print(t)
print("NO" if int(n) % 3 else "YES")