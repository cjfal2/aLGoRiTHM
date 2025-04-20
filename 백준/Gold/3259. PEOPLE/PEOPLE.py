N = int(input())
statements = []

for _ in range(N):
    true_line = list(map(int, input().split()))
    false_line = list(map(int, input().split()))
    truths = true_line[1:] if true_line[0] > 0 else []
    lies = false_line[1:] if false_line[0] > 0 else []
    statements.append((truths, lies))

def is_valid(config):
    for i in range(N):
        is_true = (config >> i) & 1
        truths, lies = statements[i]
        if is_true:  # 이 사람이 진실을 말한다면
            for t in truths:
                if ((config >> (t - 1)) & 1) == 0:
                    return False
            for f in lies:
                if ((config >> (f - 1)) & 1) == 1:
                    return False
        else:  # 이 사람이 거짓말을 한다면
            one_lie = False
            for t in truths:
                if ((config >> (t - 1)) & 1) == 0:
                    one_lie = True
            for f in lies:
                if ((config >> (f - 1)) & 1) == 1:
                    one_lie = True
            if not one_lie:
                return False
    return True

for config in range(1 << N):
    if is_valid(config):
        for i in range(N):
            print("true" if ((config >> i) & 1) else "false")
        break
