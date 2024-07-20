N1, N2 = map(int, input().split())
temp = []
ant1 = input()[::-1]
for i in ant1:
    temp.append([i, 0])
ant2 = input()
for i in ant2:
    temp.append([i, 1])
T = int(input())
for t in range(T):
    k = 0
    while k < len(temp)-1:
        if temp[k][1] == 0:
            if temp[k][1] != temp[k+1][1]:
                temp[k], temp[k+1] = temp[k+1], temp[k]
                k += 2
            else:
                k += 1
        else:
            k += 1
    #     print(temp)
    # print("TTTTTTTTTTTTTTTTTTT")
answer = ""
for a, b in temp:
    answer += a
print(answer)