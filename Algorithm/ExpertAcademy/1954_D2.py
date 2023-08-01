# 1954. 달팽이 숫자
T = int(input()) # 테스트케이스

N = int(input()) # 첫줄 숫자

snail = N * N

# 로직 x가 N까지 1 씩 증가하면서 차례로 생성
# y 가 N까지 1씩 증가
# x가 N-1 까지 1씩 감소
# y가 N-1 까지 1씩 감소
# x가 N-1 까지 1씩 증가
for test in range(T):
    
    arr = []
    
    for x in range(N):
        arr.append([]) # 새로운 내부 배열 선언
        for y in range(N):
            arr[x].append(0) # N * N 배열을 0으로 채우서 완성

    # 인덱스에 접근할 변수들
    row = 0
    col = -1
    # 인덱스마다 값을 넣어줌
    cnt = 1
    # 행, 열에 영향을 줄 변수( * -1 ) 을통해 스위칭도 가능
    trans = 1
    
    while N > 0:
        for i in range(N): # 1~N 까지 입력
            col += trans
            arr[row][col] = cnt
            cnt += 1
        
        N -= 1
        for z in range(N):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1
        
    for result in arr:
        print(result, end = ' ')
        print()