n = int(input())
temp = dict()
for _ in range(n):
    a, b = input().split()
    temp[b] = a
text = list(input())
answer = ""
for t in text:
    answer += temp[t]
s, e = map(int, input().split())
s-=1
print(answer[s:e])