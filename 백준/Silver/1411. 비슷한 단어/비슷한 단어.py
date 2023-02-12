import sys
input = sys.stdin.readline

words = []
for _ in range(int(input().strip())):
    alpha = list("qwertyuiopasdfghjklzxcvbnm")
    word = list(input().strip())
    visited = [0 for _ in range(len(word))]
    for w in range(len(word)):
        if not visited[w]:
            target = alpha.pop()
            what = word[w]
            for i in range(w, len(word)):
                if not visited[i] and word[i] == what:
                    word[i] = target
                    visited[i] = 1
    words.append(''.join(word))

ans = 0
for w in range(len(words)-1):
    for h in range(w+1, len(words)):
        if words[w] == words[h]:
            ans += 1
print(ans)
