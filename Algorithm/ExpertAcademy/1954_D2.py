# 1954. 달팽이 숫자
T = int(input()) # 테스트케이스

# 로직 x가 N까지 1 씩 증가하면서 차례로 생성
# y 가 N까지 1씩 증가
# x가 N-1 까지 1씩 감소
# y가 N-1 까지 1씩 감소
# x가 N-1 까지 1씩 증가
for test in range(T):
    
    N = int(input()) # 첫줄 숫자

    arr = []
    
    for x in range(N):
        arr.append([]) # 새로운 내부 배열 선언
        for y in range(N):
            arr[x].append(0) # N * N 배열을 0으로 채워서 완성

    # 인덱스에 접근할 변수들
    row = 0         # 위 아래 위치 초기값
    col = -1        # 왼 오 위치 초기값 -1 을 넣어준 이유는 for문에서 1을 더하면서 시작하기 때문
    cnt = 1         # 행, 열에 영향을 줄 변수( * -1 ) 을 통해 스위칭(방향 전환) 가능
    trans = 1
    
    while N > 0: # 달팽이가 더 이상 움직일 곳이 없을때까지 이동
        for i in range(N): # N 칸 이동
            col += trans # 왼오 좌표 조정
            arr[row][col] = cnt # 이동한 순서 넣어주기
            cnt += 1 # 다음 이동한 순서 넘버
        
        N -= 1 # 이동거리가 한칼씩 줄어드는 식
        for z in range(N):
            row += trans # 상하 좌표 조정
            arr[row][col] = cnt 
            cnt += 1
        trans *= -1
        
    print(f'#{test+1}')  # 몇번째 결과인지
    for result in arr: # 리스트별로 대입
        for result_num in result: # 리스트 안에서 하나씩 가져와서 넣기
            print(result_num, end=' ') # print함수의 끝을 공백으로 바꾸기
        print() # 줄바꿈