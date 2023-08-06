# SW Expert
# 4831_전기버스

# 전기버스는 한번 충전으로 이동가능한 거리가 제한
# 충전기가 있는 정류장 있음
# 버스는 0번부터 N번 정류장까지 이동
# 한번 충전으로 최대 K만큼 이동
# 충전기가 설치된 M개의 정류장
# 최소 몇번의 충전을 해야 종점에 도착하는가?
# 만약 충전기 설치가 잘못되어 있다면 0 출력

T = int(input())  # 테스트케이스

for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # 한번 충전으로 이동 거리, 종점번호, 충전기 수
    arr = [0] * (N+1)  # N번까지 있는 정류장 리스트
    charge_num = list(map(int, input().split()))  # 충전기를 설치할 노선 번호

    for i in charge_num:
        arr[i] = 1  # 충전기가 있는 정류장 표시

    now = 0  # 현재 좌표
    count = 0  # 자동차 충전 횟수

    while now < N:
        if now + K >= N:
            now = N
            break
        charge_point = 0
        for i in range(K):
            if now + 1 < N:
                now += 1
                if arr[now] == 1:
                    charge_point = now
            elif now + 1 == N:
                break

        if charge_point == 0:
            count = 0
            break
        else:
            now = charge_point
            count += 1

    print(f'#{tc} {count}')

    # -------------------------------런타임 에러------------------------------
    # while N >= now:
    #     charge_point = 0
    #     for z in range(1, K+1):
    #         if now+z <= N:
    #             if arr[now+z] == 1:
    #                 charge_point = now+z

    #     if charge_point == 0 and now + K < N:
    #         count = 0
    #         break

    #     elif now + K >= N:
    #         break

    #     elif now < N:
    #         now = charge_point
    #         count += 1

    # print(f'#{tc} {count}')
