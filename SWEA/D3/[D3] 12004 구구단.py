# 정수 N이 주어졌을 때, N 이 1 이상 9 이하의 두 수 a, b의 곱으로 표현될 수 있는지 판단하라.
def dfs():
    if len(s) == 2:
        a, b = s[0], s[1]
        temp.append(a*b)
        return

    for i in range(1, 10):
        s.append(i)
        dfs()
        s.pop()

s = []
temp = []
dfs()

# 백트래킹을 이용하여 1~9의 길이가 2인 자신을 포함한 순열을 전부 만들고
# temp에 그 곱을 저장
# N이 거기에 있는지 확인해봤어용
# 테스트 케이스에 대하여 temp 리스트는 계속 다시 써서 dfs는 한번만 시행하게됨!
for tc in range(int(input())):
    N = int(input())
    if N in temp:
        print(f'#{tc+1} Yes')
    else:
        print(f'#{tc+1} No')