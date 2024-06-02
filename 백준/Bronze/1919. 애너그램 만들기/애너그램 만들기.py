from collections import Counter

def solve(word1, word2):
    counter1 = Counter(word1)
    counter2 = Counter(word2)

    diff = counter1 - counter2
    diff += counter2 - counter1

    return sum(diff.values())


word1 = input().strip()
word2 = input().strip()


result = solve(word1, word2)

print(result)
