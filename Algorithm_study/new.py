# # 10개의 원소중 3개를 고르는 조합  N - 3까지

# def nCr(n,r,s):  # n 개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             nCr(n, r-1, i+1)

# A = [1, 2, 3, 4, 5]
# N = len(A)
# R = 3
# comb = [0] * R
# nCr(N, R, 0)

arr = [list(map(str, input().split()))]
number = []
for i in arr[0][0]:  # 리스트에 숫자를 하나씩 대입
    number.append(int(i))
data = [0] * len(arr[0][0])
for q in range(len(number)-1, -1, -1):
    print(number[q])