// 두 개 뽑아서 더하기

// 1. 첫번째 풀이 
function solution(numbers) {
    let ans = []
    for(var i=0; i<numbers.length; i++ ){
        for(var j=i+1; j<numbers.length; j++ ){
            if (ans.indexOf(numbers[i]+numbers[j])<0){
               ans.push(numbers[i]+numbers[j])
            }
        } 
    }
    ans.sort((a, b) => a - b);
    return ans
}


// 2. 두번째 풀이
// spread operaor, set 사용
function solution(numbers) {
    const temp = []

    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            temp.push(numbers[i] + numbers[j])
        }
    }

    const answer = [...new Set(temp)]

    return answer.sort((a, b) => a - b)
}
