N = int(input())

alpha = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0
}

no_zero = set()

for _ in range(N):
    word = input()
    no_zero.add(word[0])
    for w in range(len(word)-1, -1, -1):
        alpha[word[w]] += 10 ** (len(word)-w-1)

answer = 0
temp = list(alpha.items())
temp.sort(key=lambda x: x[1])

if temp[0][0] in no_zero:
    for i in range(1, 10):
        if temp[i][0] not in no_zero:
            temp.remove(temp[i])
            break

for i in range(1, 10):
    answer += temp[-i][1] * (10 - i)

print(answer)
