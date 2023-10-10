def move(now, money):
    visited[now] = 1
    for q in range(N):
        if visited[i] == 0 and arr[now][q] != 0:
            move(q, money + arr[now][q])


N = int(input())  # 도시의 수
arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 arr
visited = [0] * N  # 방문 기록
move(0, 0)
short = 99999999

for i in range(N):
    move(i, 0)