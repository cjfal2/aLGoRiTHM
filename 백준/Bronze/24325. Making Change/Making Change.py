def solve(cost, payment):
    change = payment - cost
    bills = [50, 20, 10, 5, 1]
    counts = []
    
    for bill in bills:
        c = int(change // bill)
        counts.append(c)
        change -= c * bill
    
    return counts

n = int(input())
for _ in range(n):
    cost, payment = map(float, input().split())
    counts = solve(cost, payment)
    print(f"{counts[0]}-$50, {counts[1]}-$20, {counts[2]}-$10, {counts[3]}-$5, {counts[4]}-$1")
