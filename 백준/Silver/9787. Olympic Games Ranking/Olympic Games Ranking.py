import sys

input = sys.stdin.read

def main():
    data = input().strip().split('\n')

    countries = []
    for line in data:
        code, g, s, b = line.split()
        g, s, b = map(int, (g, s, b))
        total = g + s + b
        countries.append((code, g, s, b, total))

    # 정렬: 금, 은, 동 내림차순, 국가코드 오름차순
    countries.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

    result = []
    rank = 1
    for i in range(len(countries)):
        if i > 0 and countries[i][1:4] == countries[i - 1][1:4]:
            # 동점인 경우 이전 순위와 동일
            current_rank = result[-1][0]
        else:
            current_rank = i + 1
        result.append((current_rank, *countries[i]))

    for entry in result:
        print(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5])

main()
