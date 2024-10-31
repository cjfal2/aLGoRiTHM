const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `9 3
1 2 3 4 5 6 7 8 9
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M]: number[] = input().trim().split(" ").map(Number);
const lectureInfo: number[] = input().trim().split(" ").map(Number);

let start: number = Math.max(...lectureInfo);
let end: number = lectureInfo.reduce((sum, val) => sum + val, 0);

while (start <= end) {
  let middle: number = Math.floor((start + end) / 2);
  let blueAmount: number = 1;
  let checkNumber: number = 0;

  for (let num of lectureInfo) {
    if (checkNumber + num <= middle) {
      checkNumber += num;
    } else {
      checkNumber = num;
      blueAmount += 1;
    }
  }
  if (blueAmount <= M) {
    end = middle - 1;
  } else {
    start = middle + 1;
  }
}
console.log(start);
