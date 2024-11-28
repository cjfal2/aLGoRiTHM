arr = [int(input()) for _ in range(9)]
A = sum(arr)
arr.sort()

def solve():
    for n in range(8):
        for m in range(n+1, 9):
            if A - arr[n] - arr[m] == 100:
                return n, m

r, l = solve()
for i in range(9):
    if i in [r, l]:
        continue
    print(arr[i])