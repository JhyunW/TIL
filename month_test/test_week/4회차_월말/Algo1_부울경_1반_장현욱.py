# 풍선팡
# 상하좌우 4방향 비교를 위한 수
move_x = [-1, 0, 1, 0]  # 위 왼 아 오
move_y = [0, -1, 0, 1]


T = int(input())  # 테스트케이스

for tc in range(1, T+1):
    N = int(input())  # 배열크기
    arr = []  # 배열 값을 적어놓을곳
    for i in range(N):  # 각 칸마다 숫자 입력
        arr.append(list(map(int, input().split())))

    high = 0  # 가장 큰 값
    low = 999  # 가장 작은 값
    for q in range(N):  # 각 배열을 하나하나 돌기 위한 칸
        for q1 in range(N):
            now = arr[q][q1]  # 현재 위치의 점수
            for w in range(1, arr[q][q1] + 1):  # 해당 칸의 숫자만큼 펼치기위함
                for move in range(4):  # 상하좌우 비교를 위함
                    mx, my = q + (move_x[move] * w), q1 + (move_y[move] * w)
                    if 0 <= mx < N and 0 <= my < N:  # 배열 범위를 벗어나지 않을경우
                        now += arr[mx][my]  # 범위만큼의 숫자를 더함
            if now > high:  # 현재 더한 값이 최고점보다 높을시
                high = now
            if now < low:  # 현재 더한 값이 최소점보다 낮을시
                low = now

    result = high - low  # 최대점수와 최소점수의 차

    print(f'#{tc} {result}')