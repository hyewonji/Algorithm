// 체육복

function solution(n, lost, reserve) {
    let ans = n - lost.length

    for (var i=0; i<lost.length; i++){
        if(reserve.indexOf(lost[i])>-1){
            reserve.splice(reserve.indexOf(lost[i]),1)
            lost.splice(i,1)
            ans += 1
        } 
    }
    
    for(var i=0; i<lost.length; i++){
        if((lost[i]>1) && (reserve.indexOf(lost[i]-1)>-1)){
            reserve.splice(reserve.indexOf(lost[i]-1),1)
            ans += 1
            console.log(lost[i],"-")
        } else if((lost[i]<n) && (reserve.indexOf(lost[i]+1)>-1)){
            reserve.splice(reserve.indexOf(lost[i]+1),1)
            ans += 1
            console.log(lost[i],"+")
        }
    }
    return ans;
}
