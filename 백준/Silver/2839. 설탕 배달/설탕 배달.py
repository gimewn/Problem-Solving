sugar = int(input())

result = 0

while sugar >= 0:

    if sugar % 5 == 0:

        result += sugar // 5

        print(result)

        break

    else:

        sugar -= 3

        result += 1

else:

    print(-1)