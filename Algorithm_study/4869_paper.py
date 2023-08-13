# # Sw Expert
# # 4869 종이붙이기

# T = int(input())  # 테스트 케이스

# for tc in range(1,T+1):
#     N = int(input())
N = int(input())
dp = [0] * (N + 1)

dp[0] = 1

for i in range(1, N + 1):
    if i >= 10:
        dp[i] += dp[i - 10]
    if i >= 20:
        dp[i] += dp[i - 20]

result = dp[N]
print(result)
