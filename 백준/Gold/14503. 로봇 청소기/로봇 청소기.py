# 0을 청소 하는 것

# 0상 1우 2하 3좌
# news를 조절하여 탐색 방향을 조절한다.
news = {
    0: [[0, -1, 3], [1, 0, 2], [0, 1, 1], [-1, 0, 0]],  # 좌 하 우 상
    1: [[-1, 0, 0], [0, -1, 3], [1, 0, 2], [0, 1, 1]],  # 상 좌 하 우
    2: [[0, 1, 1], [-1, 0, 0], [0, -1, 3], [1, 0, 2]],  # 우 상 좌 하
    3: [[1, 0, 2], [0, 1, 1], [-1, 0, 0], [0, -1, 3]],  # 하 우 상 좌
}


# 반대쪽을 확인하기 위한 변수, 벽이면 멈출것이기 때문에
bande = {
    0: [1, 0],  # 상 --반대-> 하
    1: [0, -1], # 우 --반대-> 좌
    2: [-1, 0], # 하 --반대-> 상
    3: [0, 1],  # 좌 --반대-> 우
}

sero, garo = map(int, input().split())
s, g, dix = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(sero)]

while 1:
    # 현재 위치를 청소한다.
    if pan[s][g] == 0:
        pan[s][g] = 2 # 청소한 곳은 2로 바꿈

    # for else 구문을 사용할 것임
    for ds, dg, new_dix in news.get(dix): # 현재 방향에서 얻은 news 리스트를 순회
        ns, ng = s + ds, g + dg
        if pan[ns][ng] == 0:
            s += ds # 한칸 전진
            g += dg
            dix = new_dix # 방향 재설정
            break # 여기서 브레이크를 걸면 for else 구문 다 탈출

    else: # for else 구문이라서 if에 아무것도 안걸렸다면 여기로 옴
        # 반대쪽이 벽인지 체크, 벽이면 True
        bds, bdg = bande.get(dix)
        if pan[s+bds][g+bdg] == 1:
            break
        else: # 땅이면 뒤로가기
            s += bds
            g += bdg

print(sum(pan, []).count(2))