command = [int(input()) for _ in range(10)]
temp = {
    "N": {
        1: "E",
        2: "S",
        3: "W"
    },
    "E": {
        1: "S",
        2: "W",
        3: "N"
    },
    "S": {
        1: "W",
        2: "N",
        3: "E"
    },
    "W": {
        1: "N",
        2: "E",
        3: "S"
    }
}
now = "N"
for c in command:
    now = temp[now][c]
print(now)
