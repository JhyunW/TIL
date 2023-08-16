# SW Expert
# 어디에 단어가 들어갈 수 있을까

# N * N 크기의 단어 퍼즐을 만들려함
# 입력으로 단어 퍼즐의 모양이 주어짐
# 주어진 포들 모양에서 특정 길이K를 갖는 단어가
# 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성
# 흰 부분은 1, 검정은 0 으로 주어짐

T = int(input())  # 테스트케이스
move_x = [-1, 0, 1, 0]  # 위 왼 아 오
move_y = [0, -1, 0, 1]
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 표 크기와 단어의길이
    arr = [[] for _ in range(N)]
    for q in range(N):
        arr[q] = list(map(int, input(). split()))  # 표 모양입력

    result = 0  # 몇개가 나오는지 기록하는곳
    for x in range(N):  # N * N 을 한칸씩 돌기
        count = 0  # 몇개가 이어져 있는지 확인하기 위한 변수
        for y in range(N):
            if arr[x][y] == 1:
                count += 1
                if y == N-1:
                    if count == K:
                        result += 1
                    count = 0
            elif arr[x][y] == 0:
                if count == K:
                    result += 1
                count = 0
    for x2 in range(N):
        count = 0
        for y2 in range(N):
            if arr[y2][x2] == 1:
                count += 1
                if y2 == N-1:
                    if count == K:
                        result += 1
                    count = 0
            elif arr[y2][x2] == 0:
                if count == K:
                    result += 1
                count = 0
    print(f'#{tc} {result}')