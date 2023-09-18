# 백준
# 20291_파일정리

# 파일을 확장자 별로 정리해서 몇 개씩 있는지 체크
# 확장자들을 사전 순으로 정렬

f_num = int(input())

file = dict()
for _ in range(f_num):
    now = (input().split('.'))[1]  # .을 기준으로 0,1 나눈 후 1번을 넣기
    if not now in file:  # 딕셔너리 안에 없을 시
        file[now] = 1
    else:  # 존재하면 카운트
        file[now] += 1

sort_file = sorted(file.items())  # 키를 사전 순으로 정렬

for key, value in sort_file: # 키랑 벨류 구분
    print(key, value)