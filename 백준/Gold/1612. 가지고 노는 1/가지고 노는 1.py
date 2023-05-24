number = int(input())
if not number % 2 or not number % 5 :
    print(-1)
else:
    sep = 0
    for i in range(1, number + 1):
        sep = (10 * sep + 1) % number
        if sep == 0:
            print(i)
            break
