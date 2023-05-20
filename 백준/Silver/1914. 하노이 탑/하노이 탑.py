n = int(input())

def hanoi(num, start, destination, other):
    if num == 1:
        print(start, destination)
        return
    hanoi(num-1, start, other, destination) # n-1개의 원반을
    print(start, destination) # n
    hanoi(num-1, other, destination, start)

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)