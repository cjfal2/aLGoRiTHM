'''
https://www.acmicpc.net/problem/19538
'''
N = int(input())
G = [[] for _ in range(N+1)]
friends_num_half = [0]
for i in range(1, N+1):
    how = 0
    for j in list(map(int, input().split())):
        if j == 0:
            break
        G[i].append(j)
        how += 1
    # 친구 수의 절반 이상인지 확인하기 위해 홀 짝을 나눔
    friends_num_half.append(how//2 if how % 2 == 0 else how//2+1)

M = int(input())
start = set(list(map(int, input().split())))
answer = [-1 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
q = []
for s in start:
    answer[s] = 0
    q.append(s)
    visited[s] = 1
t = 0
while q:
    t += 1
    for _ in range(len(q)):
        x = q.pop(0)
        for w in G[x]:
            if not visited[w]:
                temp = 0
                for z in G[w]:
                    if t+1 > visited[z] > 0:
                        temp += 1
                if temp >= friends_num_half[w]:
                    visited[w] = t+1
                    answer[w] = t
                    q.append(w)


print(*answer[1:])
