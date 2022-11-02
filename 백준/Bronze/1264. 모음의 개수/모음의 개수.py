while 1:
    w = input()
    if w == "#":
        break
    co = 0
    for x in w:
        if x in "aeiouAEIOU":
            co += 1
    print(co)