tc = int(input())  # 테스트 케이스

for test in range(tc):
    N, M = map(int, input().split())  # N개의 정수, M개의 구간
    a = list(map(int, input().split()))  # 숫자 입력
    range_standard = M // 2  # 범위 기준
    big_num = 0  # 가장 큰 수 저장
    small_num = 0  # 가장 작은 수 저장

    if M % 2 == 0:
        plus = 0
        for z in range(0, len(a) - M + 1):
            for x in range(M):
                plus += a[z + x]

            if big_num < plus:  # 만약 while문을 돌고 나온 합이 지금의 최고 숫자보다 높으면 대입
                big_num = plus

            if small_num > plus or small_num == 0:  # 만약 0 이거나 지금의 스몰넘버보다 더 작은 합이 나오면 대입
                small_num = plus

            plus = 0


    else:
        for i in range(range_standard, len(a) - range_standard):
            plus = 0  # while 문에에서 더한 총 합을 저장한 공강
            re_i = i - range_standard  # a의 0 번째 인덱스
            while re_i != i + range_standard + 1:  # 인덱스 넘버가 i + range_standard + 1 과 같아질때까지 반복
                plus += a[re_i]  # a의 0번째부터 i + range_standard 인덱스 까지
                re_i = re_i + 1  # 인덱스 번호를 1 카운트

            if big_num < plus:  # 만약 while문을 돌고 나온 합이 지금의 최고 숫자보다 높으면 대입
                big_num = plus

            if small_num > plus or small_num == 0:  # 만약 0 이거나 지금의 스몰넘버보다 더 작은 합이 나오면 대입
                small_num = plus

    result = big_num - small_num  # 계산식

    print(f'#{test + 1} {result}')
