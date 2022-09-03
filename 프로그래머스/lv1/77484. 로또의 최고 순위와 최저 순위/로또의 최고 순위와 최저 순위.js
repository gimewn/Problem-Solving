function solution(lottos, win_nums) {
    var answer = [];
    var cnt = 0;
    var zero = 0;
    var grade = [6, 6, 5, 4, 3, 2, 1];
    lottos.map((num) => {
        if(win_nums.includes(num)){
            cnt += 1;
        }
        else if(num === 0){
            zero += 1;
        }
    })
    answer = [grade[cnt+zero], grade[cnt]]
    return answer;
}