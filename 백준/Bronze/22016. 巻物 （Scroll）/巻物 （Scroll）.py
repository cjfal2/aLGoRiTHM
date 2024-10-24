N, M = map(int, input().split())
text = list(input())
for i in range(M-1, N):
    text[i] = text[i].upper() if text[i].islower() else text[i].lower()
print("".join(text))