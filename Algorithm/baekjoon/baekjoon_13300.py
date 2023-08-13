# 초등학교에서 단체로 2박3일 수학 여행을 가기로 함
# 1~6학년까지 학새을이 묵을 방을 배정해야함
# 남은 남끼리 여는 여끼리 배정
# 한방에 같은 학년들 배정 한명도 가능
# 한방 최대 배정 인원 K
# 조건에 맞게 배정하기 위한 최소방의 갯수를 구하시오
# 0 여자 1 남자

student, K = map(int,input().split())  # 참가 학생 수

arr = [[] for _ in range(student)]
man_set = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}  # 1 남자학년별
girl_set = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}  # 0 여자 학년별
for i in range(student):
    arr[i] = list(map(int, input().split()))
  
print(arr)

for q in arr:
    if q[0] == 0:
        girl_set[q[1]] += 1
    else:
        man_set[q[1]] += 1

print(man_set)
print(girl_set)