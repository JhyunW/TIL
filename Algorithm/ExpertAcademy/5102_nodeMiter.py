# SW Expert
# 5102_노드의 거리

def check(node):
    queue = [node]
    ing_node = []  # 현재 순서에서 갈 수 있는 노드들 나즁에 queue로 옮겨줄거임
    count = 0  # 시작점으로부터 도착 지점까지의 거리
    while queue:
        z = queue.pop(0)  # 확인할 노드의 첫번째 가져오기
        if z == G:
            return count
        visited[z] = 1  # 방문기록 표시
        
        for w in range(1,V+1):
            if data[z][w] and not visited[w]:  # z번 노드가 w로 이어져 있으며, w방문 기록이 없을시
                ing_node.append(w)  # w노드를 리스트에 추가
        
        if not queue and ing_node:  # 현재 돌릴걸 다 돌리고 다음 돌 노드가 남아있을 경우
            queue = ing_node
            ing_node = []  # 노드들을 옮겨준 후 다시 비워줌
            count += 1  # 카운트도 1 올려줌
    
    return 0
                




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 노드개수와 간선 개수
    
    visited = [0] * (V + 1)  # 방문기록
    
    data = [[0] * (V+1) for _ in range(V+1)]  # 몇번노드(리스트) 가 몇번 노드(인덱스)로 이어져 있는지
    
    for q in range(E):
        a, b = map(int, input().split())  # 이어진 길 입력
        data[a][b] = 1  # 몇번 노드가 몇번노드로 이어져있는지 1로 표시
        data[b][a] = 1  # 양방 이동 가능하므로 양쪽 표시
    
    S, G = map(int, input().split())  # 도착과 골 지점 입력
    
    print(f'#{tc} {check(S)}')
    
    