# baekjoon
# 2579_계단 오르기

N = int(input())  # 계단의 총 갯수
arr = [int(input()) for _ in range(N)]  # N 개의 계단 각 점수 입력
dp = [0] * N  # N 개의 0으로 채워진 dp 리스트
result = 0

if N <= 2:
    print(sum(arr))  # 계단이 2칸까지일때는 다 더하는게 최대값
else:
    dp[0] = arr[0]  # 첫계단의 경우
    dp[1] = arr[0] + arr[1]  # 첫계단과 두번째 계단을 간 경우
    for i in range(2, N):  # dp 리스트가 맨 뒤가 0으로 시작하기때문에 밑에 받아올때 0부터
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
    print(dp[-1])