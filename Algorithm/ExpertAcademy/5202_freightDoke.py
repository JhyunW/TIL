# SW Expert
# 5202_화물 도크
def doke():
    count = 0  # 이용 횟수
    finish_time = 0  # 작업 종료 시간
    for application in arr:  # 신청서 탐색
        if finish_time <= application[0]:  # 시작 시간이 마지막 종료 이후일 경우
            count += 1  # 조건 충족시 카운트 더해주기
            finish_time = application[1]  # 신청서의 종료시간을 바꿈

    print(f'#{tc} {count}')


T = int(input())  # 테케

for tc in range(1, T+1):
    N = int(input())  # 신청서 갯수
    # 시작시간, 종료시간
    arr = [list(map(int, input().split()))for _ in range(N)]
    arr.sort(key=lambda x:x[1])  # arr 을 끝나는 시간 순으로 정렬
    doke()