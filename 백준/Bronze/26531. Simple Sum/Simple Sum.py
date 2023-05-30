ans = 0
a = input()
for i in a[:8]:
    if i in '0123456789':
        ans += int(i)
print("YES") if ans == int(a[-1]) else print("NO")
        