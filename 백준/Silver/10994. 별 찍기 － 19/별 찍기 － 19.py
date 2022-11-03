n = int(input())

def star_up(i):
    if i == (n-1)*2:
        return
    if i == 0:
        print('*'*(4*n-3))
    elif i % 2 == 1:
        print('* '*(i//2+1), ' '*(4*(n-(i+1)//2)-3), ' *'*(i//2+1), sep="")
    else:
        print('* '*(i//2), '*'*(4*(n-(i+1)//2)-3), ' *'*(i//2), sep="")
    star_up(i+1)

def star_down(i):
    if i == 0:
        print('*'*(4*n-3))
        return
    elif i % 2 == 1:
        print('* '*(i//2+1), ' '*(4*(n-(i+1)//2)-3), ' *'*(i//2+1), sep="")
    else:
        print('* '*(i//2), '*'*(4*(n-(i+1)//2)-3), ' *'*(i//2), sep="")
    star_down(i-1)

star_up(0)
star_down(2*n-2)