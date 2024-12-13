word = input()
answer = ""
idx = 0

while idx < len(word):
    answer += word[idx]
    nxt = ord(word[idx]) - ord('A') + 1
    idx += nxt

print(answer)
