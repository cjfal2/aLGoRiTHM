for tc in range(int(input())):
    L = input()
    x = 0
    for i in range(1, 31):
        if x > 0:
            break
        for j in range(0,31,i):
            if L[j:j+i] == L[j+i:j+i*2] and L[j+i:j+i*2] == L[j+i*2:j+i*3]:
                x = i
                break
            else:
                break
    print(f'#{tc+1} {x}')