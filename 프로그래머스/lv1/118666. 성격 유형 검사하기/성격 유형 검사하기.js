function solution(survey, choices) {
    var answer = '';
    personal = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0,
    }
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    
    survey.map((type, index) => {
        if(choices[index] < 4){
            personal[type[0]] += score[choices[index]]
        }else{
            personal[type[1]] += score[choices[index]]
        }
    })
    
    result = Object.entries(personal)
    
    for (let i = 1; i<8; i+=2){
        if(result[i][1] > result[i-1][1]){
            answer += result[i][0]
            
        }else{
            answer += result[i-1][0]
        }
    }
    return answer;
}