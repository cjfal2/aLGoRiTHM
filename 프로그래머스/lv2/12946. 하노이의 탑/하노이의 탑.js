function solution(n) {
    function temp(N) {
        const result = [];
        function hanoi(num, x, y) {
            if (num > 1) hanoi(num-1, x, 6-x-y)
            result.push([x, y])
            if (num > 1) hanoi(num-1, 6-x-y, y)
        }
        hanoi(N, 1, 3)
        return result
    }
    return temp(n)
}