def check(num):
    for m in range(2, int(num ** 0.5) + 1):
        if not num % m:     
            return True
    return False

n = int(input())
while 1:
    n += 1
    if check(n):
        print(n)
        break
