# SW Expert
# 5105_노드의 거리

# N * N 크기의 미로에서 출발지 목적지가 주어진다
# 이때 최소 몇개의 칸을 지나면 도착지에 다다를 수 있는지 알아내는 프로그램을 작성
# 거리 사이에 있는 0의 갯수
def goal(now):
    count = 0  # 이동 거리
    queue = []  # 현재 노드에서 이어져 있는 길들을 중간저장할 공간
    while arr[now[0]][now[1]] != 3:  # 리스트가 3을 만나면 종료되게끔 함
        visited[now[0]][now[1]] = 1  # 방문기록 찍기
        for move in range(4):  # 리스트 범위를 벗어나는지 확인.
            mx, my = now[0] + move_x[move], now[1] + move_y[move]
            if 0 <= mx < N and 0 <= my < N:
                if arr[mx][my] == 0 and not visited[mx][my]:  # 다음 길이 0이고 방문 기록 없을시
                    queue.append(mx)  # 나온 숫자 넣어주기
                    queue.append(my)
                elif arr[mx][my] == 3:  # 3을 만날경우
                    return count  # 거리 반환
        now.pop(0)  # 사용한 x좌표와 t좌표 지우기
        now.pop(0)
        if now == [] and queue == []:
            return 0
        elif now == []:
            now.extend(queue)
            queue = []
            count = count + 1
        
                
    
    

move_x = [-1, 0, 1, 0]  # 위 왼 아 오
move_y = [0, -1, 0, 1]
T = int(input())  # 테케

for tc in range(1, T+1):
    N = int(input())  # 배열의 크기
    arr = [[]for _ in range(N)]
    visited = [[0]*N for _ in range(N)]  # 방문 기록을 할 공간
    start = []  # 시작점을 넣을 공간
    for q in range(N):  # N개의 출에 길 입력
        arr[q].extend(list(map(int, input())))
    
    for w in range(N):  # 시작 지점 찾기
        for w1 in range(N):
            if arr[w][w1] == 2:
                start = [w, w1]
    print(f'#{tc} {goal(start)}')