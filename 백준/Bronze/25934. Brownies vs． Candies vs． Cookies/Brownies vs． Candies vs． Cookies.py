def solve(practices):
    for i, practice in enumerate(practices):
        num_students, num_brownies = practice['students'], practice['brownies']
        groups = practice['groups']

        print(f"Practice #{i+1}: {num_students} {num_brownies}")

        for group in groups:
            while num_brownies <= group:
                num_brownies *= 2
            num_brownies -= group
            print(f"{group} {num_brownies}")

        print()


n = int(input())
practices = []

for _ in range(n):
    num_students, num_brownies = map(int, input().split())
    m = int(input())
    groups = [int(input()) for _ in range(m)]
    practices.append({
        'students': num_students,
        'brownies': num_brownies,
        'groups': groups
    })

solve(practices)
