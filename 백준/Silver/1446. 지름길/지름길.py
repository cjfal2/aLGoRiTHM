N, D = map(int, input().split())        # N: 지름길 수, D: 고속도로 길이(도착지)
distance = [now for now in range(D + 1)]    # 고속도로의 거리 저장소 (일단 원래 거리로 저장)
shortcut = [[] for _ in range(D + 1)]   # 지름길 저장소

for _ in range(N):
    start, end, how = map(int, input().split())  # 지름길의 시작 위치, 도착 위치, 지름길의 길이
    if end - start <= how:  # 지름길 길이가 더 길면
        continue

    if end > D:  # 끝이 고속도로를 넘어가면
        continue

    shortcut[start].append((end, how))

for now in range(D + 1):
    before = distance[now - 1] if now else -1 # 이전 거리
    distance[now] = min(distance[now], before + 1) # 지름길로 저장된거랑 지금거랑 비교

    if shortcut[now]:
        # 지름길이 있다면 지름길 순회
        for arv, how in shortcut[now]:
            # 지금 + 지름길 길이 와 도착지의 길이 비교해서 더 이득인 것을 넣기
            distance[arv] = min(distance[now] + how, distance[arv])

print(distance[D])  # 도착지 출력
