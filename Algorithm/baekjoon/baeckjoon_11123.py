# baekjoon_11123
# 양한마리.. 양 두마리..
dx = [0, 1, 0, -1]  # 오 아 왼 위
dy = [1, 0, -1, 0]

def find(x, y):
  quee = [x, y]
  while quee:
    a = quee.pop(0)
    b = quee.pop(0)
    for i in range(4):
      ma = a + dx[i]
      mb = b + dy[i]
      if 0 <= ma < H and 0 <= mb < W:
        if arr[ma][mb] =='#' and not visited[ma][mb]:
          visited[ma][mb] = 1
          quee.append(ma)
          quee.append(mb)


T = int(input())  # 테케

for tc in range(1, T+1):
  H, W = map(int, input().split())  # 높이, 넓이
  arr = [(input()) for _ in range(H)]
  visited = [[0]*W for _ in range(H)]  # 방문 기록
  count = 0

  for q in range(H):
    for w in range(W):
      if arr[q][w] == '#' and visited[q][w] != 1:
        find(q,w)
        count += 1
  
  print(count)