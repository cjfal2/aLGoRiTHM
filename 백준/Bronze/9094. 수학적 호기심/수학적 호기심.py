def cal(a, b, k):
    temp = (a*a+b*b+k)/(a*b)
    temp_int = int(temp)
    return True if temp == temp_int else False


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    answer = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            answer += cal(i, j, m)
    print(answer)
