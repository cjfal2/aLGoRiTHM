while 1:
    n = int(input())
    if not n: break
    print("TENTE NOVAMENTE" if n % 42 else "PREMIADO")