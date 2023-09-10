# 2606_바이러스

# 한 컴퓨터가 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는
# 모든 컴퓨터는 웜 바이러스에 걸린다
# 1번 컴퓨터가 바이러스에 걸렸을 때 바이러스에 걸리게 되는 컴퓨터의 수를 구하는
# 프로그램을 작성



def bfs(n):
  marking[n] = 1  # 지나는 데이터 체크
  for i in data[n]:
    # n번째의 컴퓨터가 i번째와 연결되어 있고, 지나온 길에 기록이 없다면
    if not marking[i]:
      bfs(i)


com = int(input())  # 컴퓨터의 수

connect = int(input())  # 연결된 다리 수

arr = []  # 컴퓨터 연결정보를 쓸 곳

data = [[]for _ in range(com+1)]  # 연결 정보를 쓸 곳
marking = [0] * (com+1)  # 지나온곳을 표시할 변수
for _ in range(connect):
  arr.append(list(map(int, input().split())))  # 연결되어진 번호

for check in arr:
  data[check[0]] += [check[1]] 
  data[check[0]] += [check[1]]

bfs(1)
result = -1
for plus in range(1, com+1):
  result += marking[plus]

print(result)
