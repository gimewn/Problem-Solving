function solution(numbers, target) {
    var answer = 0;
    const length = numbers.length;
    
    const dfs = (level, res) => {
        if(level >= length){
            if(res === target){
                answer += 1;
            }
            return;
        }
        
        dfs(level+1, res + numbers[level]);
        dfs(level+1, res + numbers[level]*(-1));
    }
    
    dfs(0, 0);
    return answer;
}