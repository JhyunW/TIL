def best_choice(product, now):  # 몇번 제품, 총 가격 합
    global result  # 값을 매번 바꾸기 위해 받아오기
    # 가지치기 : 지금의 값이 최소값보다 높을 시
    if now > result:  # 반환x
        return

    # 종료조건 : 모든 순서를 다 거쳤을 시
    if product == N:  # 값 저장
        result = now
        return

    # 반복 작업 : 모든 회사마다 한번씩
    for i in range(N):
        if visited[i] == 0:  # 0번 부터 시작하므로 다음 함수는 +1을 붙여줌
            visited[i] = 1
            best_choice(product+1, now + arr[product][i])  # 값은 해당 라인의 몇번을 더함
            visited[i] = 0  # 해당 라인을 0,1,2 인덱스를 다 돌고





T = int(input())  # 테케입력
for tc in range(1, T+1):
    N = int(input())  # 제품 수 입력
    arr = [(list(map(int, input().split()))) for _ in range(N)]  # 리스트별로 제품 수 길이 만큼의 리스트를 N개의 회사만큼
    visited = [0] * N  # 공장 돌렸는지의 유무 확인
    result = sum(sum(arr, []))  # 최저값을 저장할 공간
    best_choice(0, 0)
    print(f'#{tc} {result}')