def make(m):
    global last
    last += 1 # 마지막 정점 추가
    tree[last] = m # 마지막 정점에 key 추가

    # 부모가 있고, 부모 > 자식 인 경우 자리 교환 (최소 힙)
    c = last
    p = c // 2 # 완전이진트리에서 부모 정점 번호
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


for tc in range(int(input())):
    N = int(input())
    tree = [0] * (N+1)
    last = 0
    for m in list(map(int, input().split())):
        make(m)
    ans = 0
    last_node = N
    while 1:
        last_node = last_node//2
        if last_node == 0:
            break
        ans += tree[last_node]
    print(f'#{tc+1} {ans}')
