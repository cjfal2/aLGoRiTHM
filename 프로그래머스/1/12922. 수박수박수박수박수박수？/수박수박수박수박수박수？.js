function solution(n) {
    if (n === 1) {
        return "수";
    }
    else if (n === 2) {
        return "수박";
    }
    else if (n%2) {
        console.log(Math.floor(n/2));
        return "수" + "박수".repeat(Math.floor(n/2));
    }
    return "수박".repeat(Math.floor(n/2));
}