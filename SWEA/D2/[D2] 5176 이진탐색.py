def tree(n):
    print(f'tree({n})')
    global num
    if n <= N:
        tree(n*2)
        G[n] = num
        print(f'G[{n}]', G[n])
        num += 1
        print('num:', num)
        tree(n*2+1)


for tc in range(int(input())):
    N = int(input())
    G = [0 for _ in range(N+1)]
    num = 1
    tree(num)
    print(G)
    print(f'#{tc+1} {G[1]} {G[N//2]}')