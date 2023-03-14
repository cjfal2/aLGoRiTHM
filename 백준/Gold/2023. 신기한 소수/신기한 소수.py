def check(num):
    '''
    에라토스테네스의 체
    n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    '''
    for m in range(2, int(num ** 0.5) + 1):
        if not num % m:     
            return True
    return False


def dfs(num):
    if check(int(num)):
        return
        
    if len(num) == N:
        print(num)
        return
    for k in range(1, 10):
        dfs(num+str(k))


N = int(input())
for n in '2357':
    dfs(n)
