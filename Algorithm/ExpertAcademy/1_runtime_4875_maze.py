# SW Expert
# 4875_maze

# 0 = 통로 / 1 = 벽 / 2 = 시작 / 3 = 도착
# SW Expert
# 4875_maze
move_x = [-1, 0, 1, 0]  # 위 왼 아 오
move_y = [0, -1, 0, 1]

T = int(input())  # 테케 입력

for tc in range(1, T+1):
    N = int(input())  # 미로 크기 입력
    arr = [[] for _ in range(N)]  # N줄의 리스트 생성
    start = []  # 시작 좌표
    check = 0  # 도착 지점에 갈시에 1로 바뀌게 할 공간
    visited = []  # 방문기록 저장
    for i in range(N):  # 미로 길 입력
        arr[i] = list(map(int, input()))
        visited.append([0]*N)  # 0으로 방문기록을 적을 데이터 생성
    for q in range(N):  # 시작 좌표 찾기
        for q1 in range(N):
            if arr[q][q1] == 2:
                start = [q, q1]  # 스타트 지점
                print(start, '찾은 시작 좌표')
                break
    stack = [start]  # 길을 되돌아오기 위해 필요한 스택공간
    print(stack, '시작하는 첫 조사대상')
    def find():
        while stack:  # 스택이 있는동안 반복
            x, y = stack.pop(0)  # 스택의 마지막 지점부터 시작
            for w in range(4):  # 위 왼 아 오 순서대로 반복
                nx, ny = x + move_x[w], y + move_y[w]
                # 리스트 범위를 벗어나지 않으며, 방문기록이 없을 시
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    if arr[nx][ny] == 0:
                        stack.append([nx, ny])  # 되돌아가는 길 저장
                        visited[nx][ny] = 1  # 방문기록 저장
                    elif arr[nx][ny] == 3:  # 만약 3 , 도착지점에 도달하면
                        return 1
        return 0
    print(f'#{tc} {find()}')






# =======오답케이스 이유 찾아보기 =======================
# move_x = [-1, 0, 1, 0]  # 위 왼 아 오
# move_y = [0, -1, 0, 1]
#
# T = int(input())  # 테케 입력
#
# for tc in range(1, T+1):
#     N = int(input())  # 미로 크기 입력
#     arr = [[] for _ in range(N)]  # N줄의 리스트 생성
#     start = []  # 시작 좌표
#     check = 0  # 도착 지점에 갈시에 1로 바뀌게 할 공간
#     visited = []  # 방문기록 저장
#     for i in range(N):  # 미로 길 입력
#         arr[i] = list(map(int, input()))
#         visited.append([0]*N)  # 0으로 방문기록을 적을 데이터 생성
#     for q in range(N):  # 시작 좌표 찾기
#         for q1 in range(N):
#             if arr[q][q1] == 2:
#                 start = [q, q1]  # 스타트 지점
#                 break
#
#     stack = [[start]]  # 길을 되돌아오기 위해 필요한 스택공간
#
#     while stack:  # 스택이 있는동안 반복
#         if check == 1:  # 체크지점에 도달했으면 와일문 탈출
#             break
#         x, y = stack.pop(0)  # 스택의 마지막 지점부터 시작
#         for w in range(4):  # 위 왼 아 오 순서대로 반복
#             nx, ny = x + move_x[w], y + move_y[w]
#             # 리스트 범위를 벗어나지 않으며, 방문기록이 없을 시
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
#                 if arr[nx][ny] == 0:
#                     stack.append([nx, ny])  # 되돌아가는 길 저장
#                     visited[nx][ny] = 1  # 방문기록 저장
#                 elif arr[nx][ny] == 3:  # 만약 3 , 도착지점에 도달하면
#                     check = 1  # 체크 카운트 증가
#                     break  # for문 탈출
#     print(f'#{tc} {check}')
