n = int(input())

def hanoi(num, start, destination, other):
    if num == 1:
        print(start, destination)
        return
    hanoi(num-1, start, other, destination) # num-1개의 원반을 2번으로 옮기기
    print(start, destination) # num번 원반을 3번으로 옮기기
    hanoi(num-1, other, destination, start) # num-1개의 원반을 3번으로 옮기기

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)