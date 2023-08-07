T = int(input())  # 테스트 케이스

for tc in range(1, T + 1):
    N = int(input())  # 평지의 크기
    arr = [[0] * N for _ in range(N)]  # N * N 크기의 땅 생성

    x, y, x_end, y_end = map(int, input().split())  # 평탄화 할 범위 설정

    for num in range(N):  # 각각의 공간에 숫자 입력
        arr[num] = list(map(int, input().split()))

    all_plus = 0  # 최종 평탄할 공간의 높이 총 합
    green_len = 0  # 평탄화 할 공간의 크기
    for q in range(x, x_end + 1):  # 평탄화 공간 x,y ~ x_end, y_end 까지의 높이 합
        for w in range(y, y_end + 1):
            all_plus += arr[q][w]
            green_len += 1

    main_cm = all_plus // green_len  # 평균 높이 최종
    count = 0  # 총 옮긴 횟수
    for q in range(x, x_end + 1):  # 평탄화 공간 도는 반복문
        for w in range(y, y_end + 1):
            if arr[q][w] < main_cm:  # 만약 기준보다 낮을시
                count += main_cm - arr[q][w]  # 카운트에 기준 높이를 만들기 위한횟수를 카운트
                arr[q][w] += main_cm - arr[q][w]
            elif arr[q][w] > main_cm:  # 만약 기준보다 높을시
                count += arr[q][w] - main_cm  # 카운트에 기준까지 낮추기 위해 일하는 횟수를 카운
                arr[q][w] = main_cm
    print(f'#{tc} {count}') # 결과값
