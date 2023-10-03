keys, words = input(), input()
N = len(keys)
K = len(words)//N

G = [[keys[k], k] for k in range(N)]
G.sort(key=lambda x: (x[0], x[1]))

i = -1
for idx, w in enumerate(words):
    if not idx%K:
        i += 1
    G[i].append(w)

G.sort(key=lambda x: (x[1], x[0]))

a = ""
for m in range(2, K+2):
    for n in range(N):
        a += G[n][m]
print(a)