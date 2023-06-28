const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5 5
    1 3
    1 4
    4 5
    4 3
    3 2
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().trim().split(" ").map(Number)
const friends = Array.from(Array(N+1), () => Array())
for (let i = 0; i < M; i++) {
  const [A, B] = input().trim().split(" ").map(Number)
  friends[A].push(B)
  friends[B].push(A)
}


let answer_person = [101, 999999999]; // 사람 번호, 케빈베이컨수

// 플로이드 워셜
for (let who = 1; who < N+1; who++) {
  let number = 0;
  for (let to = 1; to < N+1; to++) {
    if (who === to) continue

    let visitedBase = Array(N+1).fill(false)
    visitedBase[who] = true
    let queue = [[who, 0]]
    while (queue.length > 0) {
      let base = queue.shift()
      let x = base[0]
      let count = base[1]
      if (x === to) {
        number += count
        break
      }

      friends[x].forEach(element => {
        if (!visitedBase[element]) {
          queue.push([element, count+1])
          visitedBase[element] = true
        }
      });
    }
  }

  if (number < answer_person[1]) {
    answer_person[0] = who
    answer_person[1] = number
  } else if (number === answer_person[1]) {
    answer_person[0] = Math.min(who, answer_person[0])
  }
}
console.log(answer_person[0])

