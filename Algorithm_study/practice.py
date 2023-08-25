# SW Expert
# 1216_회문2
# import sys
# sys.stdin = open('input.txt')
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

    end = 2
    for q in range(100):
        start = 0
        move = 0
        while end + start < 100:
            a = arr_x[q][start:end+move]
            b = arr_y[q][start:end+move]
            if a == a[::-1] or b == b[::-1]:
                best = end + move - start
                end = best  # 늘리고 그자리 다시 탐색
                end += 1
                move = 0
                start = 0
            else:
                move += 1
            if end + move >= 100:
                start += 1
                move = 0

    print(f'#{tc} {best}')