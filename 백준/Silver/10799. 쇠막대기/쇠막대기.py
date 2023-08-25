def LEN(arr):
    co = 0
    for _ in arr:
        co += 1
    return co

L = list(input())
stick = 0
zogak = 0

for i in range(LEN(L)):
    if L[i] == '(':
        stick += 1
    elif L[i] == ')' and L[i - 1] == '(':
        stick -= 1
        zogak += stick
    elif L[i] == ')' and L[i - 1] != '(':
        stick -= 1
        zogak += 1

print(zogak)
