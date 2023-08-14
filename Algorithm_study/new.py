
def road(start):
    visited[start] = 1  # 시작점은 방문을 한 것이므로 1 입력넣기
    if start == G:  # 스타트 지점이랑 골 지점이 같으면 값을 찾은것이므로 리턴해주고 끝내기
        return
    for next in range(1, V+1):  # 노드의 번호순회
        if data[start][next] and not visited[next]:  # 데이터의 몇번째에 길이 있는지랑, 동시에 다음 길에 방문 기록이 없는지
            road(next)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())  # 노드번호와 간선 갯수

    data = [[0] * (V+1) for _ in range(V+1)]  # 이어진 노드

    visited = [0] * (V+1)  # 방문 기록

    for i in range(0, E*2, 2):
        x, y = map(int, input().split())
        data[x][y] = 1

    S, G = map(int, input().split())
    road(S)
    print(f'{tc} {visited[G]}')