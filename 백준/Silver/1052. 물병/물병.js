const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();
// 인풋 처리를 위한 코드


let [N, K] = input().split(" ").map(Number); // N: 주어진 물병의 수, K: 한 번에 옮길 수 있는 물병의 수(제한)
let answer = 0; // 구매한 물병의 수
while (true) { 
  let cnt = 0; // 가져갈 물병 (짝이 맞지 않는 애)
  let temp = N; // 임시 총 물병의 수

  while (temp > 0) { // 물병이 남아 있을 때만
    cnt += (temp % 2) // 물병이 홀수일 때는 물병 하나를 가져간다.
    temp = Math.floor(temp / 2) // 같은 양의 물을 합치는 과정
    if (cnt > K) { // 가져가는 양이 K보다 많으면 멈춘다.
      break
    }
  }

  if(cnt <= K) { // 가져가는 물병의 양이 K를 넘지 않았으면 출력후 종료
    console.log(answer)
    break
  }
  answer += 1 // 구매한 물병에 +1
  N += 1 // 총 물병수도 +1
}

