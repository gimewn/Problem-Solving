import sys
import heapq

def main():
    
    n = int(sys.stdin.readline())
    
    classes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    # 입력받은 수업 시간들을 heap으로 만들기
    heapq.heapify(classes)
    
    classroom = []
    
    roomcnt = 0
    
    while classes:
        # 시작 시간이 가장 빠른 (시작 시간이 동일하면 끝나는 시간이 가장 빠른)
        # 수업 하나 꺼내기
        now = heapq.heappop(classes)
        # 만약 classroom (heap)이 비어있지 않으면
        if classroom:
            # 현재 시작 시간과 classroom에 담긴 가장 빠른 시간 비교
            # 현재 시작 시간이 더 빠르면 강의실 개수 추가
            if now[0] < classroom[0]:
                roomcnt += 1
            # 현재 시작 시간과 같거나 현재 시작 시간이 더 늦으면 강의실 사용 가능
            else:
                heapq.heappop(classroom)
        # classroom이 비어 있으면 강의실 개수 추가
        else:
            roomcnt += 1
        # classroom이 비어 있으면 => 강의실 추가
        # 현재 시작 시간이 더 빠르면 => 강의실 추가
        # 현재 시작 시간과 같거나 더 늦으면 => 강의실 이용 가능,
        # 이전 시간 빼주고 현재 수업의 끝나는 시간 넣기
        heapq.heappush(classroom, now[1])
    
    print(roomcnt)

if __name__ == '__main__':
    main()