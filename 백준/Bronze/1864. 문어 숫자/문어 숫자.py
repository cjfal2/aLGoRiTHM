temp = {
    "-": 0,
    "\\": 1,
    "(": 2,
    "@": 3,
    "?": 4,
    ">": 5,
    "&": 6,
    "%": 7,
    "/": -1,
}

while 1:
    w = input()
    if w == "#":
        break
    arr = 0
    i = len(w) - 1
    for a in w:
        arr += (temp[a] * (8 ** i))
        i -= 1
    print(arr)
