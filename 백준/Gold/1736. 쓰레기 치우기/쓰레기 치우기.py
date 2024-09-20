N, M = map(int, input().split())
trash = 0 
pan = []
for _ in range(N):
    temp = list(map(int, input().split()))
    trash += sum(temp)  # 각 행에서 쓰레기의 개수를 더함
    pan.append(temp)


def clean():
    global trash

    last_cleaned_col = 0  # 마지막으로 청소된 열의 인덱스 / 이미 청소된 열은 다시 확인할 필요가 없으므로 이후 열 부터 청소
    for n in range(N):  # 각 행을 순차적으로 처리
        final_trash_col = last_cleaned_col  # 마지막 쓰레기가 있는 열을 기록할 변수
        for m in range(last_cleaned_col, M):  # 마지막 청소된 열부터 끝까지 확인
            if pan[n][m]:  # 쓰레기가 발견되면
                final_trash_col = m  # 해당 열을 마지막 쓰레기 열로 업데이트

        for m in range(last_cleaned_col, final_trash_col+1):  # 마지막 청소된 열부터 마지막 쓰레기 열까지 청소
            if pan[n][m]:  # 쓰레기가 있으면
                pan[n][m] = 0  # 쓰레기를 청소
                trash -= 1  # 남은 쓰레기 수를 1 줄임
        last_cleaned_col = final_trash_col  # 마지막 청소된 열을 업데이트


answer = 0
while trash:
    clean()
    answer += 1
print(answer)
