n = int(input())
nums = list(map(int, input().split()))
s = int(input())

for i in range(n):
    a = max(nums[i: min(n, i + s + 1)])
    z = nums.index(a)
    for j in range(z, i, -1):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        
    s -= (z - i)
    if s <= 0:
        break

print(*nums)