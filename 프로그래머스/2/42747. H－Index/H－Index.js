function solution(citations) {
    
    const checkCitations = (value) => {
        const count = citations.reduce((acc, cur) => acc += cur >= value, 0);
        
        return count >= value ? true : false;
    }
    
    var answer = 0;
    
    citations.sort((a, b) => a - b);
    
    let [s, e] = [0, citations.at(-1)];
    
    while(s <= e){
        const mid = Math.floor((s + e) / 2);
        
        if(checkCitations(mid)){
            answer = mid;
            s = mid + 1;
        }else{
            e = mid - 1;
        }
    }
    
    return answer;
}