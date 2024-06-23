for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    candy = [input() for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if i < n-2 and candy[i][j] == "v" and candy[i+1][j] == "o" and candy[i+2][j] == "^":
                answer += 1
            
            if j < m-2 and candy[i][j] == ">" and candy[i][j+1] == "o" and candy[i][j+2] == "<":
                answer += 1
    print(answer)
            