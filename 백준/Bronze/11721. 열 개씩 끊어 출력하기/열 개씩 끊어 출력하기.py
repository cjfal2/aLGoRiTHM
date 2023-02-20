a = input()
i = 1
for j in a:
    if i%10:
        print(j, end="")
    else:
        print(j)
    i += 1