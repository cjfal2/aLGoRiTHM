import math
import sys
for _ in range(int(sys.stdin.readline().strip())):
    N,M = map(int,sys.stdin.readline().strip().split())
    print(math.lcm(N,M))