const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `ABCD\nEFGH\nIJKL\nM.NO`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = 4;
const target = "ABCD" + "EFGH" + "IJKL" + "MNO.";
const pan = stdin.map(row => row.split(""));

function cal(pan, target) {
  let distance = 0;
  let position = {};

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      position[pan[i][j]] = [i, j];
    }
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      let targetChar = target[i * N + j];
      if (targetChar !== ".") {
        let [x, y] = position[targetChar];
        distance += Math.abs(x - i) + Math.abs(y - j);
      }
    }
  }

  return distance;
}

console.log(cal(pan, target));
