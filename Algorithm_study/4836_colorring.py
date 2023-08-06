# SW Expert


T = int(input())  # 테스트 케이스
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]  # 10 * 10 배열 생성

    N = int(input())  # 칠할 횟수
    for i in range(N):
        x, y, x_1, y_1, color = map(int, input().split())
        for q in range(x, x_1+1):
            for w in range(y, y_1+1):
                arr[q][w] += color
    count = 0
    for e in range(10):
        for w in range(10):
            if arr[e][w] == 3:
                count += 1
    print(f'#{tc} {count}')
