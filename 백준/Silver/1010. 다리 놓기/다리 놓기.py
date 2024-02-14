for _ in range(int(input())):
    N, M = map(int, input().split())
    a = 1
    b = 1
    for i in range(N):
        a *= (M-i)
        b *= (N-i)
    print(a//b)
