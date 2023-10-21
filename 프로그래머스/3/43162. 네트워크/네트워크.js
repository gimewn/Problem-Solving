function solution(n, computers) {
    const length = computers.length;
    const visit = new Array(length).fill(0);
    let cnt = 1;
    
    const dfs = (now, cnt) => {
        computers[now].forEach((item, index) => {
            if(index !== now && item && !visit[index]){
                visit[index] = cnt;
                dfs(index, cnt);
            }
        })
    }
    
    computers.forEach((item, index) => {
        if(!visit[index]){
            visit[index] = cnt;
            dfs(index, cnt);
            cnt += 1;
        }
    })
    
    return cnt - 1;
}