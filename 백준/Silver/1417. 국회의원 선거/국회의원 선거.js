const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5
    5
    10
    7
    3
    8
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let n = parseInt(input()); // 후보의 수
let dasom = parseInt(input()); // 다솜이 지지자

if (n === 1) {
  console.log(0);
} else {
  let inputArray = Array(n-1).fill(0).map(() => parseInt(input())); // 다솜이 안 지지자
  let answer = 0; // 매수
  
  inputArray.sort((a, b) => b - a); // 내림차순 정렬
  while (inputArray[0] >= dasom) {
    dasom += 1;
    inputArray[0] -= 1;
    answer += 1;
    inputArray.sort((a, b) => b - a);
  }
  console.log(answer);
}
