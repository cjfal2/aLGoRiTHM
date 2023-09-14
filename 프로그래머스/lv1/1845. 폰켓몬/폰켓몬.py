def solution(nums):
    I = len(nums) // 2
    nums = set(nums)
    N = len(nums)
    return N if N <= I else I