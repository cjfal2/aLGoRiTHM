from collections import deque

def main(n, a, b):
    # BFS를 위한 큐 초기화
    queue = deque([(n, 0)])  # (현재 남은 사람 수, 소요 시간)
    visited = [False] * (n + 1)  # 방문 여부 체크

    while queue:
        current, time = queue.popleft()

        # 맨 앞에 도달하면 최소 시간 반환
        if current == 0:
            return time

        # 이미 방문한 경우 스킵
        if visited[current]:
            continue
        visited[current] = True


        # 행동 추가
        if current >= 1:
            queue.append((current - 1, time + 1))
        if current >= a:  # a명 앞으로 가기
            queue.append((current - a - 1, time + 1))
        if current >= b:  # b명 앞으로 가기
            queue.append((current - b - 1, time + 1))

    return -1

if __name__ == "__main__":
    nn, aa, bb = map(int, input().split())
    print(main(nn, aa, bb))