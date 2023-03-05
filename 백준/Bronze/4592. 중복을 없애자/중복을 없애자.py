while 1:
    a, *b = map(int, input().split())
    if not a:
        break
    ans = []
    for num in b:
        if not ans or num != ans[-1]:
            ans.append(num)
    print(*ans, "$")
            