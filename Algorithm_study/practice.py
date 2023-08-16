# SW Expert
# 4881_배열 최소 합

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 배열 크기

    arr = [[] for _ in range(N)]

    for q in range(N):
        arr[q] = list(map(int, input().split()))

    for w in range(N):
        for w1 in range(N):
            main = arr[w][w1]

            for e in range(N):
                for e1 in range(N):
                    if e != w and e1 != w1: