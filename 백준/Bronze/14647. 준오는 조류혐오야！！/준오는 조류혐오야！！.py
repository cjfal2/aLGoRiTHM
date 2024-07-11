n, m = map(int, input().split())
total = 0
max_nine = 0
pan = [input().split() for _ in range(n)]

for i in range(n):
    temp = "".join(pan[i])
    nine = temp.count("9")
    total += nine
    max_nine = max(max_nine, nine)

for j in range(m):
    temp = ""
    for i in range(n):
        temp += pan[i][j]
    nine = temp.count("9")
    max_nine = max(max_nine, nine)
    
print(total - max_nine)