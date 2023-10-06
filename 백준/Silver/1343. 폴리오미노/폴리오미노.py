w = input()
N = len(w)

i = 0
temp = []
while i < N:
    if i < N-3 and w[i] == w[i+1] == w[i+2] == w[i+3] == "X":
        temp.append("AAAA")
        i += 4
    elif i < N-1 and w[i] == w[i+1] == "X":
        temp.append("BB")
        i += 2
    elif w[i] == '.':
        temp.append(".")
        i += 1
    else:
        print(-1)
        quit()
print(*temp, sep="")