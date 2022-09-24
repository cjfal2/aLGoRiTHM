def enq(z):
    if ch[z] and z > N-1:
        return
    if ch[z]:
        for i in ch[z]:
            enq(i)
    else:
        ch[z].append(-7)

# -1 

N = int(input())
arr = list(map(int, input().split()))
DN = int(input())

ch = [[] for _ in range(N)]

for i in range(N):
    if arr[i] == -1:
        continue
    ch[arr[i]].append(i)

# print(ch)
enq(DN)
# print(ch)

if ch[arr[DN]] and DN in ch[arr[DN]]:
    ch[arr[DN]].remove(DN)
print(ch.count([]))