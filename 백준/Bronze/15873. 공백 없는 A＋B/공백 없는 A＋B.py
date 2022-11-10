n = input()
if len(n) == 4:
    print(20)
elif len(n) == 2:
    print(int(n[0])+int(n[1]))
else:
    if n[1] == "1":
        print(10+int(n[0]))
    else:
        print(int(n[:2])+int(n[2]))
    