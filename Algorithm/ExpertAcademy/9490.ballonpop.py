# SW Expert 9490 풍선팡

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for y in range(N):
        for x in range(M):
            count = arr[y][x]

            for long in range(1, arr[y][x]+1):
                for move in range(4):
                    pop_y, pop_x = y+(di[move]*long), x+(dj[move]*long)
                    if 0 <= pop_y < N and 0 <= pop_x < M:
                        count += arr[pop_y][pop_x]

            if max_v < count:
                max_v = count

    print(f'#{tc} {max_v}')