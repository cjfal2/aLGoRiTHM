def solution(sizes):
    answer = 0
    w, h = -10000000, -10000000
    for a, b in sizes:
        n, m = max(a, b), min(a, b)
        w, h = max(n, w), max(m, h)
    return w * h


'''
function solution(sizes) {
    let maxWidth = -Infinity, maxHeight = -Infinity
    sizes.forEach(([width,height])=>{
        const maxLength = Math.max(width,height)
        const minLength = Math.min(width,height)

        // 명함의 가로 세로중 긴 부분을 width로 저장
        maxWidth = Math.max(maxLength, maxWidth)
        maxHeight = Math.max(minLength, maxHeight) 
    })
    return maxWidth * maxHeight;
}
'''