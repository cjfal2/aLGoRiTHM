'''
각 조의 맨 끝과 맨끝의 키차이는 그 사이 키차이의 누적합? 합? 과 같다.
조는 양쪽의 키차이가 가장 큰 친구를 기준으로 나누면 된다.
그래서 양 옆 키 차이를 저장하고, 그 키차이들 중
키 차이가 큰 것을 조의 수 만큼 제외하고 다 더하면 된다.
'''

N, K = map(int, input().split())
L = list(map(int, input().split()))
memo = [L[i+1] - L[i] for i in range(N-1)] # 끝 까지 가면 인덱스에러, 옆 사람과의 키 차이 저장
print(sum(sorted(memo)[:N-K]))  # 조의 수 만큼 키차이를 제외하고 모두 더함
