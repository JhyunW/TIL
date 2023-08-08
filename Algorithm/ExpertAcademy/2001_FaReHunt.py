# SWe Expert

# 2001_파리퇴치

# N * N 배열 안에 파리의 숫자 제시
# M * M 크기의 파리채를 한번 내리쳐 최대한 많은 파리를 잡아야함

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 배열의 범위

    arr = [[0] * N for _ in range(N)]  # 리스트 생성

    best_count = 0

    for arr_num in range(N):  # 각각의 리스트에 숫자 생성
        arr[arr_num] = list(map(int, input().split()))

    for hunt_pointx in range(0, N-M+1):  # 0 ~ N-M번째 범위까지
        for hunt_pointy in range(0, N-M+1):
            count = 0
            for hunt_x in range(M):
                for hunt_y in range(M):
                    count += arr[hunt_pointx + hunt_x][hunt_pointy + hunt_y]

            if best_count < count:
                best_count = count

    print(f'#{tc} {best_count}')