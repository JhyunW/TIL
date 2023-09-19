# SW Expert
# 1865_동철이의 일 분배

def percent(line, per):  # 몇번라인, 확률
    global result
    if per < result:
        return
    if line == N:  # 모든 라인을 돌고 난 후
        result = per  # 현재per이 결과보다 높은 확률일 경우 대입
        return
    else:
        for i in range(N):  # N번 만큼 반복
            if arr[line][i] == 0:
                return
            else:
                if visited[i] == 0:
                    visited[i] = 1  # 1을 칠하고 탐색 시작
                    
                    percent(line+1, per * arr[line][i])  # 현재 라인의 몇번 제품 가격
                    visited[i] = 0  # 이 라인이 1번일 경우의 탐색을 다 끝낸후 지우기



T = int(input())  # 테케
for tc in range(1, T+1):
    N = int(input())  # 각 정수 pi는 확률
    # arr = [list(map(int, input().split()))]
    # for i in range(N):  # 구역별 확률 입력
    #     for j in range(N): # 확률 구하는 공식
    #         arr[i][j] /= 100
    # lambda로 줄여보면
    arr = [list(map(lambda x: int(x)/100, input().split()))for _ in range(N)]

    result = 0  # 최대 확률
    visited = [0] * N  # 지난길 체크

    percent(0, 1)
    finish = result*100
    print(f'#{tc} {finish:7f}')  # 7번째자리에서 반올림
    