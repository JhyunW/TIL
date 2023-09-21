'''
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


# MST
def prim(start):
    # 방문 정보
    visited = [0] * (V+1)
    visited[start] = 1
    # 가중치 누적값
    result = 0
    # heap 자료 구조를 안쓴다 -> 모든 정점 조사
    for _ in range(1, V):
        # 다음 조사 대상
        next = 0
        # 가중치 비교 대상
        min_val = 10000000000
        for i in range(V+1):  # 실제 조사할 노드 번호
            if visited[i] == 1:
                for j in range(V+1):
                    # 한번 방문한적 있었던 i의 인접노드 j
                    # 인접행렬을 진출 가능한 노드에 대해서만 가중치를 기록
                    if arr[i][j] > 0 and visited[j] and min_val > arr[i][j]:
                        next = j
                        min_val = arr[i][j]
        result += min_val
        visited[next] = 1
    return result



# 노드, 간선
V, E = map(int, input().split())
# 간선 정보 -> 인접 행렬
arr = [[0] * (V+1) for _ in range(V + 1)]

for _ in range(E):
    # 질추르 진입, 가중치
    S, E, W = map(int, input().split())
    # 무방향 그래프이므로 양쪽 노드 정보입력
    arr[S][E] = W
    arr[E][S] = W
print(arr)
