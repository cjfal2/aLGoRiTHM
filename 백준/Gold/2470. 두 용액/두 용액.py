import sys

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

MIN = sys.maxsize
start_point = 0
end_point = N - 1

while (start_point < end_point):
    SUM = liquid[start_point] + liquid[end_point]

    if MIN > abs(SUM):
        MIN = abs(SUM)
        small = liquid[start_point]
        big = liquid[end_point]
        if not SUM:
            break
    
    if SUM < 0:
        start_point += 1
    else:
        end_point -= 1
        
print(small, big)
