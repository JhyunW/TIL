# SW Expert extra_01_풍선팡2

t = int(input())

dy = [0, 1, -1, 0] # 기준점을 중심으로 좌우위아래
dx = [1, 0, 0, -1] # 좌표를 하나씩 찍어줄 위치점

for tc in range(1, t + 1): # 테스트케이스 반복문
    y, x = map(int, input().split()) # y와x에 각각 숫자 입력
    # 한줄씩 스플릿 입력, y줄
    arr = [list(map(int, input().split())) for _ in range(y)]

    max_num = 0 # 가장 높은 숫자를 저장할 변수
    for z in range(y): # y좌표
        for c in range(x): # x좌표
            count = arr[z][c] # 기준점 숫자 더하기

            for v in range(4): # 상하좌우반복
                my, mx = z + dy[v], c + dx[v]
                if 0 <= my < y and 0 <= mx < x: # 리스트 밖으로 안나갈 시에만
                    count += arr[my][mx] # 기준점에 나온 값 더하기

                if max_num < count: # 결과가 맥스값보다 클 시 바꾸기
                    max_num = count

    print(f'#{tc} {max_num}')







# --------------------- 풀이식 ------------------
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0   #
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j]
#             for k in range(4):
#                 ni, nj = i + di[k], j+dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     cnt += arr[ni][nj]
#
#             if max_v < cnt: # i,j 인접 풍선까찌 더하고 나면
#                 max_v = cnt
#     print(f'#{tc} {max_v}') # 모든 위치에서 더한값
