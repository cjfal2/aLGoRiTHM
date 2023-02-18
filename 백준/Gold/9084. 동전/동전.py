'''
3
2
1 2
1000
3
1 5 10
100
2
5 7
22
'''

import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    N = int(input().strip())
    coins = list(map(int, input().strip().split()))
    target = int(input().strip())
    
    memo = [1] + [0 for _ in range(target)]
    for coin in coins:
        for i in range(1, target+1):
            if i - coin >= 0:
                memo[i] += memo[i-coin]
    print(memo[target])
