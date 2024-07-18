words = [input() for _ in range(int(input()))]
words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)