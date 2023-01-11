N = int(input())

day = 0
temp = 0
for s in input():
    if s == "(":
        temp += 1
    else:
        temp -= 1
    day = max(abs(temp), day)
    
print(day) if not temp else print(-1)