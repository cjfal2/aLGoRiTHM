def solve(p1, s1, s2, p2):
    # 두 팀의 득점 합산
    persepolis = p1 + p2
    esteghlal = s1 + s2

    # 합계 점수가 같은 경우
    if persepolis == esteghlal:
        # 원정 다득점 규칙 적용
        if s1 > p2:
            return "Esteghlal"
        elif p2 > s1:
            return "Persepolis"
        else:
            return "Penalty"  # 승부차기로 결정
    # 합계 점수가 다른 경우
    elif persepolis > esteghlal:
        return "Persepolis"
    else:
        return "Esteghlal"


# 입력 받기
p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
# 결과 출력
print(solve(p1, s1, s2, p2))
