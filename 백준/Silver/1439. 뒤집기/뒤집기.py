s = "2" + input()
zero = 0
one = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == "1":
            one += 1
        else:
            zero += 1
print(min(zero, one))