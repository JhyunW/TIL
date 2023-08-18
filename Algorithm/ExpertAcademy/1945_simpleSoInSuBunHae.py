# SW Expert
# 1945_간단한 소인수분해

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while num != 1:
        if num % 11 == 0:
            num = num // 11
            e += 1
        elif num % 7 == 0:
            num = num // 7
            d += 1
        elif num % 5 == 0:
            num = num // 5
            c += 1
        elif num % 3 == 0:
            num = num // 3
            b += 1
        elif num % 2 == 0:
            num = num //2
            a += 1
    result = [a, b, c, d, e]
    print(f'#{tc}', end = ' ')
    for i in result:
        print(i, end = ' ')
    print()