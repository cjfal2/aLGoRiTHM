def cal(a, b, c):
    if c == "+":
        return a + b

    if c == "-":
        return a - b

    if c == "*":
        return a * b

    if c == "/":
        return a // b


arr = []
while 1:
    w = input()
    if w == "=": break
    arr.append(w if w in '*+-/' else int(w))


answer = arr[0]
for i in range(1, len(arr), 2):
    answer = cal(answer, arr[i+1], arr[i])
print(answer)