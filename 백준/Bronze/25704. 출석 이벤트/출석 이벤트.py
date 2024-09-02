N = int(input())
total = int(input())
answer = [total]
if N >= 5:
    answer.append(total-500)

if N >= 10:
    answer.append(int(total*0.9))

if N >= 15:
    answer.append(total-2000)

if N >= 20:
    answer.append(int(total*0.75))
answer.sort()
print(answer[0] if answer[0] > 0 else 0)