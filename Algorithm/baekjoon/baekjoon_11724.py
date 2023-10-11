# 백준 11724_연결요소의 개수
# 연결요소 즉 몇개의 그룹이 있는지 구하는 문제
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline
def graph(num):
  visited[num] = 1  # 방문기록 찍기
  for w in range(1, N+1):
    if visited[w] == 0 and arr[num][w] == 1:  # 방문 기록이 없고 길이 있으면
      graph(w)

N, M = map(int, input().split())  # 정점의 개수, 간선의 개수
arr = [[0] * (N+1) for _ in range(N+1)]  # 리스트 생성
for i in range(M):  # 이어진 통로 1로 찍어주기
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1

visited = [0] * (N+1)  # 방문 기록
count = 0  # 그룹의 갯수
for q in range(1, N+1):
  if visited[q] == 0:
    count += 1
    graph(q)

print(count)


# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline
# # 백준 11724_연결요소의 개수
# # 연결요소 즉 몇개의 그룹이 있는지 구하는 문제

# def graph(num):
#   visited[num] = 1  # 방문기록 찍기
#   for w in arr[num]:
#     if visited[w] == 0:  # 방문 기록이 없고 길이 있으면
#       graph(w)

# N, M = map(int, input().split())  # 정점의 개수, 간선의 개수
# arr = [[] * (N+1) for _ in range(N+1)]  # 리스트 생성
# for i in range(M):  # 이어진 통로 1로 찍어주기
#   a, b = map(int, input().split())
#   arr[a].append(b)
#   arr[b].append(a)

# visited = [0] * (N+1)  # 방문 기록
# count = 0  # 그룹의 갯수
# for q in range(1, N+1):
#   if visited[q] == 0:
#     count += 1
#     graph(q)

# print(count)
