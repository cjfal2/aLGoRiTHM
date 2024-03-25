function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    
    const visited = Array.from(Array(n), () => Array(m).fill(0));
    visited[0][0] = 1
    
    const q = [[0, 0]];
    
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (q.length > 0) {
        const [x, y] = q.shift();
        if (x === n-1 && y === m-1) {
            return visited[x][y];
        }
        for (let [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;
            if (
                n > nx &&
                nx >= 0 &&
                m > ny &&
                ny >= 0 &&
                maps[nx][ny] === 1 &&
                visited[nx][ny] === 0
            ) {
                q.push([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
            }
        }
    }
    
    return -1;
}