# SW Expert
# 4871_그래프 경로
# 첫 줄에 노드 갯수 V와 간선의 갯수 E가 주어진다
# E개의 줄에 걸쳐 착 노드로 간선 정보가 주어짐
# 그후 출발S와 도착노드 G가 주어진다

def graph(start):
    # 조사 지점 방무 표시
    visited[start] = 1
    if start == G:  # 끝점에 도달하면 조사 종료
        return  # 현재 조사 지점을 방문 표시하였으므로 반환값 없이 종하여도 가능

    for next in range(1, V+1):  # 1부터 노드의 종류즉 갯수만큼 반복
        # start 지점에서 nextㅣ점에 갈 수 있고, next 지점을 방문한적 없다면
        # 데이터의 시작번 리스트의 next인덱스에 1이 있으며(즉 몇번쨰로 가는 노선이 있으며),
        # 방문기록에서 방문한 흔적이 없으면.(0은False,1은True이기 때문)
        if data[start][next] and not visited[next]:
            graph(next)  # 함수를 next번 부터 다시 실행행

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())

    data = [[0] * (V+1) for _ in range(V+1)]  # 인접행렬
    # print('인접 행렬', data)

    visited = [0] * (V+1)  # 방문 표시용 리스트
    # print('방문 표시', visited)

    for i in range(E):  # 간성 정보 입력받기
        x, y = map(int, input().split())  # 어디서 어디로 를 입력
        data[x][y] = 1  # 인접 행렬에 표시 ex) 몇번째줄(노드) 는 3번째인덱스(연결점)가 1로 표시

    # print('인전행렬 찍은 후', data)

    S, G = map(int, input().split())  # 시작점과 도착점
    graph(S)  # 함수적기
    print(f'#{tc} {visited[G]}')

