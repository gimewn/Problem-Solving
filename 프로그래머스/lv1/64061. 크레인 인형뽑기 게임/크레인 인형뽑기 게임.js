function solution(board, moves) {
    var answer = 0;
    let len = board.length;
    let basket = [];
    function crain(col){
        for (let row = 0; row<len; row++){
            // 열의 0이 아닌 최초의 값 => 맨 위에 있는 인형
            if(board[row][col] !== 0){
                let tmp = board[row][col];
                // 뽑았으니까 0으로 초기화
                board[row][col] = 0;
                return tmp
            }
        }
    }
    function removeDoll(doll){
        // basket이 빈 배열이면 비교할 대상 없으므로
        if(!basket){
            // 그냥 넣어줌
            basket.push(doll)
        }else{
            // 마지막 인덱스 계산
            let bask_len = basket.length-1;
            // 마지막 원소가 새로 뽑은 인형과 동일하다면
            if(basket[bask_len] === doll){
                // 마지막 원소 삭제
                basket.pop();
                // answer에 2 더해주기
                answer += 2;
            }else{
                // 같지 않으면 배열에 새로 뽑은 인형 넣어주기
                basket.push(doll)
            }
        }
    }
    // moves 배열 순회하면서 인형 뽑고 => 바구니 검사 실행
    moves.forEach((seq) => {
        let ans = crain(seq-1);
        // 인형을 뽑았다면 (undefined가 아니라면)
        if(ans){
            // 바구니 검사
            removeDoll(ans)   
        }
    })
    return answer;
}