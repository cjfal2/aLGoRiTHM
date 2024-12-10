N = int(input())
if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print('*' * N)  # 첫 줄
    print(' ' * (N // 2) + '*')  # 가운데 별
    for i in range(1, N // 2 + 1):  # 아래 갈래
        print(' ' * (N // 2 - i) + '*' + ' ' * (2 * i - 1) + '*')