a=input()
if a == "\"\"" or a == "\"":
    print("CE")
elif a[0] == a[-1] == "\"":
    print(a[1:-1])
else:
    print("CE")
