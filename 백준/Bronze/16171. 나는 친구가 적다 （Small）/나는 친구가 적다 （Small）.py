a = ""
for j in input():
    if not j.isdigit():
        a += j
b = input()
if b in a:
    print(1)
else:
    print(0)