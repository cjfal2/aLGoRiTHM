const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5
    6 9 5 7 4
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const towers = input().trim().split(" ").map(Number);
const stack = [[1, towers[0]]]; // 첫 번째 타워를 스택에 넣어줌
const answer = Array(N).fill(0); // 정답 배열, 아무 것도 안받으면 0이 되는 것

for (let idx = 1; idx < N; idx++) { // 첫 번째를 넣어줬기 때문에 1부터 시작, idx는 타워의 위치
  while (stack.length > 0 && stack[stack.length - 1][1] < towers[idx]) {
    // 스택에 뭐가 있거나 스택의 마지막의 타워가 다음 타워보다 작을때만 스택을 팝해준다.
    // 그러면 스택에 남은 마지막 타워 정보는 현재 idx거보다 큰 게 된다. 그 타워가 레이저를 받는 타워
    stack.pop();
  }
  if (stack.length > 0) {
    // 스택에 뭐가 있으면, 정답 배열에 그 스택 마지막에 있는 idx를 저장한다.
    answer[idx] = stack[stack.length - 1][0];
  }
  stack.push([idx + 1, towers[idx]]); // 지금 idx의 타워를 스택에 넣는다.
}

console.log(answer.join(" "));
