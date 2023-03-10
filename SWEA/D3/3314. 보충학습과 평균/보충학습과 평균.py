for tc in range(int(input())):
    L = list(map(lambda x: int(x) if int(x) >= 40 else 40, input().split()))
    print(f'#{tc+1} {sum(L)//len(L)}')  