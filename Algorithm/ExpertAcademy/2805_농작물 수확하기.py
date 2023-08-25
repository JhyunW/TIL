# SW Expert
# 2805_농작물 수확하기

T = int(input())  # 테케
for tc in range(1, T+1):
    N = int(input())  # 배열크기(홀수)
    arr = []
    for i in range(N):
        arr.append(list(map(int, input())))
    result = 0
    center = N // 2  # 중앙 지점 체크
    center_move = -1
    count = 1  # 시작지점
    count_change = 2  # 카운트 늘려주는 변수
    if N == 1:
        result = arr[0][0]
    else:
        for q in range(N):
            for q1 in range(count):
                result += arr[q][center + q1]  # 센터에서부터
            if center == 0:
                center_move = center_move * -1
                count_change = count_change * -1
            center += center_move
            count += count_change

    print(f'#{tc} {result}')
