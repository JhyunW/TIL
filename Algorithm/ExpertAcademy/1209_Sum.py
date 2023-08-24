# SW Expert
# 1209_Sum


def find():
    best = 0
    cross_l = 0
    cross_r = 0
    for q in range(100):
        now_y = 0
        now_x = 0
        for q1 in range(100):
            now_y += arr[q][q1]
            now_x += arr[q1][q]
            if q == q1:
                cross_l += arr[q][q1]
            if q + q1 == 99:
                cross_r += arr[q][q1]
        if now_y > best:
            best = now_y
        if now_x > best:
            best = now_x
    if cross_l > best:
        best = cross_l
    if cross_r > best:
        best = cross_r
    return best

for test in range(1, 11):
    tc = int(input())  # 테케 번호
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    print(f'#{tc} {find()}')