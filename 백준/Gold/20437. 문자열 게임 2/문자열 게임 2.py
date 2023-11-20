from collections import defaultdict


for _ in range(int(input())):
    w, k = input(), int(input())
    if k == 1:
        print(1, 1)
        continue

    long = len(w)
    MIN = long
    MAX = 0
    memo = defaultdict(list)

    for i in range(long):
        if w.count(w[i]) >= k:
            memo[w[i]].append(i)

    if not memo:
        print(-1)
        continue

    for i in memo.values():
        for j in range(len(i)-k+1):
            temp = i[j+k-1]-i[j]+1
            MIN = min(MIN, temp)
            MAX = max(MAX, temp)

    print(MIN, MAX)
