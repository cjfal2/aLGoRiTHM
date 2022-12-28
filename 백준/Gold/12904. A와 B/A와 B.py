base, target = input(), input()

while (target != base):
    if len(target) == 0:
        print(0)
        quit()
    if target[-1] == 'A':
        target = target[:-1]
    elif target[-1] == 'B':
        target = target[::-1]
        target = target[1:]
    else:
        print(0)
        quit()
print(1)