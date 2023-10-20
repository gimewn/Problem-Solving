function solution(maps) {
    const direction = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    const X = maps.length;
    const Y = maps[0].length;
    const visited = Array.from(Array(X), () => new Array(Y));
    
    const queue = [];
    
    queue.push([0, 0, 1]);
    visited[0][0] = 1;
    
    while(queue.length){
        const [nx, ny, ncount] = queue.shift();
        if(nx === X-1 && ny == Y-1){
            return ncount
        }
        direction.forEach(([i, j]) => {
            const dx = nx + i;
            const dy = ny + j;
            if(dx < 0 || dx >= X || dy < 0 || dy >= Y || visited[dx][dy] === 1 || maps[dx][dy] === 0){
                return;
            }else{
                visited[dx][dy] = 1;
                queue.push([dx, dy, ncount+1]);
            }
        })
    }
    
    return -1;
}