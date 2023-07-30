function solution(rectangle, characterX, characterY, itemX, itemY) {
    var answer = 0;
    
    // 상하좌우 4방향
    const dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
	
    // board 생성 (꺾이는 부분을 위해 *2)
	let board = Array.from({ length: 103 }, () => Array(103).fill(0));
    
    // 꺾이는 부분을 위해 *2
    let doubleRec = rectangle.map(rec => rec.map(item => item*2));
    
    // 테두리면 1, 내부이면 2로 기록
    doubleRec.forEach(([x1, y1, x2, y2]) => {
        for (let i = x1; i <= x2; i++) {
          for (let j = y1; j <= y2; j++) {
            if (i === x1 || i === x2 || j === y1 || j === y2) {
              if (board[i][j] === 0) board[i][j] = 1;
            } else {
              board[i][j] = 2;
            }
          }
        }
    });
    
    // q에 캐릭터 위치 담기
    let q = [[characterX*2, characterY*2, 0]];
    
    // 캐릭터 위치 -> 0으로 변경, 재방문 막기
    board[characterX*2][characterY*2] = 0;

    while(q.length){
        let [nowX, nowY, nowCnt] = q.shift();
        
        // 현재 위치가 아이템 위치와 같으면 answer = 현재 cnt/2 (*2 했으므로)
        if(nowX === itemX*2 && nowY === itemY*2){
            answer = nowCnt/2;
            break
        }
        
        // 상하좌우 체크 -> 이동가능한 경우 이동
        for(let idx=0; idx<4; idx++){
            let nextX = nowX+dir[idx][0];
            let nextY = nowY+dir[idx][1];
            if(nextX < 103 && nextY < 103 && board[nextX][nextY] === 1){
                board[nextX][nextY] = 0;
                q.push([nextX, nextY, nowCnt+1])
            }
        }
        
    }
    return answer;
}