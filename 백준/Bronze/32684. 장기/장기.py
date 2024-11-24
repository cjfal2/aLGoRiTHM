scores = {
    "차": 13,
    "포": 7,
    "마": 5,
    "상": 3,
    "사": 3,
    "졸": 2
}


def cal(arr):
    return (arr[0] * scores["차"] +
            arr[1] * scores["포"] +
            arr[2] * scores["마"] +
            arr[3] * scores["상"] +
            arr[4] * scores["사"] +
            arr[5] * scores["졸"])

choki = cal(list(map(int, input().split())))
eungyu = cal(list(map(int, input().split()))) + 1.5

if choki > eungyu:
    print("cocjr0208")
else:
    print("ekwoo")
