co = 0
for _ in range(int(input())):
    memo = []
    for i in input():
        if memo and memo[-1] == i:
            continue
        memo.append(i)
    # print(f'디버깅 단어:{memo}')
    flag = True
    for j in memo:
        if memo.count(j) > 1:
            flag = False
            break
    if flag:
        co += 1
print(co)
