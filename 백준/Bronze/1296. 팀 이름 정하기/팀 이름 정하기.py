from copy import deepcopy


temp = {
    "L": 0,
    "O": 0,
    "V": 0,
    "E": 0
}

t = input()
for k in t:
    if k in "LOVE":
        temp[k] += 1


def cal(l, o, v, e):
    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100


N = int(input())
arr = sorted(input() for _ in range(N))
num = -1
answer = arr[0]
for w in arr:
    love = deepcopy(temp)
    for a in w:
        if a in "LOVE":
            love[a] += 1
    b = list(love.values())
    c = cal(*b)
    if num < c:
        answer = w
        num = c
print(answer)
