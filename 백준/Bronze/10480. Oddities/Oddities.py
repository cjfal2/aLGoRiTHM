for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(f'{n} is even')
        continue
    d = n
    if n < 0:
        n *= -1
        
    print(f"{d} is odd" if n % 2 else f"{d} is even")
        