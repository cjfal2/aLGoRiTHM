const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `BAAAAABAA
    BAABAAAAAB
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const start = input().trim();
const startLength = start.length;
const target = input().trim();
const targetLength = target.length;
let answer = 0;

function reverse(word) {
  const reversedWord = word.split("").reverse().join("");
  return minus(reversedWord);
}

function minus(word) {
  return word.substring(0, word.length - 1);
}

function dfs(word, len) {
  if (answer === 1) return;
  if (word === start) answer = 1;
  if (len === startLength) return;
  if (word[word.length - 1] === "A") dfs(minus(word), len - 1);
  if (word[0] === "B") dfs(reverse(word), len - 1);
}

dfs(target, targetLength);
console.log(answer);
