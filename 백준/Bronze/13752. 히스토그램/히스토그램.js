const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `5
    1
    3
    4
    6
    2
`
).split('\n');
 
const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();
 
let t = input();
while (t--) {
    const a = parseInt(input());
    const ans = "=".repeat(a)
    console.log(ans);
}