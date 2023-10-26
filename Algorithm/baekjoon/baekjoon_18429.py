# 백준_18429
# 근손실

# 3대500에서 하루마다 중량이 K만큼 감소
# 운동키트 N일동안 한번씩만 사용가능
from itertools import permutations  # 순열 함수

N, K = map(int, input().split())  # N일간 매일 K만큼 빠짐

arr = list(map(int, input().split()))  # 운동 키트 중량 증가량

count = 0  # 경우의 수 카운팅

for i in permutations(arr, N):  # 순서가 다른경우도 포함이므로 permutaions
  now = 0  # 중량 기준
  for j in range(N):
    now += i[j] - K
    if now < 0 :
      break
    if j == N-1:
      count += 1

print(count)

