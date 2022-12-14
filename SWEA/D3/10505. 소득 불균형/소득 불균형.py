for tc in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    avg = sum(L)/N
    co = 0
    for num in L:
        if num <= avg:
            co += 1
    print(f'#{tc+1} {co}')