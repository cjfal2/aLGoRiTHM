def cal(formula):
    cnt = 0
    for num in formula.split("+"):
        cnt += int(num)
    return cnt


sik = input().split('-')
co = cal(sik[0])
for i in range(1, len(sik)):
    co -= cal(sik[i])
print(co)
