L = sorted(map(int, input().split()))

dt = {
    "A":L[0],
    "B":L[1],
    "C":L[2]
}
for i in input():
    print(dt.get(i), end=" ")