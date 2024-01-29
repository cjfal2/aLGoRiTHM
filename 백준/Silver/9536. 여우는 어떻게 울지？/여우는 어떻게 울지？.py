for _ in range(int(input())):
    said = input().split()
    memo = set()
    while 1:
        fox = input()
        if fox == "what does the fox say?":
            break
        a, b, c = fox.split()
        memo.add(c)
    for s in said:
        if s not in memo:
            print(s, end=" ")
    print()