def solve(num):
    man = 1
    wife = num
    bojagi = num ** 2
    cat = num ** 3
    kitty = num ** 4
    return round(man + wife + bojagi + cat + kitty, 2)


while 1:
    n = float(input())
    if n == 0:
        break
    print(f'{solve(n):.2f}')