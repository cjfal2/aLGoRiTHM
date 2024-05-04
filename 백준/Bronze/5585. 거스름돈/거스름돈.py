n = 1000 - int(input())
a = 0
for i in [500, 100, 50, 10, 5, 1]:
    b, n = divmod(n, i)
    a += b
print(a)