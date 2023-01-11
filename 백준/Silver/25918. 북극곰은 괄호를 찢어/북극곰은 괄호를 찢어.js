const fs = require('fs');
const [N, S] = fs.readFileSync("/dev/stdin").toString().trim().split(/\n/);

let day = 0
let temp = 0

for (let i = 0; i < N; i++) {
  if (S[i] === "(") {
    temp += 1
  } else {
    temp -= 1
  }

  day = Math.max(Math.abs(temp), day)
}

console.log(temp === 0 ? day : -1);