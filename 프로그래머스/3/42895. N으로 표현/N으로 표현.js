function solution(N, number) {
    const joinN = (count) => {
        let stringN = '';
        for(let i=0; i<count; i++){
            stringN += String(N);
        }
        return stringN
    }
    var answer = Infinity;
    const dp = new Array(10).fill(0).map(() => new Set())
    
    for(let i=1; i<10; i++){
        dp[i].add(Number(joinN(i)))
        for(let j=1; j<i; j++){
            dp[j].forEach((x) => {
                dp[i-j].forEach((y) => {
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if(x){
                        dp[i].add(Math.floor(x / y))
                    }
                })
            })
        }
        if(dp[i].has(number)){
            if(i <= 8){
                return i;
            }
        }
    }
    
    return -1
}