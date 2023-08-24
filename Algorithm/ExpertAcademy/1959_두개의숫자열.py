# SW Expert
# 1959_두개의숫자열

T = int(input())  # 테케

for tc in range(1, T+1):
    N, M = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    best = 0
    if N <= M:
        for i in range(M):
            if i + N - 1 < M:
                plus = 0
                for q in range(N):
                    plus += a[q] * b[i+q]
                if best < plus:
                    best = plus

    elif N > M:
        for i in range(N):
            if i + M - 1 < N:
                plus = 0
                for q in range(M):
                    plus += b[q] * a[i+q]
                if best < plus:
                    best = plus


    print(f'#{tc} {best}')