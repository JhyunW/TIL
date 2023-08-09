# N * M 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램

T = int(input())  # 테스트 횟수

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 글자판의 크기, 문자길이
    arr = [[0] * N for _ in range(N)]  #  N * N 배열 생성
    for i in range(N):  # 각 줄마다 문장 입력
        arr_in = str(input())
        for i_2 in range(N):
            arr[i][i_2] = arr_in[i_2]  # 각각의 자리에 글자 넣어주기
    result =''

    # 가로열 비교
    for q in range(N):
        for q_1 in range(N-M+1):
            x_str = ''
            for q_2 in range(M):
                x_str += arr[q][q_1 + q_2]
            if x_str == x_str[::-1]:
                result = x_str

    # 세로열 비교
    for w in range(N-M+1):
        for w_1 in range(N):
            y_str = ''
            for w_2 in range(M):
                y_str += arr[w+w_2][w_1]
            if y_str == y_str[::-1]:
                result = y_str

    print(f'#{tc} {result}')
