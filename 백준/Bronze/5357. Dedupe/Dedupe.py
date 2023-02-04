'''
3
ABBBBAACC
AAAAA
ABC
'''
for _ in range(int(input())):
    a=''
    for k in input():
        if not a:
            a += k
        else:
            if a[-1] != k:
                a += k
    print(a)
