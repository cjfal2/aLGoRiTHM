num = 0
ans = 0
for i in range(1, 6):
    L = sum(list(map(int ,input().split())))
    if ans < L:
        num = i
        ans = L
print(num, ans)