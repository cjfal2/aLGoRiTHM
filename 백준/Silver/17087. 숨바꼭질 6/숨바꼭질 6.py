import math
from functools import reduce


n, s = map(int, input().split())
positions = list(map(int, input().split()))
differences = [abs(s - pos) for pos in positions]
result_gcd = reduce(math.gcd, differences)
print(result_gcd)