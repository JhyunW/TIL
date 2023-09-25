T = int(input())  # 테스트케이스

move_x = [-1, 0, 1, 0]  # 위 왼 아 오 순서
move_y = [0, -1, 0, 1]

for tc in range(1, T+1):  # 테스트 반복
    N = int(input())  # N * N배열 값 입력

    arr = [[]for _ in range(N)]  # N개의 열 생성

    for i in range(N):  # N개으 줄에 숫자 입력
        arr[i] = list(map(int, input().split()))

    count = 0  # 봉우리의 갯수 카운팅 할 변수

    for x in range(N):
        for y in range(N):
            center = arr[x][y]  # 기준점의 높이

            no = 0  # 주위에 같거나 더 높은 산이 있으면 카운트 되어 봉우리가 아님을 표시

            for move in range(4):
                xx, yy = x + move_x[move], y + move_y[move]
                if 0 <= xx < N and 0 <= yy < N:
                    if center <= arr[xx][yy]:
                        no += 1
            if no == 0:
                count += 1

    print(f'#{tc} {count}')
