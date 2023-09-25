# 백준
# 11048_이동하기
m_x = [1, 0, 1]  # 오, 아 , 대아
m_y = [0, 1, 1]


N, M = map(int, input().split())  # N*M 배열 입력
arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 줄만큼 각 숫자 입력
visited = [[0]*M for _ in range(N)]  # 방문기록 생성
visited[0][0] = arr[0][0]  # 기록할 첫번째 같에 숫자 입력받아넣기

for i in range(1, M):  # 첫번째 줄 숫자 넣기
  visited[0][i] = visited[0][i-1] + arr[0][i]  # 그 줄의 최대값을 각 자리에 저장

for j in range(1, N): # 세로열 숫자 넣기
  visited[j][0] = visited[j-1][0] + arr[j][0]

for q in range(1, N):
  for k in range(1, M):
    visited[q][k] = max(visited[q-1][k], visited[q][k-1]) + arr[q][k]  # 위랑 왼쪽중 더 큰수를 비교해서 더해넣기
    
print(visited[N-1][M-1])
