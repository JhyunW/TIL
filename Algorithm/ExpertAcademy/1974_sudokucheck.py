# SW Expert
# 1974_스도쿠 검증

T = int(input())  # 테케

for tc in range(1, T+1):
    arr = []
    for i in range(9):
        arr.append(list(map(str, input().split())))

    result = 1
    for q in range(9):  # 가로열
        if result == 0:
            break
        a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for w in arr[q]:
            if w in a:
                a.remove(w)
            else:
                result = 0
                break

    for e in range(9):  # 세로열
        if result == 0:
            break
        a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for r in range(9):
            if arr[r][e] in a:
                a.remove(arr[r][e])
            else:
                result = 0
                break

    for t in range(0, 9, 3):
        for t1 in range(0, 9, 3):
            # print(f'T와 T1{t}, {t1}')
            if result == 0:
                break
            a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for y in range(3):
                for y1 in range(3):
                    # print(f'Y와Y1{y}, {y1}')
                    if arr[t+y][t1+y1] in a:
                        a.remove(arr[t+y][t1+y1])
                    else:
                        result = 0
                        break
    print(f'#{tc} {result}')