function solution(jobs) {
    
    var answer = 0;
    
    const heap = [];
    
    let time = 0;
    let j = 0;
    
    jobs.sort((a, b) => a[0] - b[0]);
    
    while(jobs.length > j || heap.length !== 0){
        // 현재 진행 중인 작업의 끝나는 시간보다 빨리 요청된 작업이 있으면 heap에 넣기
        if(jobs.length > j && time >= jobs[j][0]){
            heap.push(jobs[j]);
            j += 1;
            // 종료까지 걸리는 시간을 기준으로 오름차순
            heap.sort((a, b) => a[1] - b[1]);
            continue;
        }
        // 종료까지 걸리는 시간이 적은 것부터 꺼내서 실행
        if(heap.length > 0){
            time += heap[0][1];
            answer += time - heap[0][0];
            heap.shift();
        }else{
            time = jobs[j][0];
        }
    }
    
    return Math.floor(answer / jobs.length);
}