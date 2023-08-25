# SW Expert
# 1216_회문2

for t in range(1, 11):
    tc = int(input())  # 테스트 케이스 번호
    arr_x = []  # 정식배열
    arr_y = []
    best = 1
    for i in range(100):  # x배열
        arr_x.append(input())  # 리시트 글자추가
    for i1 in range(100):
        trash = ''
        for i2 in range(100):  # 회전배열
            trash += arr_x[i2][i1]
        arr_y.append(trash)

    start = 0
    end = 2

    for q in range(100):
        move = 0
        while end + move < 100:
            a = arr_x[q][move:end+move]
            b = arr_y[q][move:end+move]
            if a == a[::-1] or b == b[::-1]:
                if best < end:
                    best = end
                end += 1  # 늘리고 그자리 다시 탐색

            else:
                move += 1

    print(f'#{tc} {best}')

