def cal(a, b):
    return abs(a-b)


tc = int(input())
for _ in range(tc):
    M = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    k = 0
    while k < 1001:
        k += 1
        for i in range(M):
            if i == M - 1:
                new_arr.append(cal(arr[-1], arr[0]))
            else:
                new_arr.append(cal(arr[i], arr[i+1]))
        temp = set(new_arr)
        if temp == {0}:
            print("ZERO")
            break
        else:
            arr = new_arr[:]
            new_arr.clear()
    if k > 1000:
        print("LOOP")
