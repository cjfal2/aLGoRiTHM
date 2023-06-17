const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1020
    0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const M = parseInt(input());
const brokenButtons = input().trim().split(" ").map(Number);

// 최소 횟수, 지금에서 +, -만 사용하는 경우를 디폴트로
let minClick = Math.abs(100 - N);
if (M === 0) {
  minClick = Math.min(minClick, N.toString().length);
}
for (let nums = 0; nums <= 1000001; nums++) {
  const numsStr = nums.toString();

  for (let j = 0; j < numsStr.length; j++) {
    // 각 자리의 숫자 확인 후, 고장 났으면 스킵
    if (brokenButtons.includes(parseInt(numsStr[j]))) {
      break;
    }

    // 고장난 숫자가 없다면 최소 횟수 
    else if (j === numsStr.length - 1) {
      minClick = Math.min(minClick, Math.abs(nums - N) + numsStr.length);
    }
  }
}

console.log(minClick);
