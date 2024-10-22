n=int(input())%10
answer = ""
t = "SciComLove"
for i in range(n, 10):
    answer += t[i]
for j in range(n):
    answer += t[j]
print(answer)