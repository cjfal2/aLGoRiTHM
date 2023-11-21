def dfs(arr):
    global s, answer

    if len(s) == len(arr) - 1:
        a = []
        for k in range(len(arr)-1):
            a.append(arr[k])
            a.append(s[k])
        a.append(arr[-1])

        t = "".join(a).replace(" ", "")
        if eval(t) == 0:
            answer.append(a)
        return

    for d in ["+", "-", " "]:
        s.append(d)
        dfs(arr)
        s.pop()

tc = int(input())
for z in range(tc):
    temp = list(map(str, list(range(1, int(input())+1))))
    s = []
    answer = []
    dfs(temp)
    for m in sorted(answer):
        print(*m, sep="")
    if z != tc-1:
        print()