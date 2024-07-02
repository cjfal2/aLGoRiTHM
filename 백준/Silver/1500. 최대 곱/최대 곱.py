s, k = map(int, input().split())
q, r = divmod(s, k)
nums = [q + 1] * r + [q] * (k - r)
result = 1
for n in nums:
    result *= n
print(result)
