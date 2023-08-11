# SW Expert
# 길찾기
# A지점에서 B도시로 가는 길이 존재하는지 조사하려고 한다.
# 길 중간중간 최대 2개의 갈림길이 존재하며, 모든길은 일방통행으로 돌아오기가 불가능
# A 에서 B로 가는 길이 존재하는지 알아내는 프로그램을 작성하라
# A와 B는 숫자0가 99로 고정


def DFS(start):
    # 처음 시작하는점은 방문을 한 것이므로 1을 표시
    visited[start] = 1
    # 현재 조사 지점이 도착지점인 G라면 바로 조사 종료
    if start == G:
        return

    for next in range(100):
        #  스타트 지점에서 next지점에 갈 수 있고, next 지점을 방문한적 없다면
        if data[start][next] and not visited[next]:  # 만약 data의stat즉 지금위치에서 next 번호로 가는 길이 있고, 방문 기록이 없다면 이동
            DFS(next)


for t in range(1, 11):
    tc, E = map(int, input().split())  # 테스트 넘버와 이동 경로의 개수
    x_y = list(map(int, input().split()))  # 몇번 노드가 몇번으로 이어져 있는지 입력
    data = [[0] * 100 for _ in range(100)]  # 몇번째(리스트)가 몇번째 (인덱스)로 이어지는가
    visited = [0] * 100  # 방문기록
    for i in range(0, E*2, 2):
        data[x_y[i]][x_y[i+1]] = 1  # 몇번노드가 몇번으로 표시할 반복문

    # 시작점과 도착점
    S = 0
    G = 99

    DFS(0)
    print(f'#{tc} {visited[G]}')