# SW Expert
# 5176_이진탐색

T= int(input())  # 테케
for tc in range(1, T+1):
  N = int(input())  # 자연수

  edge = []
  left = [0] * (N + 1)
  right = [0] * (N + 1)
  parent = [0] * (N + 1)

  