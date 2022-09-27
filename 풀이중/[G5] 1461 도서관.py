N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
minus = []
plus = []
for i in L:
    if i < 0 :
        minus.append(-i)
    else:
        plus.append(i)

print(minus,  plus)




