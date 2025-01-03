change = {
    "A" : "B",
    "B" : "C",
    "C" : "D",
    "D" : "E",
    "E" : "F",
    "F" : "G",
    "G" : "H",
    "H" : "I",
    "I" : "J",
    "J" : "K",
    "K" : "L",
    "L" : "M",
    "M" : "N",
    "N" : "O",
    "O" : "P",
    "P" : "Q",
    "Q" : "R",
    "R" : "S",
    "S" : "T",
    "T" : "U",
    "U" : "V",
    "V" : "W",
    "W" : "X",
    "X" : "Y",
    "Y" : "Z",
    "Z" : "A"
}


test_case = int(input())
for tc in range(1, test_case+1):
    print(f'String #{tc}')

    answer = ""
    for word in input():
        answer += change[word]

    print(answer)
    if tc != test_case:
        print()





