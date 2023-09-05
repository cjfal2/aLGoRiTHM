def solution(nums):
    answer = 0
    
    def is_prime():
        temp = [True] * (3002)
        temp[0] = temp[1] = False

        for num in range(2, int(3001**0.5) + 1):
            if temp[num]:
                for multiple in range(num * num, 3002, num):
                    temp[multiple] = False

        prime_list = [x for x in range(3, 3002) if temp[x]]
        return prime_list

    
    primes = is_prime()
    N = len(nums)
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if nums[a]+nums[b]+nums[c] in primes:
                    answer += 1

    return answer