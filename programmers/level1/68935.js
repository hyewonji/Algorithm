// 3번 뒤집기

// 1번째 풀이
function solution(n) {
    let ans = n.toString(3).split("").reverse().join("")
    return Number.parseInt(ans,3)
};


// 2번째 풀이
// separate operation 사용
const solution = (n) => {
    return parseInt([...n.toString(3)].reverse().join(""), 3);
}
