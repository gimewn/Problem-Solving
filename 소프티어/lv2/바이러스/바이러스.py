import sys

input = sys.stdin.readline

K, P, N = map(int, input().split())

answer = K

for _ in range(N):
    # answer = K * (P**N) % 1000000007
    # answer와 P를 차례로 곱하면서 나머지 연산 => 위 연산과 동일
    answer = (answer * P) % 1000000007

print(answer)