# 백준 116600
# 구간 합 구하기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[0] * (N + 1)]  # A배열
D = [[0] * (N + 1) for _ in range(N + 1)]  # D 이중배열 N+1 * N+1

for i in range(N):
  row_A = [0] + [int(x) for x in input().split()]
  A.append(row_A)

for i in range(1, N+1):
  for j in range(1, N+1):
    D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]  # 이거는 공식임.. 외우거나 이해해야할듯

for tc in range(M):
  x1, y1, x2, y2 = map(int, input().split())  # 배열
  result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
  print(result)