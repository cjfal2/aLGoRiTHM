case = 0
while 1:
    case += 1
    a = input()
    b = input()
    if a == b == "END":
        break
    a = sorted(list(a))
    b = sorted(list(b))
    if a == b:
        print(f'Case {case}: same')
    else:
        print(f'Case {case}: different')
        