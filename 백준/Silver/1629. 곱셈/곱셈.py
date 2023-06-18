# 지수 법칙 : A ** (M+N) => A**M * A**N
# 나머지 분배 법칙 : (A*B)%C => ((A%C) * (B%C)%C

A, B, C = map(int, input().split())

def cal(a, b):
    if b == 1:
        return a % C

    value = cal(a, b//2)

    if b % 2 == 0:
        # b가 짝수라면 => b // 2 값을 C로 나눈 걸 2번 곱해주고, 다시 C로 나눠주면 됨
        return (value * value) % C
    else:
        # b가 홀수라면 => b // 2 값을 C로 나눈 걸 2번 곱해주고, 나눠지지 않은 a를 한 번 곱한 후, 다시 C로 나눠주면 됨
        return (value * value * a) % C

print(cal(A, B))