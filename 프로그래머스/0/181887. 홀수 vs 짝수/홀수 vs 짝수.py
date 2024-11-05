def solution(num_list):
    odd, eve = 0, 0
    for n in range(1, len(num_list)+1):
        if n % 2:
            odd += num_list[n-1]
        else:
            eve += num_list[n-1]
    return max(odd, eve)