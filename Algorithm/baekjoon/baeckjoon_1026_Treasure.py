# 길이가 N인 정수 배열 A와 B가 있을 때
# 다음과 같이 함수S를 정의
# S = A[0] x B[0] + ... + A[N-1] x B[N-1]

# 문제점..? : B를 입력받은걸 재배열 하면 안된다가 문제 조건인데 이게 B안에서 재정렬을 하지 말라는건지
# 아예 B를 건들이지 말고 하라는 건지 이해가 안된다.. 일단 B에 넣은 값을 다른 리스트에 새롭게 저장을 하는
# 방법을 사용하여 입력받은 B 함수 자체는 변하지 않았는데 맞는지 모르겠다...

N = int(input()) # 인덱스 갯수

num_A = [] # A를 저장할 공간
num_B = [] # B를 저장할 공간
B_rank = [] # B를 가장 큰 수부터 저장

num_A = sorted(list(map(int, input().split()))) # A를 입력받고 작은수부터 정렬
num_B = list(map(int, input().split())) # B를 입력받음

list_B = []
for case in range(N):
    list_B.append(num_B[case])
    count = case
    while count > 0 : # 카운트가 0보다 큰 동안 반복
        if list_B[count-1] < list_B[count]: # 지금 넣은 숫자와 바fh 직전 숫자와 비교후
            list_B[count - 1], list_B[count] = list_B[count], list_B[count - 1] # 자리바꿈
        count -= 1 # 그 다음판 비교를 위한 카운트 -1

result = 0
for index in range(N):
    result += num_A[index] * list_B[index]

print(result)






# 밑에는 sorted 없이 시도해 봤던 코드 .. 이지만 런타임 에러로 인해 아웃.. 나중에 고쳐보기 위해 저장

# N = int(input()) # 인덱스 갯수
#
# num_A = [] # A를 저장할 공간
# num_B = [] # B를 저장할 공간
# B_rank = [] # B를 가장 큰 수부터 저장
#
# num_A = list(map(int, input().split()))
# num_B = list(map(int, input().split()))
#
# for z in range(N): # B_rank에 num_B의 값들을 크기 순으로 정렬
#     count = z # for문에서 z값을 넘지 않게끔 하기위한 카운트
#     B_rank.append(num_B[z])
#     while count > 0 : # 카운트가 0보다 큰 동안 반복
#         if B_rank[count-1] < B_rank[count]: # 지금 넣은 숫자와 바러 직전 숫자와 비교후
#             B_rank[count - 1], B_rank[count] = B_rank[count], B_rank[count - 1] # 자리바꿈
#         count -= 1 # 그 다음판 비교를 위한 카운트 -1
#
# B_r_index = [] # 벨류가 큰 인덱스 번호를 순서대로 저장할 위치
# for x in B_rank:
#     B_in = [i for i, value in enumerate(num_B) if value == x]
#     if B_in not in B_r_index:
#         B_r_index.extend(B_in)
#
# for c in range(N): # num_A 크기 작은순으로 정렬
#     count = z
#     while count > 0:
#         if num_A[count - 1] > num_A[count]:
#             num_A[count - 1], num_A[count] = num_A[count], num_A[count - 1]
#         count -= 1
#
# result = 0 # 키와 벨류 따로 뽑아서 각 각 대입
# for A_index, B_index in enumerate(B_r_index):
#     result += num_A[A_index] * num_B[B_index]
#
# print(result)


