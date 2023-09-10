# 1012 유기농 배추
# 인접해 있지않은 땅이 총 몇개인지 알아내는 코드


def search(num1, num2):
    data[num1][num2] = 1  # 데이터 방문기록 체크
    for m in range(4):
        mx, my = num1 + move_x[m], num2 + move_y[m]  # 배열넘어가는지 비교하기;
        if 0 <= mx < M and 0 <= my < N:  # M*N 범위를 벗어나지 않게끔
            if arr[mx][my] == 1 and data[mx][my] == 0:  # 배추가 있고, 방문기록이 없을시
                search(mx, my)


move_x = [0, 1, 0, -1]  # 오 아 왼 위
move_y = [1, 0, -1, 0]
T = int(input())  # 테케

for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # 가로,세로,갯수
    arr = [[0]*M for _ in range(N)]  # M * N 배열 생성
    data = [[0]*M for _ in range(N)]  # 탐색 기록
    for i in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1  # 배추가 심어진 위치 표시

    count = 0  # 배추흰나비가 필요한 갯수
    for find_x in range(M):
        for find_y in range(N):
            if arr[find_x][find_y] == 1 and data[find_x][find_y] == 0:  # 배추흰나비가 있고 방문x
                search(find_x, find_y)
                count += 1  # 배추흰나비 풀기

    print(count)
