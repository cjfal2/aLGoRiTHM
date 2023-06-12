const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `2
`
).split('\n');
 
const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

input()%2 ? console.log("SK") : console.log("CY")