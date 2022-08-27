co=0
for i in input():
    if i in 'ABC':
        co+=3
    elif i in 'DEF':
        co+=4
    elif i in 'GHI':
        co+=5
    elif i in 'JKL':
        co+=6
    elif i in 'MNO':
        co+=7
    elif i in 'PQRS':
        co+=8
    elif i in 'TUV':
        co+=9
    elif i in 'WXYZ':
        co+=10
print(co)