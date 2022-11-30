import sys

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

pH, basic, acidic = sys.maxsize, 0, N -1

while (basic < acidic):
    mix = liquid[basic] + liquid[acidic]

    if pH > abs(mix):
        pH, neutral_s, neutral_l = abs(mix), liquid[basic], liquid[acidic]
        if not mix:
            break

    if mix < 0:
        basic += 1
    else:
        acidic -= 1
        
print(neutral_s, neutral_l)
