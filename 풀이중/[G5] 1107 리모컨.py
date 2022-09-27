now = 100
want = int(input())
M = int(input())
error = list(map(int, input().split()))
counts = 0
can = []
for n in range(0, 10):
    if n not in error:
        can.append(n)

while 1:
    if want == now:
        print(counts)
        break

    if abs(want - now) <= 2:
        pass
