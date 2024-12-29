while True:
    n = int(input())
    if n == 0:
        break

    votes = input().split()
    person_count = {i: 0 for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]}
    
    for i, person in enumerate(votes, 1):
        person_count[person] += 1
        remaining = n - i  # 남은 투표 수
        
        # 현재까지 가장 많은 표를 받은 후보와 두 번째로 많은 표를 받은 후보 찾기
        sorted_counts = sorted(person_count.items(), key=lambda x: x[1], reverse=True)
        max_votes = sorted_counts[0][1]
        second_votes = sorted_counts[1][1]
        
        # 현재 최다 득표자가 남은 투표를 모두 받아도 이길 수 없는 경우
        if max_votes + remaining < second_votes:
            print("TIE")
            break
            
        # 다른 후보가 남은 투표를 모두 받아도 현재 최다 득표자를 이길 수 없는 경우
        if second_votes + remaining < max_votes:
            print(sorted_counts[0][0], i)
            break
    else:
        # 모든 투표를 끝냈는데도 승자가 결정되지 않은 경우
        sorted_counts = sorted(person_count.items(), key=lambda x: x[1], reverse=True)
        if sorted_counts[0][1] == sorted_counts[1][1]:
            print("TIE")
        else:
            print(sorted_counts[0][0], n)