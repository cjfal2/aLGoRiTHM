def calculate_kilometers(test_cases):
    results = []
    for case in test_cases:
        G, C, E = case
        group_distances = {1: 1, 2: 3, 3: 5}
        
        candies_needed = E - C
        
        if candies_needed <= 0:
            results.append(0)
        else:
            results.append(candies_needed * group_distances[G])
    
    return results

results = calculate_kilometers([list(map(int, input().split())) for _ in range(int(input()))])
for result in results:
    print(result)
