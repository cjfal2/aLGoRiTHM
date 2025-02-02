const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
_
A
3
I_LOVE_THE_CCC`
)
  .trim()
  .split("\n");

const input = (() => {
  let index = 0;
  return () => stdin[index++];
})();

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_";
const cipherMap = Array.from({ length: 27 }, () => input());
const repeatCount = parseInt(input(), 10);
let message = input();

let currentCipher = cipherMap.slice();
let result = message;
let count = repeatCount;

while (count > 0) {
  if (count % 2 === 1) {
    result = result.split('').map(char => currentCipher[letters.indexOf(char)]).join('');
  }
  count = Math.floor(count / 2);
  currentCipher = currentCipher.join('').split('').map(char => currentCipher[letters.indexOf(char)]);
}

console.log(result);
