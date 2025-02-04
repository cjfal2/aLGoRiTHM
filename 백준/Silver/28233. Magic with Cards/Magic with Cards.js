const fs = require('fs');
const stdin = (
    process.platform === 'linux'
        ? fs.readFileSync('/dev/stdin').toString()
        : `1 1 1
`
)
    .trim()
    .split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

const [n, start, target] = input().trim().split(' ').map(Number);
const total = 2 * n; // 전체 카드 수임

// 시작 위치와 목표 위치가 같으면 바로 0을 출력함
if (start === target) {
    console.log(0);
    process.exit(0);
}

// pos(1-indexed)가 n 이하이면 새로운 위치는 2*pos - 1,
// pos가 n 초과이면 새로운 위치는 2*(pos - n)임.
const riffle = (pos) => {
    if (pos <= n) {
        return 2 * pos - 1;
    } else {
        return 2 * (pos - n);
    }
};

// pos가 홀수이면 pos+1, 짝수이면 pos-1로 이동함.
const scuffle = (pos) => {
    return (pos % 2 === 1) ? pos + 1 : pos - 1;
};

const visited = new Array(total + 1).fill(false);
const queue = []; // {pos, cnt}를 저장함
let head = 0;    // 큐의 시작 인덱스를 가리킴

queue.push({ pos: start, cnt: 0 });
visited[start] = true;

// BFS를 이용해 최소 셔플 횟수를 탐색함
while (head < queue.length) {
    const { pos, cnt } = queue[head++];
    const nextCnt = cnt + 1;

    // riffle 셔플 적용함
    const posRiffle = riffle(pos);
    if (posRiffle === target) {
        console.log(nextCnt);
        process.exit(0);
    }
    if (!visited[posRiffle]) {
        visited[posRiffle] = true;
        queue.push({ pos: posRiffle, cnt: nextCnt });
    }

    // scuffle 셔플 적용함
    const posScuffle = scuffle(pos);
    if (posScuffle === target) {
        console.log(nextCnt);
        process.exit(0);
    }
    if (!visited[posScuffle]) {
        visited[posScuffle] = true;
        queue.push({ pos: posScuffle, cnt: nextCnt });
    }
}

// 모든 경우를 탐색했음에도 목표에 도달하지 못하면 -1을 출력함
console.log(-1);
