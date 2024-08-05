temp = dict()
for _ in range(int(input())):
    a, b = input().split()
    if temp.get(a):
        temp[a].append(b)
    else:
        temp[a] = [b]
arr = dict(sorted(temp.items()))
for a in arr:
    b = sorted(arr[a], reverse=1)
    for c in b:
        print(a, c)