import sys
input = sys.stdin.readline
from collections import deque


def isPrime(number):
    '''
    에라토스테네스의 체
    number의 최대 약수가 sqrt(number) 이하이므로 i=sqrt(number)까지 검사
    '''
    for m in range(2, int(number ** 0.5) + 1):
        if not number % m:     
            return False # 소수가 아니다.
    return True # 소수가 맞다.


def check(n):
    '''
    범위 체크 & 소수 체크
    '''
    if start <= n <= end:
        return isPrime(n) # 소수가 맞으면 True, 아니면 False
    return False # 범위가 아니면 False


def bfs(num):
    q = deque([(num, 0)])
    visited = set([num])
    while q:
        x, cnt = q.popleft()
        for i in [x//3, x//2, x+1, x-1]:
            if i not in visited and 1000001 >= i > 0:
                if not check(i):
                    q.append((i, cnt+1))
                    visited.add(i)
                else:
                    return cnt+1
    return -1


for _ in range(int(input())):
    N, start, end = map(int, input().split()) # 전체 수 N, 목표 범위인 자연수 start, end
    if check(N):
        print(0)
        continue

    print(bfs(N))