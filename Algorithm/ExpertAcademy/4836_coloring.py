# 4836_색칠하기

t = int(input()) # 테스트케이스 입력

for tc in range(t): # 반복
    arr = [[0] * 10 for _ in range(10)]

    color_try = int(input()) # 색칠을 시도할 수

    for i in range(color_try): # 색칠 반복문 돌리기
        color_in = [] # 리스트 초기화
        color_in = list(map(int, input().split())) # 좌표
        x_str = color_in[0] # 세로좌표 시자점 초기화
        y_str = color_in[1] # 가로좌표 시작점 초기화
        x_end = color_in[2] # 세로좌표 끝
        y_end = color_in[3] # 가로좌표 끝

        while x_str <= x_end: # 세로가 끝 지점을 넘어가기 전까지 반복
            y_str = color_in[1] # 가로좌표를 매 반복마다 시작점으로 초기화
            while y_str <= y_end: # 가로좌표를 끝 지점을 넘어가기 전까지 반복
                arr[x_str][y_str] += color_in[4] # 색을 칠함(1 또는 2를 더해줌
                y_str += 1 # 가로 한칸 이동
            x_str += 1 # 세로 한칸 이동

    count = 0 # 보라색 칸 카운트

    for z in range(10): # 리스트를 처음부터 읽으며 보라색(3)을 찾음
        for x in range(10):
            if arr[z][x] == 3: # 만약 있을시 카운트 +1
                count += 1

    print(f'#{tc + 1} {count}')




