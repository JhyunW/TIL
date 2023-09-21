# SW Expert
# 5250_최소 비용
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    Q = deque()
    # x, y 삽입 : 시작 좌표는 항상  0, 0
    Q.append((0,0))
    visited[0][0] = 0

    while Q:
        x, y = Q.popleft()
        # 4방향 조사
        for k in range(4):
            # 다음 좌표
            nx = x + dx[k]
            ny = y + dy[k]
            # 다음 좌표가 범위 내에 있고, 목적지 좌표의 방문 표시값보다 작거나 같은 경우
            # 분기 : 현재 위치가 다음 위치보다 낮거나 높은것
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] <= visited[N-1][N-1]:
                if arr[x][y] >= arr[nx][ny]:
                    # 기본 비용만 소몬
                    # 다음 칸의 방문 표시값을 현재 표시값과 비교
                    if visited[nx][ny] > visited[x][y] + 1:
                else:
                    # 높이 차에 대한 비용도 함께 소모
                    if visited[nx][ny] > visited[x][y] + 1 + (arr[nx][ny] + 1):
                        visited[nx][ny] = visited[x][y] + 1 + (arr[nx][ny] + 1)
                        Q.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    

    # 비교대상
    max_val = sum(sum(arr, [])) + N**2
    # 이전에 방문한 적이 있다면, 가중치를 visited에 기록
    # 최초 방문시에도, 비교 할 수 있는 값이어야한다. -> 최소 비용을 찾고 있으므로
    visited = [[max_val] * N for _ in range(N)]
    print(visited)