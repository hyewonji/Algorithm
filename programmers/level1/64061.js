//크레인 인형뽑기 게임

function solution(b, m) {
    
    let stacklist = [];
    let answer = 0;
    const bl = b.length;
    const ml = m.length;
    
    for (var i = 0; i < ml; i++){
        for (var j = 0; j < bl; j++){
            if (b[j][m[i]-1] !== 0){
                stacklist.push(b[j][m[i]-1])
                b[j][m[i]-1] = 0
                if (stacklist.length > 1){
                    if (stacklist[stacklist.length-1] === stacklist[[stacklist.length-2]]){
                        stacklist.pop()
                        stacklist.pop()
                        answer += 2 
                    }
                }
                break
            }
        }
    };

    return answer
}
