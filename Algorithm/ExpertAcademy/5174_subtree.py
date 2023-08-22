# SW Expert
# 5174_subtree

# 서브 트리에 속한 노드의 개수를 알아내는 프로그램

def count(n):  # 밑에 몇개가 있는지 알기위해 함수를 돌때마다 카운트를 +1
  global result  # 결과값에 참조하기위해
  result += 1
  for q in range(V+1):  # 해당하는 노드에 이어진 길이 있는지 확인후 있다면 그 번호로 함수를 돌림
    if data[n][q] == 1:
      count(q)

T = int(input())  # 테케

for tc in range(1, T+1):
  E, N = map(int, input().split())  # 간선의 갯수, 기준노드

  V = E + 1  # 노드의 갯수

  data = [[0] * (V+1) for _ in range(V+1)]  # 몇번노드가 몇번

  edge = list(map(int, input().split()))  # 노드가 이어진 경로
  for i in range(0, len(edge), 2):  # 데이터에 어느 노드가 어디로 이어져있나 기록
    data[edge[i]][edge[i+1]] = 1

  result = 0  # 결과를 기록할 공간
  count(N)  # 함수 호출

  print(f'#{tc} {result}')



