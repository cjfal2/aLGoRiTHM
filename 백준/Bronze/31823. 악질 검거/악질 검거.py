N, M = map(int, input().split())
fails = set()
answer = list()
for _ in range(N):
    temp = input().split()
    name = temp[-1]
    max_fail = 0
    now_fail = 0
    for m in range(M):
        if temp[m] == ".":
            now_fail += 1
        else:
            max_fail = max(max_fail, now_fail)
            now_fail = 0
    
    max_fail = max(max_fail, now_fail)
    answer.append([max_fail, name])
    fails.add(max_fail)
print(len(fails))
for a, b in answer:
    print(a, b)