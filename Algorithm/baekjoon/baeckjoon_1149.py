# 백준
# 1149_RGB거리

# 빨초파 순으로 칠함. 1번집은2번집과 같으면안됨
# N번집의 색은 N-1번집과 같으면 안됨
# i-1번과 i+1 즉 양 옆의 집과 색이 같으면 안됨.

N = int(input())  # 집의 수
arr =[list(map(int, input().split())) for _ in range (N)]

for i in range(1, N):  # 위에서부터 시작해서 바로 아래칸의 겹치지 않는 숫자 두개중 더 작은수를 더함
  arr[i][0] += min(arr[i-1][1], arr[i-1][2])  # i줄의 0번 칸에는 i-1줄의 1,2번 칸중 가장 작은수
  arr[i][1] += min(arr[i-1][0], arr[i-1][2])  # 위와 마찬가지로
  arr[i][2] += min(arr[i-1][0], arr[i-1][1])  


print(min(arr[-1]))  # 가장 마지막 줄이 최종수이므로 그중 가장 작은 수