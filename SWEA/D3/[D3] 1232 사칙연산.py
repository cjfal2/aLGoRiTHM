def postorder(n):
    if n:
        if ch1[n] != 0:
            postorder(ch1[n])
        if ch2[n] != 0:
            postorder(ch2[n])
        Q.append(tree[n])


buho = ["+", "-", "/", "*"]
for tc in range(10):
    N = int(input())
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for _ in range(N):
        L = list(input().split())
        n = int(L[0])
        if L[1] in buho:
            tree[n] = L[1]
            if len(L) > 2:
                for i in L[2:]:
                    p, c = n, int(i)
                    if ch1[p] == 0:  # 아직 자식이 없으면
                        ch1[p] = c
                    else:
                        ch2[p] = c
        else:
            tree[n] = int(L[1])
    Q = []
    postorder(1)
    s = []
    for q in Q:
        if q not in buho:
            s.append(q)
        else:
            a = s.pop()
            b = s.pop()
            if q == "+":
                c = b + a
                s.append(c)
            elif q == "-":
                c = b - a
                s.append(c)
            elif q == "*":
                c = b * a
                s.append(c)
            elif q == "/":
                c = b // a
                s.append(c)
    print(f'#{tc+1}', *s)