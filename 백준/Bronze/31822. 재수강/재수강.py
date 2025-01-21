a = input()[:5]
b = 0
for _ in range(int(input())):
    c = input()[:5]
    if a == c:
        b += 1
print(b)