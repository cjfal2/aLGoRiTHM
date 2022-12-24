import sys
input = sys.stdin.readline
while 1:
    a,b,c=input().strip().split()
    if a == '#':
        quit()
    if int(b) > 17 or int(c) >= 80:
        print(f'{a} Senior')
    else:
        print(f'{a} Junior')
        