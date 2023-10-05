# 백준
# 1965_상자넣기

N = int(input())  # 상자의 갯수
arr = list(map(int, input().split()))  # arr 입력
dp = [1] * N  # [1, 1, 1, 1]

for i in range(N):  # 상자 갯수만큼 반복
  for j in range(i):  # 현재 상자의 번호까지만 반복
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)  # 바로 직전까지 비교한 수와 지금의 비교수 중 최적의 경우

print(max(dp))  # 가장 높은 수
