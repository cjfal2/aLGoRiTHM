n = input()
t = 0
while 1:
    if len(n) == 1:
        print(t)
        break
    m = 1
    for i in n:
        m *= int(i)
    n = str(m)
    t += 1