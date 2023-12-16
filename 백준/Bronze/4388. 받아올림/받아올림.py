while 1:
    a, b = input().split()
    if a == b == "0":
        break
    a = sorted(map(int, [0] + list(a)), reverse=1)
    b = sorted(map(int, [0] + list(b)), reverse=1)
    if len(a) > len(b):
        while len(a) != len(b):
            b += [0]
    elif len(a) < len(b):
        while len(a) != len(b):
            a += [0]
    length = len(a)
    answer = 0
    for i in range(length):
        if a[i] + b[i] >= 10:
            a[i+1] += 1
            answer += 1
    print(answer)
