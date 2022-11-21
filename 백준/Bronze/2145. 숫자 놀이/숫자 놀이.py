while 1:
    num = input()
    if num[0] == "0":
        break
    while len(num) != 1:
        co = 0
        for i in num:
            a = int(i)
            co += a
        num = list(str(co))
    print(num[0])