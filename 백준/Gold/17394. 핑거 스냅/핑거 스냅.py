def isPrime(number):
    '''
    에라토스테네스의 체
    number의 최대 약수가 sqrt(number) 이하이므로 i=sqrt(number)까지 검사
    '''
    for m in range(2, int(number ** 0.5) + 1):
        if not number % m:     
            return True
    return False


def check(n):
    if start <= n <= end:
        return isPrime(n)
    return True


def bfs(num):
    q = [(num, 0)]
    visited = set(q)
    while q:
        x, cnt = q.pop(0)
        for i in [x//3, x//2, x+1, x-1]:
            if i not in visited and 1000001 >= i > 0:
                if check(i):
                    q.append((i, cnt+1))
                    visited.add(i)
                else:
                    return cnt+1
    return -1


for _ in range(int(input())):
    N, start, end = map(int, input().split()) # 전체 수 N, 목표 범위인 자연수 start, end
    if not check(N):
        print(0)
        continue

    print(bfs(N))