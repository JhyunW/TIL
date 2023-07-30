# 1859

# 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 3. 판매는 얼마든지 할 수 있다.

t = int(input()) # test case

for test_case in range(t): # 테스트 케이스 반복문
    
    day = int(input()) # 몇일을 알고 있는지 날짜 입력

    day_price = [] # 날짜별 가격을 저장할 리스트

    day_price = list(map(int,input().split())) # 리스트 안에 가격 입력받기 / 띄어쓰기로 구분

    high_price = 0  # 가장 높은 가격 저장할 변수

    profit = 0 # 이윤

    for day_in in day_price[::-1]: # 마지막 날부터 비교를 해간다고 가정
        if high_price < day_in:  # 미래의 가격이 현재의 가격보다 비쌀경우
            high_price = day_in  # 가장 높은 가격이므로 가장 높은 가격 변수에 저장
        
        elif high_price > day_in: # 미래의 가격이 현재의 가격보다 싼 경우
            profit += high_price - day_in # 미래의 가격에서 현재 가격을 뺀 남은 수를 이윤에 더하기

    print(f'#{test_case + 1} {profit}') # 출력
        