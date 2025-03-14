import sys
from collections import Counter

input = sys.stdin.readline

while True:
    n = int(input().strip())
    if n == 0:
        break

    course_combinations = Counter()

    for _ in range(n):
        courses = tuple(sorted(map(int, input().split())))
        course_combinations[courses] += 1

    max_popularity = max(course_combinations.values(), default=0)
    result = sum(count for count in course_combinations.values() if count == max_popularity)

    print(result)
