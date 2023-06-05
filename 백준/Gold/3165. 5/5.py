def back(L, i):
    global len_num

    if L.count('5') >= K:
        print(*L, sep="")
        quit()
    
    while L[i] == '5' and abs(i) < len_num:
        i -= 1
    
    num = int(''.join(L))
    num = num + 10 ** (abs(i) - 1)
    L = list(str(num))
    len_num = len(L)
    
    return back(L, i)


N, K = map(int, input().split())
N += 1
L = list(str(N))
i = -1
len_num = len(L)
back(L, i)

