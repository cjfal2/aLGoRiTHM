target = int(input())
while 1:
    num = int(input())
    if not num:
        quit()
    print(f'{num} is NOT a multiple of {target}.') if num % target else print(f'{num} is a multiple of {target}.')