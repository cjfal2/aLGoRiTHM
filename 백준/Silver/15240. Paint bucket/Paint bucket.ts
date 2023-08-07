const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `4 7
    0000000
    0111000
    0111010
    0000000
    0 0 3
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const directions: number[][] = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];
const [N, M]: number[] = input().trim().split(" ").map(Number);
const paint: number[][] = [];
const visited: boolean[][] = Array.from(Array(N), () => Array(M).fill(false));
for (let t = 0; t < N; t++) {
  const i: number[] = input().trim().split("").map(Number);
  paint.push(i);
}
const [n, m, w]: number[] = input().trim().split(" ").map(Number);
const f: number = paint[n][m];
paint[n][m] = w;
visited[n][m] = true;
const queue: number[][] = [[n, m]];
while (queue.length > 0) {
  const q: number[] | undefined = queue.shift(); // 배열 q가 비어있으면 undefined이므로 두개를 선언해줘야한다. 하지만 없는경우는 없다.
  if (q) {
    // 없는경우가 있을 수 있다는 멍청한 타입스크립트 때문에 if로 값이 있을 때만 해줘야 한다.
    const x: number = q[0];
    const y: number = q[1];
    directions.forEach((d) => {
      const nx: number = x + d[0];
      const ny: number = y + d[1];
      if (
        N > nx &&
        nx >= 0 &&
        M > ny &&
        ny >= 0 &&
        paint[nx][ny] === f &&
        !visited[nx][ny]
      ) {
        paint[nx][ny] = w;
        visited[nx][ny] = true;
        queue.push([nx, ny]);
      }
    });
  }
}

paint.forEach((answer) => {
  console.log(answer.join(""));
});
