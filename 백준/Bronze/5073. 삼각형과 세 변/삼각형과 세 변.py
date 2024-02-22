while 1:
    arr = sorted(map(int, input().split()))

    a = arr[0]
    b = arr[1]
    c = arr[2]

    if a == b == c == 0:
        break

    if a + b <= c:
        print("Invalid")
        continue

    if a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")
