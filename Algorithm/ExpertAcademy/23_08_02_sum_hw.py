t = 10

arr = [[0] * 100 for i in range(100)] # 2차원 리스트 생성

for tc in range(t): # 테스트 케이스 10번 박복

    test_num = int(input()) # 몇번째 실험인지 입력 받기

    for z in range(100): # 100줄 각 리스트에 들어갈 숫자 입력
        arr[z] = list(map(int, input().split()))

    big_x_y = 0 # 가로 세로열을 총 비교하고 가장 큰 숫자 출력
    cross_l_r = 0 # 왼쪽에서 오른쪽으로 가는 대각선 총 합
    cross_r_l = 0 # 오른쪽에서 왼쪽 가는 대각선 총 합

    for x in range(100): # 100줄 각 x와 y의 합, 대각선의 합을 구하는 반복문
        x_plus = 0 # 한 줄 끝날때마다 초기화
        y_plus = 0
        cross_l_r += arr[x][x]
        cross_r_l += arr[99-x][99-x]

        for c in range(100):
            x_plus += arr[x][c]
            y_plus += arr[c][x]

        if big_x_y < x_plus: # 가로와 세로의 크기를 비교하여 가장 큰 숫자 뽑기
            big_x_y = x_plus

        if big_x_y < y_plus:
            big_x_y = y_plus

    if big_x_y < cross_l_r: # 가로세로에서 가장 높은 숫자와 대각선 합 비교
        big_x_y = cross_l_r

    if big_x_y < cross_r_l:
        big_x_y = cross_r_l

    print(f'#{test_num} {big_x_y}')