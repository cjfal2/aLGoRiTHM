def LEN(arr):
    co = 0
    for _ in arr:
        co+=1
    return co

L = list(input())
if LEN(L) == 2:
    print(0)
else:
    stick = 0
    zogak = 1
    for i in range(LEN(L)-1):
        if L[i] =='(' and L[i+1] == ')':
            zogak += stick
        elif L[i] == '(' and L[i+1] != ')':
            stick += 1
        elif i>1 and L[i] == ')' and L[i-1] != '(':
            stick -= 1
            zogak += 1
    print(zogak)