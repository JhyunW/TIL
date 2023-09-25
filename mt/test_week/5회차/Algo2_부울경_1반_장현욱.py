def score(num, sco):  # 과녁번호와 현재 점수 표시
    global result  # 최고점에 변화를 주기위함
    if num == N:  # 종료조건
        if sco > result:  # 지금 최대값보다 새로 구한값이 높을 경우
            result = sco
            return
    
    for i in range(N):  # N개의 리스트이므로
        if visited[i] == 0:  # 아직 해당 과녁을 안쐈을떄
            visited[i] = 1  # 쐈다는 표시
            score(num + 1, sco + arr[num][i])  # 해당 과녁을 쐈을경우의 경우의점수
            visited[i] = 0  # 돌고 난 후 다시 0으로 초기회


T = int(input())  # 테케

for tc in range(1,T+1):
    N = int(input())  # N * N 열의 과녁, 사격횟수
    arr = [list(map(int, input().split())) for _ in range(N)]  # N * N 과녁 입력
    visited = [0] * N  # 쏜 과녁 표시
    result = 0  # 최대 점수 표시
    score(0, 0)
    
    print(f'#{tc} {result}')