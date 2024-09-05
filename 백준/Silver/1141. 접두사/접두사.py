N = int(input())
words = sorted(set([input() for _ in range(N)]))
words.sort(key=lambda x: len(x))
N = len(words)
cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        if words[j].startswith(words[i]):
            cnt += 1
            break

print(N-cnt)
