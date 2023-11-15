a = list(int(input()) for _ in range(4))
if a[0] in [8, 9] and a[-1] in [8, 9] and a[1] == a[2]:
    print("ignore")
else:
    print("answer")