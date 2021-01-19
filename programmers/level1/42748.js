// k번째수

// 1번째 풀이
// 숫자 배열 -> .sort()로 하면 문자열배열 규칙에 따름
function solution(array, commands) {
    let ans = []
    for(var i=0; i<commands.length; i++){
        const a = commands[i];
        let A = array.slice(a[0]-1,a[1]).sort((a,b)=>{return a-b});
        ans.push(A[a[2]-1])
    }
    return ans
}

// 2번째 풀이
// for문 대신, map을 이용해 commands배열 탐색
function solution(array, commands) {
    let ans = []
    commands.map(command => {
        const [sPosition, ePosition, position] = command
        let A = array.slice(command[0]-1,command[1]).sort((a,b)=>{return a-b})
        ans.push(A[command[2]-1])
    })
    return ans
}
