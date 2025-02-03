const fs = require('fs');
const stdin = (
    process.platform === 'linux'
        ? fs.readFileSync('/dev/stdin').toString()
        : `10 5
1 3 4 5 6 7 8 10 12 14
`
)
    .trim()
    .split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

const [N, M] = input().trim().split(' ').map(Number);
const arr = input().split(' ').map(Number);

let maxSize = 0;

const snowballing = (now, size, time) => {
    if (now >= N - 1 || time === M) {
        maxSize = Math.max(maxSize, size);
        return;
    }

    if (now + 1 < N) {
        const newSize = size + arr[now + 1];
        snowballing(now + 1, newSize, time + 1);
    }

    if (now + 2 < N) {
        const newSize = Math.floor(size / 2) + arr[now + 2];
        snowballing(now + 2, newSize, time + 1);
    }
};

snowballing(-1, 1, 0);
console.log(maxSize);
