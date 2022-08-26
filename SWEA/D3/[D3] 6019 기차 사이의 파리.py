for tc in range(int(input())):
    D,A,B,F=map(int,input().split())
    print(f'#{tc+1} {F*D/(A+B)}')