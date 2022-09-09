def cal():
    if len(s) == N-1:
        l = L[1:]
        A = L[0]
        for buho in s:
            if buho == '+':
                A += l.pop(0)
            elif buho == '-':
                A -= l.pop(0)
            elif buho == '*':
                A *= l.pop(0)
            elif buho == '//':
                if l[0] == 0:
                    return
                if A<0:
                    A *= -1
                    A //= l.pop(0)
                    A *= -1
                else:
                    A //= l.pop(0)
        real.append(A)
        return
    for i in range(N-1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        s.append(Q[i])
        cal()
        s.pop()
        visited[i] = 0


N = int(input()) # 숫자의 수
L = list(map(int, input().split())) # 숫자들
X = ['+', '-', '*', '//']
Q = []
y = 0
Y = list(map(int, input().split()))
for q in Y: # 연산자 리스트 만들기
    for _ in range(q):
        Q.append(X[y])
    y += 1
s = []
visited = [0] * (N+1)
real = []
cal()
print(max(real))
print(min(real))
