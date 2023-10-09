'''
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
또, 나눗셈은 정수 나눗셈으로 몫만 취한다.

음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고,
그 몫을 음수로 바꾼 것과 같다

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다.
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100)
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데
    차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
'''
N = int(input())
numbers = list(map(int, input().split()))
gihos = ""
temp = list(map(int, input().split()))

for i in range(4):
    if i == 0:
        gihos += ("+" * temp[i])
    if i == 1:
        gihos += ("-" * temp[i])
    if i == 2:
        gihos += ("*" * temp[i])
    if i == 3:
        gihos += ("/" * temp[i])

visited = [0 for _ in range(N)]

answer_max, answer_min = -float("INF"), float("INF")


def dfs(num, use):
    global answer_max, answer_min

    if use == N-1:
        answer_max = max(answer_max, num)
        answer_min = min(answer_min, num)
        return

    for w in range(N-1):
        if not visited[w]:
            visited[w] = 1
            if gihos[w] == "+":
                new_num = num + numbers[use+1]
            elif gihos[w] == "-":
                new_num = num - numbers[use+1]
            elif gihos[w] == "*":
                new_num = num * numbers[use+1]
            elif gihos[w] == "/":
                if num >= 0:
                    new_num = num // numbers[use+1]
                else:
                    temp = num * -1
                    new_num = temp // numbers[use+1]
                    new_num *= -1

            dfs(new_num, use+1)
            visited[w] = 0


dfs(numbers[0], 0)
print(answer_max)
print(answer_min)
