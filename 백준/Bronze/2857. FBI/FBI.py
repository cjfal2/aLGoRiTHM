L = []
for i in range(1, 6):
    if "FBI" in input():
        L.append(i)
if L:
    print(*L)
else:
    print("HE GOT AWAY!")