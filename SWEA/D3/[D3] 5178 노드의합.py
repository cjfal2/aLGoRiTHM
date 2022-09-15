def cal(node):
    if node <= N:
        if tree[node] == 0:  # 조상
            tree[node] = cal(node * 2) + cal(node * 2 + 1)    # 좌자식 + 우자식 을 재귀
        return tree[node]  # 리프 or 채워진 조상
    else:  # 트리 밖
        return 0


for tc in range(int(input())):
    N, M, L = map(int, input().split())
    # tree = [0] * (N+1)
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        n, num = map(int, input().split())
        tree[n] = num
    cal(1)
    # print(tree)
    print(f'#{tc+1} {tree[L]}')
