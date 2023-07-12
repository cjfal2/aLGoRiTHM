const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `15 15
    2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
    1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
    1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().trim().split(" ").map(Number);
const answer = Array.from(Array(N), () => Array(M).fill(0));
const pan = [];
let flag = true;
const q = [];
let sx = 0;
let sy = 0;

for (let n = 0; n < N; n++) {
  const arr = input().trim().split(" ").map(Number);
  if (flag) {
    for (let m = 0; m < M; m++) {
      if (arr[m] === 2) {
        flag = false;
        answer[n][m] = 1;
        sx = n;
        sy = m;
        q.push([n, m, 0]);
      }
    }
  }
  pan.push(arr);
}

function bfs() {
  while (q.length > 0) {
    const [x, y, distance] = q.shift();
    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];

    for (const [dx, dy] of directions) {
      const nx = x + dx;
      const ny = y + dy;

      if (N > nx && nx >= 0 && M > ny && ny >= 0 && answer[nx][ny] === 0 && pan[nx][ny] === 1) {
        answer[nx][ny] = distance + 1;
        q.push([nx, ny, distance + 1]);
      }
    }
  }

  answer[sx][sy] = 0;
}

function printAnswer() {
  for (let n = 0; n < N; n++) {
    let line = "";
    for (let m = 0; m < M; m++) {
      if (pan[n][m] === 1 && answer[n][m] === 0) {
        line += "-1";
      } else {
        line += answer[n][m].toString();
      }

      if (m < M - 1) {
        line += " ";
      }
    }

    console.log(line);
  }
}


bfs();
printAnswer();