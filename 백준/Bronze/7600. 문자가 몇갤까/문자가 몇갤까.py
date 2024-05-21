while 1:
    a = input()
    if a == "#":
        break
    c = set()
    for b in a.lower():
        if b in "qwertyuiopasdfghjklzxcvbnm":
            c.add(b)
    print(len(c))