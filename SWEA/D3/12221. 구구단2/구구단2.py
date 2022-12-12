for tc in range(int(input())):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(f'#{tc+1} -1')
    else:
        print(f'#{tc+1} {a*b}')