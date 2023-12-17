import sys
input = sys.stdin.readline


rsp = {
    "R": "S",
    "S": "P",
    "P": "R"
}


for _ in range(int(input().strip())):
    a, b = 0, 0
    for _ in range(int(input().strip())):
        q, p = input().strip().split()
        if rsp[q] == p:
            a += 1
        elif rsp[p] == q:
            b += 1

    if a > b:
        print("Player 1")
    elif a == b:
        print("TIE")
    else:
        print("Player 2")
