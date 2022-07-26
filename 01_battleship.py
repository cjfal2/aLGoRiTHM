import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    pass
    sea[index-1] = sea[index] = sea[index+1] = 1
    return sea


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드


# 1. 게임 준비
while True:
    pass
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_start_point = int(input("당신의 시작점을 고르세요: "))
    # 1-2) 범위를 벗어난 시작점을 고른 경우
    if player_start_point > 13 or 1 > player_start_point:
        print('1~13 의 숫자를 입력하세요.')
        continue
    # 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
    computer_start_point = random.randint(1,13)
    # 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
    computer_ship_zone = set_ship(computer_start_point,computer_sea)
    player_ship_zone = set_ship(player_start_point,player_sea)
    break


# 2. 라운드 진행
while True:
    pass
    # 2-1) 플레이어 공격
    print(f'ROUND{round} 시작')
    print(f'플레이어의 해역: {player_ship_zone}')
    print(f'플레이어의 공격 기록: {computer_attacked}')

    player_attack = int(input("공격할 위치를 입력하세요. : "))
    if not (1 <= player_attack <= 15):
        print("[해역의 범위에서 벗어난 위치] 다시 입력하세요.")
        continue

    # 2-2) 플레이어의 공격 위치 선택
    if 1 <= player_attack <= 15:
        if computer_attacked[player_attack-1] == False:
            computer_attacked[player_attack-1] = True
        elif computer_attacked[player_attack-1] == True:
            print("[이미 공격한 자리] 다시 입력하세요.")
            continue
    # 2-3) 플레이어의 공격이 성공한 경우
    if computer_ship_zone[player_attack-1] :
        print(f"플레이어는 상대방의 해역 {player_attack-1}을 공격하여 상대 배를 혼내줬습니다! 플레이어는 {round}라운드만에 승리했습니다.")
        break
    # 2-4) 플레이어의 공격이 실패한 경우
    else :
        print(f'플레이어는 상대방 해역{player_attack-1}을 공격했지만, 공격에 실패했습니다')
    # 2-5) 컴퓨터의 공격 위치 지정
    while True :
        com_attack = random.randint(1,15)
        if player_attacked[com_attack-1] == True:
            continue
        elif player_attacked[com_attack-1] == False:
            break
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    if player_attacked[com_attack-1] == False:
        player_attacked[com_attack-1] = True

    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_ship_zone[com_attack-1] :
        print(f"콤퓨타는 당신의 해역 {com_attack-1}을 공격하여 당신을 혼내줬습니다! 콤퓨타한테 {round}라운드만에 졌습니다.")
        break
    # 2-7) 컴퓨터의 공격이 실패한 경우
    elif not player_ship_zone[com_attack-1]:
        print(f'콤퓨타는 당신 해역{com_attack-1}을 공격했지만, 공격에 실패했습니다')
    round += 1