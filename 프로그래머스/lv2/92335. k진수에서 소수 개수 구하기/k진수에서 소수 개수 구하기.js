function solution(n, k) {
    var answer = 0;
    let num = n.toString(k);
    let choicePN = num.split("0");
    
    function isPrime(num){
        for (let idx=2; idx<=Math.sqrt(num); idx++){
            if(num%idx === 0){return 0}
        }
        return 1
    }
    
    choicePN.forEach((item)=>{
        if(Number(item) > 1){
            answer += isPrime(Number(item));
        }
    })
    
    return answer;
}