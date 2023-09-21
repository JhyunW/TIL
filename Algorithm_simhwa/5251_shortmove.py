import sys
sys.stdin = open('input.txt')

def dijkstra():
    # 비교 대상이 될 가중치 정보
    dist = [E * 100] * (V + 1)
    visited = [0] * (V+1)
    # 시작지점이 항상 0(해당 문제)
    dist[0] = 0
    
    for _ in range(V):
        next = 0
        min_val = E * 100

        # 최솟값 찾기
        for i in range(V + 1):
            if not visited[i] and min_val > dist[i]:
                next = i
                min_val = dist[i]
        visited[next] = 1

        # 모든 노드에 대해서 도착할 수 있는 최소 가중치 갱신
        for j in range(V + 1):
            if not visited[i] and dist[j] > dist[next] + arr[next][i]:
                dist[j] = dist[next] + arr[next][j]
        print(dist)





T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    
    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S][E] = W  # 일방통행
    dijkstra()