for tc in range(int(input())):
    num = input()
    leng = len(num)
    ans = 9999999999
    for k in range(leng-1):
        n1 = int(num[:k+1])
        n2 = int(num[k+1:])
        n3 = n1+n2
        if n3 < ans:
            ans = n3
    print(f'#{tc+1} {ans}')