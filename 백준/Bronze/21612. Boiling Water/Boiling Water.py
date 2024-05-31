B = int(input())
P = 5 * B - 400

if P < 100:
    level = 1  # 해수면 위
elif P == 100:
    level = 0  # 해수면
else:
    level = -1  # 해수면 아래

print(P)
print(level)
