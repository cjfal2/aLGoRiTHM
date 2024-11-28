def back():
    global answer

    if len(s) == a_len:
        number = int("".join(s))
        if number < B:
            answer = max(answer, number)
        return

    for i in range(a_len):
        if a_arr[i] == "0" and not s:
            continue

        if not visited[i]:
            s.append(a_arr[i])
            visited[i] = 1
            back()
            visited[i] = 0
            s.pop()


A, B = map(int, input().split())
a_len = len(str(A))
b_len = len(str(B))

a_arr = sorted(list(str(A)), reverse=True)
s = []
visited = [0 for _ in range(a_len)]
answer = 0

if a_len <= b_len:
    back()

print(answer if answer else -1)