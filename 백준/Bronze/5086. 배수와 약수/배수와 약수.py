while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
        
    elif m % n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    else:
        print("neither")