# SW Expert
# 중위순회
def inorder(p, N):  # N은 완전 이진트리의 마지막 정점
  if p <= N:
    inorder(p*2, N)    # 왼쪽 자식으로 이동
    print(tree[p], end = ' ')
    inorder(p * 2 + 1, N)    # 오른쪽으로 이동


T = 10
for tc in range(1, T+1):
  N = int(input())  # 정점의 총 수
  tree = [0] * (N+1)  # N번 까지 노드가 있는 완전이진트리
  for _ in range(N):
    arr = list(input().split())  # 띄어서 리스트로 들어옴
    tree[int(arr[0])] = arr[1]
  # 중위순회
  print(f'#{tc} ', end = ' ')
  inorder(1, N)