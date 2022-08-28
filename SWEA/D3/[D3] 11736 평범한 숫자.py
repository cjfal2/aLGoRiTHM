for tc in range(int(input())):
    N = int(input())
    L = list(map(int,input().split()))
    co = 0
    for idx,num in enumerate(L[1:-1],1):
        if L[idx-1] < num < L[idx+1]:
            co += 1
        if L[idx+1] < num < L[idx-1]:
            co += 1
    print(f'#{tc+1} {co}')