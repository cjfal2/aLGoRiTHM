import sys
input = sys.stdin.readline

while 1:
    try:
        N = int(input())
        a = 0
        while 1:
            a += 1
            ans = int('1'*a)
            if not ans % N:
                print(a)
                break
    except:
        break