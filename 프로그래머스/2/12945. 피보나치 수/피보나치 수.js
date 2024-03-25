function solution(n) {
    const fibo = Array(n+1).fill(0);
    fibo[1] = 1;
    for (let i = 2; i < n+1; i++) {
        fibo[i] = (fibo[i-2] + fibo[i-1]) % 1234567
    }
    return fibo[n];
}