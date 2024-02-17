for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = divmod(a, b)
    print(f"You get {c} piece(s) and your dad gets {d} piece(s).")