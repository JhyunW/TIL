# SW Expert
# 2817_부분 수열의 합

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0   # 합이 k가 되는 경우의 수
    for i in range(1 << N):
        s = 0
        for j in range(N):  # j번 비트
            if i&(1 << j):  # i의 j번 비트검사
                s += arr[j]  # 0이 아니면 j 번 원소가 부분집합에 포함됨

        if s == K:
            cnt += 1

    print(f'#{tc} {cnt}')