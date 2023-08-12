for _ in range(int(input())):
    S, T = map(int, input().split())
    q = [(S, T, 0)]
    while q:
        x, y, c = q.pop(0)
        if x == y:
            print(c)
            break
        
        for d in "AB":
            if d == "A":
                nx = x + x
                ny = y + 3
            else:
                nx = x + 1
                ny = y
            if nx <= ny:
                q.append((nx, ny, c+1))
                