# SW Expert
# 1213_중위순회

T = 10  # 테케 입력

for tc in range(1, T+1):
  N = int(input())  # 노드의 갯수

  arr = [[]for _ in range(N+1)]

  for i in range(1, N+1):
    arr[i] = list(map(str, input().split()))  # 노드번호 문자 왼 오 노드

  edge = []  # 노드의 연결점

  for q in range(1, len(arr)):
    for q1 in range(len(arr[q])):
      if q1 > 1:
        edge.append(int(arr[q][0]))
        edge.append(int(arr[q][q1]))

  left = [0] * (N + 1)
  right = [0] * (N + 1)
  parent = [0] * (N + 1)

  for i in range(N - 1):  # 왼 오 부
    p, c = edge[i * 2], edge[i * 2 + 1]
    if left[p] == 0:  # 아직 왼쪽 자식이 기록되지 않았다면
      left[p] = c  # 몇번 인덱스는 몇번으로 연결
    else:
      right[p] = c  # 몇번 인덱스는 몇번으로 연결
    parent[c] = p  # 몇번인덱스의 부모노드는 몇인지

  def mo(n):
      if left[n] != 0:
        mo(left[n])

      print(arr[n][1], end = '')

      if right[n] != 0:
        mo(right[n])

  print(f'#{tc}', end =' ')
  mo(1)
  print()














# SW Expert
# # 중위순회
# def inorder(p, N):  # N은 완전 이진트리의 마지막 정점
#   if p <= N:
#     inorder(p*2, N)    # 왼쪽 자식으로 이동
#     print(tree[p], end = ' ')
#     inorder(p * 2 + 1, N)    # 오른쪽으로 이동
#
#
# T = 10
# for tc in range(1, T+1):
#   N = int(input())  # 정점의 총 수
#   tree = [0] * (N+1)  # N번 까지 노드가 있는 완전이진트리
#   for _ in range(N):
#     arr = list(input().split())  # 띄어서 리스트로 들어옴
#     tree[int(arr[0])] = arr[1]
#   # 중위순회
#   print(f'#{tc} ', end = ' ')
#   inorder(1, N)