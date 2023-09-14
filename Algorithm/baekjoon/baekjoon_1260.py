# baekjoon_1260
# DFS와 BFS

def DFS(num):  # 깊이 우선 탐색
    print(num, end=' ')  # 탐색하는 넘버 출력
    visited_D[num] = 1  # 현재 탐색하는 위치 방문기록 표시
    for find in range(1, N+1):  # 1~N+1 까지 탐색
        if data[num][find] == 1 and not visited_D[find]:  # 경로가 있고 방문기록 x
            DFS(find)

def BFS(num):  # 넓이 우선 탐색
    arr = [num]  # arr리스트 생성
    while arr:  # arr리스트가 있는동안 계속 반복
        now = arr.pop(0)
        visited_B[now] = 1  # 리스트의 맨 처음 숫자 방문기록
        print(now, end=' ')  # 탐색순서 출력
        for find in range(1, N+1):  # 1 ~ N+1 까지 탐색
            if data[now][find] == 1 and not visited_B[find]:  # 길이 이어져 있고, 방문 기록이 없을시
                arr.append(find)  # arr에 해당 번호 추가
                visited_B[find] = 1

N, M, V = map(int, input().split())  # 정점의 갯수, 간선 갯수, 시작 간선

visited_D = [0] * (N+1)  # 방문 기록 표시
visited_B = [0] * (N+1)  # 방문 기록 표시

data = [[0]*(N+1) for _ in range(N+1)]  # 몇번이 몇번으로 이어져 있는지 확인

for i in range(M):
    a, b = map(int, input().split())
    data[a][b] = 1  # 몇번 노드가 몇번 이어짐 표시
    data[b][a] = 1

DFS(V)
print()
BFS(V)