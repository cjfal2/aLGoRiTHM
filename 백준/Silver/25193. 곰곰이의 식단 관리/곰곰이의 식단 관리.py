c, n = 0, int(input())
for i in input():
    if i == "C":
        c += 1
print(n // (n - c + 1))