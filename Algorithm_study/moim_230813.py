# 특정 거리의 도시 찾기

# 1~N번 까지의 도시와 M개의 단방향 도로가 존재
# 이때 X도시로부터 출발하여 도달할 수 있는 최단 거리가K인
# 모든 도시의 번호를 출력하는 프로그램을 작성하세요.

def short_move(city):
    visited[city] = 1  # 시작점은 방문을 한 것이므로 방문 하였다는 표시를 찍는다.
    G = [X]  # 4번째 도착이 가능한 도시들을 넣기 위한 리스트
    for move_count in range(K):  # 길을 탐색할 횟수
        next_G = []  # 이번 반복문에서 나오는 이동 가능한 노드들을 저장한 공간
        for center in G:  # G노드들이 어디로 이어져 있는지 찾기위한 반복문
            for w in range(1, N+1):  # 한 리스트에 들어있는 모든 경우의 수 확인
                if data[center][w] and not visited[w]:  # 이번 노드가 W와 이어져 있으며, 방문한 기록이 없을 시
                    next_G.append(w)  # 이동 가능한 노드에 추가
                    visited[w] = 1  # 방문 기록에 해당 노드 번호 저장
        G = next_G  # 방문 가능한 노드들을 다음 확인할 리스트에 저장
    if G == []:  # 만약 최단거리가 K인 도시가 없을 시 -1을 리턴
        G = [-1]
    return G  # 그 외의 경우 G를 리턴 


# N도시의개수, M도로의개수, K최단거리, X출발도시
N, M, K, X = map(int, input().split())

arr = []  # 노드와 노선을 기록할 리스트
for i in range(M):  # 노선의 갯수만큼 출발 노드와 도착 노드 입력 = 경로
    arr += list(map(int, input().split()))

visited = [0] * (N+1)  # 몇번 노드를 방문하였는지 확인하는 리스트

# 몇번노드(리스트)가 몇번 노드(인덱스)로 가는지 기록된 데이터
data = [[0] * (N+1) for _ in range(N + 1)]

for q in range(0, M*2, 2):  # 데이터에 어디서 어디로 이어지는지 기록
    data[arr[q]][arr[q+1]] = 1  # 
count = 0  # 4번째를 찾기위한 카운트
print(*short_move(X))  # 결과 출력