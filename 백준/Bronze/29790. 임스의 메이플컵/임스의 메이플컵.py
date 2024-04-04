a, b, c = map(int, input().split())
if a > 999 and (b > 7999 or c > 259):
    print("Very Good")
elif a > 999:
    print("Good")
else:
    print("Bad")