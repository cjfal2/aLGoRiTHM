temp = {
    "k": 0,
    "p": 1,
    "n": 3,
    "b": 3,
    "r": 5,
    "q": 9,
    "K": 0,
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
}

answer = 0
for _ in range(8):
    for w in input():
        if w == ".":
            continue
        if w in "kpnbrq":
            answer -= temp.get(w)
        else:
            answer += temp.get(w)
print(answer)