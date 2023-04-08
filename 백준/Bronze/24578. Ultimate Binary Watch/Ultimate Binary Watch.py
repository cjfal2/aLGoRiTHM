num = list(map(lambda x: bin(int(x)).replace('0b',''), list(input())))

for n in range(len(num)):
    if len(num[n]) == 1:
        num[n] = "..."+num[n]
    elif len(num[n]) == 2:
        num[n] = ".."+num[n]
    elif len(num[n]) == 3:
        num[n] = "."+num[n]
    num[n] = num[n].replace("0", ".")
    num[n] = num[n].replace("1", "*")
for i in range(4):
    for n in range(len(num)):
        if n == 1:
            print(num[n][i], end="   ")
        elif n == 3:
            print(num[n][i],)
        else:
            print(num[n][i], end=" ")
