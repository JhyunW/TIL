# SW Expert
# 그래프 경로

T = int(input())  # 테스트 횟수
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 노트와 간선의 개수
    move = []
    for i in range(E):
        move += list(map(int, input().split()))  # 노드의 간선 정보 어디서 어디로
    S_G = map(int, input().split())  # 스타트와 골 지점

    # 노드가 V개 이므로 V번 인데스까지 필요함 고로 7+1 개의 값을 가진 리스트
    visited = [False] * (V + 1)  # 방문기록
    # 이동 가능 정보 2차원 리스트
    # 몇번째 노트가 어디어디 연결되어있나 나타내는 리스트
    matrix = [[0] * (V + 1) for _ in range(V + 1)]

    print(visited)
    print('========================')
    print(matrix)
    print('========================')
    print(move)

    for q in range(0, E * 2, 2):  # 0~간선*2 의 갯수 만큼 반복을 도는데
        matrix[move[q]][move[q+1]] = 1  # 2씩 뜀 즉 1 -> 4로 갔고
        # 즉 몇번(노트)리스트의 몇번째 숫자가1인 경우 그 몇번째로 이어진 간선이 있음
        matrix[move[q + 1]][move[q]] = 1

    # 1번 노트가 6번 노트로 가는 길이 있는지 확인해야함.
