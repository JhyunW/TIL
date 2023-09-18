# 백준
# 11052_카드 구매하기


# 카드는 총 8가지
# 카드는 팩으로만 살수 있고 1~N개까지 포함된 카드까지 N가지가 존재
# 가격이 비싼카드팩만 사서 N개를 구매하려함

want = int(input())  # 살려고 하는 카드 갯수

arr = []
for i in range(1, want+1):
  a = int(input())
  b = round(a / i, 4)  # 소수점 4자리까지
  arr.append([i, a, b])  # 갯수, 가격, 가성비

arr.sort(key = lambda x : x[2], reverse = True)

now = 0
while now == want:
  