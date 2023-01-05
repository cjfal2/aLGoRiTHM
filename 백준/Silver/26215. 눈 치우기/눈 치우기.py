N = int(input())
L = sorted(map(int, input().split()), reverse=True)
cost = 0
while L:
    if len(L) >= 2:
        L[0] -= 1
        L[1] -= 1
        cost += 1
        while 1:
            L.sort()
            if L and L[0] == 0:
                L.pop(0)
            else:
                break
    else:
        cost += L[0]
        print(cost) if cost < 1441 else print(-1)
        quit()
    L.sort(reverse=True)
    # print(f'==========cost:{cost}=============')
    # print(L)
    # print("==============================")
print(cost) if cost < 1441 else print(-1)