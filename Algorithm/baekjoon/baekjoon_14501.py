# 백준
# 14501_퇴사

def how(day, money):  
    global result  # 최대값을 설정하기위한 글로벌 선언
    for i in range(day, N):  # 입력 날짜부터 퇴사 전날까지
        if i + arr[i][0] <= N:  # 상담 소요가 N보다 작거나 같으면
            how(i+arr[i][0], money + arr[i][1])  # 그 경우의 수 함수 호출
    
    if money > result:  # 모든 일수를 탐색후 결과값이 최대값보다 큰 경우 대입
            result = money
            return  


N = int(input())  # 남은 일 수
arr = [list(map(int, input().split())) for _ in range(N)]  # [[기간, 돈]] 식으로 정리
result = 0  # 최대값을 저장한 공간

how(0,0)  # 함수를 불러오기

print(result)  # 결과값 출력