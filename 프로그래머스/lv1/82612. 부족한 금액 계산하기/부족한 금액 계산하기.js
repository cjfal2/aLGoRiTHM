function solution(price, money, count) {
    let cnt = 1
    let temp = 0
    while (cnt <= count) {
        temp = cnt * price
        money -= temp
        cnt += 1
    }
    if (money < 0) {
        return money * -1
    } else {
        return 0
    }
}