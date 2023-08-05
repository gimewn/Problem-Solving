import sys
from itertools import combinations

def dfs(now, same_group, check):
    for next_city in city_connect[now]:
        if next_city in same_group and not check[next_city]:
            check[next_city] = 1
            dfs(next_city, same_group, check)

    return check

def check_group(group):
    check = [0]*(N+1)
    first = list(group)[0]
    check[first] = 1

    dfs(first, group, check)

    for g in group:
        if not check[g]:
            return False

    return True

def cal_population(group):
    all_count = 0
    for g in group:
        all_count += population[g]
    return all_count

N = int(input())

city = set(num for num in range(1, N+1))

population = [0] + list(map(int, sys.stdin.readline().split()))

city_connect = [[] for _ in range(N+1)]

answer = 2e9

for idx in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    city_connect[idx+1] = temp[1:]

for i in range(1, (N//2)+1):
    combination_set = list(map(set, combinations(city, i)))
    for group1 in combination_set:
        group2 = city ^ group1
        check_group1 = check_group(group1)

        if check_group1:
            check_group2 = check_group(group2)

        if check_group1 and check_group2:
            group1_population = cal_population(group1)
            group2_population = cal_population(group2)
            answer = min(answer, abs(group2_population - group1_population))

if answer == 2e9:
    print(-1)
else:
    print(answer)