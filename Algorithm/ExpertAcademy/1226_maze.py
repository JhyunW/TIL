# SW Expert
# 1226_Maze
move_x = [-1, 0, 1, 0]  # 위 왼 아 오
move_y = [0, -1, 0, 1]

def check(now):
    while now:
        a = now.pop(0)  # 지금의 x좌표 가져오는것과 동시에 now에서 제거
        b = now.pop(0)  # 지금의 y좌표
        
        visited[a][b] = 1  # 방문 기록에 현재 위치 표시
        
        for move in range(4):
            ax, by = a + move_x[move], b + move_y[move]
            if 0 <= ax < 16 and 0 <= by < 16:  # 리스트를 벗어나지 않는지 확인
                if arr[ax][by] == 3:
                    return 1
                elif not arr[ax][by] and not visited[ax][by]:  # 이동할곳이 0 이며, 방문을 아직 안했경우
                    visited[ax][by] = 1  # 방문기록 체크
                    now.append(ax)  # now 리스트에 좌표 추가
                    now.append(by)
    
    return 0
                

for t in range(1, 11):
    tc = int(input())  # 테스트 케이스 입력
    
    arr = [[]* 16 for _ in range(16)]
    
    for i in range(16):  # 맵을 만드는 반복문
        arr[i].extend(list(map(int, input())))
        
    visited = [[0]*16 for _ in range(16)]  # 방문 기록
    
    start = []  # 시작점을 찍을 곳
    for q in range(16):  # 시작점을 찾는 반복문
        for q1 in range(16):
            if arr[q][q1] == 2:
                start = [q, q1]
                break
    
    print(f'#{tc} {check(start)}')
    